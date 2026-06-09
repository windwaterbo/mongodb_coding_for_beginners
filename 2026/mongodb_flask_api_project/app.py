from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from datetime import datetime
from bson import json_util
import json
import os
from dotenv import load_dotenv

load_dotenv() 

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", "mongodb://localhost:27017/test_tv")
mongo = PyMongo(app)

dramas = mongo.db.dramas
users = mongo.db.users

# ---- DRAMA APIs ----

@app.route('/api/v1/dramas', methods=['POST'])
def add_dramas():
    data = request.get_json()
    result = dramas.insert_many(data if isinstance(data, list) else [data])
    return jsonify({"inserted_ids": [str(_id) for _id in result.inserted_ids]}), 201

@app.route('/api/v1/dramas', methods=['GET'])
def get_dramas():
    query = {}
    category = request.args.get('category')
    release_date = request.args.get('release_date')
    operator = request.args.get('operator', 'gte')

    if category:
        query['category'] = category
    if release_date:
        try:
            release_dt = datetime.strptime(release_date, "%Y-%m-%d")
            query['release_date'] = {f"${operator}": release_dt}
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    result = list(dramas.find(query))
    return Response(
        json.dumps(result, default=json_util.default, ensure_ascii=False),
        content_type="application/json"
    )

@app.route('/api/v1/dramas/tags', methods=['PUT'])
def update_top10_tags():
    data = request.get_json()
    names = data.get('names', [])
    if not names:
        return jsonify({"error": "No drama names provided"}), 400

    result = dramas.update_many(
        {"name": {"$in": names}},
        {"$set": {"tag": ["top10"]}}
    )
    return jsonify({"matched": result.matched_count, "modified": result.modified_count}), 200

@app.route('/api/v1/dramas/tags/top10', methods=['GET'])
def get_top10_dramas():
    result = list(dramas.find({"tag": "top10"}))
    return Response(
        json.dumps(result, default=json_util.default, ensure_ascii=False),
        content_type="application/json"
    )

# ---- USER APIs ----

@app.route('/api/v1/users', methods=['POST'])
def add_users():
    data = request.get_json()
    result = users.insert_many(data if isinstance(data, list) else [data])
    return jsonify({"inserted_ids": [str(_id) for _id in result.inserted_ids]}), 201

@app.route('/api/v1/users', methods=['PUT'])
def update_followed_dramas():
    data = request.get_json()
    account = data.get('account')
    dramas_list = data.get('followedDramas', [])
    if not account:
        return jsonify({"error": "Account is required"}), 400

    result = users.update_one(
        {"account": account},
        {"$set": {"followedDramas": dramas_list}}
    )
    return jsonify({"matched": result.matched_count, "modified": result.modified_count}), 200

@app.route('/api/v1/users/<account>/followedDramas', methods=['GET'])
def get_followed_dramas_by_account(account):
    result = list(users.find(
        {"account": account},
        {"_id": 0, "account": 1, "followedDramas": 1}
    ))

    if not result:
        return jsonify({"error": f"user '{account}' not found"}), 404

    return Response(
        json.dumps(result, default=json_util.default, ensure_ascii=False),
        content_type="application/json"
    )

if __name__ == '__main__':
    app.run(debug=True)
