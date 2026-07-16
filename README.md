# 🚀 FastAPI Hello World

一個使用 FastAPI 建立的簡單 REST API，部署於 Render。

## 📋 端點

| 方法 | 路由 | 回傳 |
|------|------|------|
| GET | `/` | `{"message": "Hello"}` |
| GET | `/hello` | `{"message": "Hello"}` |
| GET | `/eugenia` | `{"message": "Hi, I am Eugenia"}` |

## 🛠️ 本地執行

### 安裝依賴

```bash
pip install -r requirements.txt
```

### 啟動伺服器

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 開啟 Swagger 文件

```
http://localhost:8000/docs
```

## 🌐 部署到 Render

1. 前往 [render.com](https://render.com) → **New → Web Service**
2. 連接此 GitHub Repository
3. 填入以下設定：

| 欄位 | 值 |
|------|----|
| Runtime | `Python 3` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

4. 點擊 **Deploy Web Service**

## 📦 專案結構

```
render_test/
├── main.py           # FastAPI 主程式
├── requirements.txt  # 套件依賴
└── README.md
```
