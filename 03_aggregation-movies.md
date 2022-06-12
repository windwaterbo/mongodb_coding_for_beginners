# Aggregation - Multi-Collection Join & One-to-Many

## Scenario

You can retrieve the movies with user comments.
- comments collection contains comments associated with specific movies.
- movies collection contains movie information, including release year, director, and reviews.
- users contains user information.

## Sample Data

Download `movies_sample_data.zip`. There are data for three collection, `movies`, `comments`, `users`. You can import to database.

## Aggregation Pipeline

Define a pipeline ready to perform the aggregation:

```js
var pipeline = [
    {"$lookup": {
      "from": "movies",
      "localField": "movie_id", 
      "foreignField": "_id",
      "as": "MovieComment",
    }},
    {
        "$lookup":{
            "from": "users", 
            "localField": "email", 
            "foreignField": "email",
            "as": "UserComment"
        }
    },
    {
        "$unwind": "$MovieComment"
    },
    {
        "$unwind": "$UserComment"
    },
    {   
        "$project":{
            "name": "$UserComment.name",
            "email" : "$UserComment.email",
            "title" : "$MovieComment.title",
            "text" : 1,
        } 
    },
    {"$unset": [
        "_id",
    ]},
  ];
```

## Execution

Execute the aggregation using the defined pipeline and also view its explain plan:

```js
db.comments.aggregate(pipeline);
```
