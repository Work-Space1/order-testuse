import pymongo
import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# 從環境變數中獲取 MongoDB 連線 URL
try:
    MONGODB_URL = os.getenv("MONGODB_URL")
    if not MONGODB_URL:
        raise ValueError("MONGODB_URL is not set in the environment variables.")
except

# 初始化 MongoDB 客戶端
client = pymongo.MongoClient(MONGODB_URL)

# 選擇資料庫
db = client['Orders']

# 提供給外部使用的集合
menus_collection = db['Orders']
