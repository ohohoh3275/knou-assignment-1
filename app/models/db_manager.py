from pymongo import MongoClient
from datetime import datetime
from typing import Dict, List


class NoticeDBManager:
    def __init__(self, connection_string: str = "mongodb://localhost:27017/"):
        self.client = MongoClient(connection_string)
        self.db = self.client["prime_notice"]
        self.notices = self.db["notices"]

    def save_notice(self, notice_data: Dict) -> bool:
        """
        공지사항 데이터를 저장합니다. 중복 체크 후 저장합니다.
        """
        # URL로 중복 체크
        if self.notices.find_one({"url": notice_data["url"]}):
            return False

        # 저장 시간 추가
        notice_data["created_at"] = datetime.now()
        self.notices.insert_one(notice_data)
        return True

    def get_all_notices(self) -> List[Dict]:
        """
        저장된 모든 공지사항을 가져옵니다.
        """
        return list(self.notices.find({}, {"_id": 0}))

    def get_recent_notices(self, limit: int = 10) -> List[Dict]:
        """
        최근 저장된 공지사항을 가져옵니다.
        """
        return list(self.notices.find({}, {"_id": 0}).sort("created_at", -1).limit(limit))


if __name__ == "__main__":
    # 테스트: DB 연결 및 데이터 저장
    db_manager = NoticeDBManager()
    
    # 예시 공지사항 데이터
    sample_notice = {
        "title": "2024년 1학기 수강신청 안내",
        "url": "https://www.knou.ac.kr/notice/123",
        "date": "2024-02-01",
        "content": "수강신청 기간: 2월 15일 ~ 2월 20일",
        "summary": "2024년 1학기 수강신청 안내"
    }
    
    # 데이터 저장
    if db_manager.save_notice(sample_notice):
        print("공지사항이 저장되었습니다.")
    else:
        print("이미 존재하는 공지사항입니다.")
    
    # 저장된 데이터 확인
    notices = db_manager.get_recent_notices(5)
    for notice in notices:
        print(f"제목: {notice['title']}")
        print(f"날짜: {notice['date']}")
        print("-" * 40) 