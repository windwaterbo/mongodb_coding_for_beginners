# 🚀 API Development with Python: Quick Start Guide

本教學將帶你從零開始，使用 Python + Flask + MongoDB 建立一個 RESTful API，並透過 Postman 進行測試。

---

## 📁 專案內容

| 檔案名稱 | 說明 |
|----------|------|
| `app.py` | Flask 主程式 |
| `requirements.txt` | Python 套件清單 |
| `.env.example` | MongoDB 連線字串設定樣板 |
| `mongodb_flask_api.postman_collection.json` | Postman 測試集合 |

---

## ⚙️ 安裝與啟動步驟

### 1. 安裝套件

```bash
pip install -r requirements.txt
```

### 2. 設定環境變數

建立 `.env` 檔案，內容如下（或從 `.env.example` 複製）：

```
MONGO_URI=mongodb://localhost:27017/test_tv
```

### 3. 啟動 API Server

```bash
python app.py
```

預設會啟動在：`http://127.0.0.1:5000`

- 如果你用 MACOS 會遇到小問題
  - ❌ SSL: CERTIFICATE_VERIFY_FAILED – 因為 Python 無法驗證 MongoDB Atlas 使用的 SSL 憑證

請執行以下命令
```bash
/Applications/Python\ 3.11/Install\ Certificates.command
```
安裝後再試一次啟動 Flask


---

## 🧪 Postman 測試指南

1. 開啟 Postman
2. 匯入 `mongodb_flask_api.postman_collection.json` 檔案
3. 測試以下 API：

- `POST /api/v1/dramas`：新增戲劇
- `GET /api/v1/dramas?category=亞洲`：分類查詢
- `POST /api/v1/users`：新增使用者
- `PUT /api/v1/users`：更新追蹤片單
- `GET /api/v1/users/followedDramas`：查詢使用者追蹤戲劇資訊（含戲劇資料）

---

祝你學習愉快 🙌
