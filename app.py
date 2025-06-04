from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from db_manager import NoticeDBManager

# 환경 변수 로드
load_dotenv()

app = Flask(__name__)
db_manager = NoticeDBManager()

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Prime Notice API is running"
    })

@app.route("/api/notices", methods=["GET"])
def get_notices():
    """
    모든 공지사항 목록을 반환합니다.
    """
    notices = db_manager.get_all_notices()
    return jsonify(notices)

@app.route("/api/notices/recent", methods=["GET"])
def get_recent_notices():
    """
    최근 공지사항 목록을 반환합니다.
    """
    notices = db_manager.get_recent_notices(limit=10)
    return jsonify(notices)

if __name__ == '__main__':
    app.run(debug=True) 