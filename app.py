from app.models.db_manager import NoticeDBManager
# from flask import Flask, jsonify
# from flask_cors import CORS
# from db_manager import DBManager
from app.crawler.notice_crawler import NoticeCrawler
import uvicorn
from fastapi import FastAPI


# 환경 변수 로드
# load_dotenv()

# app = Flask(__name__)
# # CORS 설정 추가
# CORS(app, resources={r"/*": {"origins": "*"}})

# MongoDB 연결
db_manager = NoticeDBManager()
# 크롤러 초기화
crawler = NoticeCrawler()

app = FastAPI()

@app.route('/api/notices', methods=['GET'])
def get_notices():
    notices = db_manager.get_all_notices()
    return jsonify(notices)

@app.route('/api/notices/<notice_id>', methods=['GET'])
def get_notice(notice_id):
    notice = db_manager.get_notice_by_id(notice_id)
    if notice:
        return jsonify(notice)
    return jsonify({"error": "Notice not found"}), 404

@app.route('/api/crawl', methods=['POST'])
def crawl_notices():
    try:
        # 웹사이트에서 공지사항 크롤링
        notices = crawler.get_notices()
        # DB에 저장
        for notice in notices:
            db_manager.save_notice(notice)
        return jsonify({"message": f"{len(notices)}개의 공지사항을 크롤링했습니다."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)