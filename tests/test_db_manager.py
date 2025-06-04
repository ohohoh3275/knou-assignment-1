import unittest
from datetime import datetime
from app.db.models import DatabaseManager, Notice

class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        """테스트 전 설정"""
        self.db_manager = DatabaseManager("mongodb://localhost:27017")
        self.test_collection = self.db_manager.db.test_notices
        self.test_collection.drop()  # 테스트 컬렉션 초기화

    def tearDown(self):
        """테스트 후 정리"""
        self.test_collection.drop()
        self.db_manager.close()

    def test_create_indexes(self):
        """인덱스 생성 테스트"""
        # 인덱스 생성
        self.db_manager.notices = self.test_collection
        self.db_manager.init_db()

        # 인덱스 목록 확인
        indexes = self.test_collection.list_indexes()
        index_names = [index["name"] for index in indexes]

        # 필수 인덱스 확인
        self.assertIn("unique_url", index_names)
        self.assertIn("text_search", index_names)
        self.assertIn("category_date", index_names)
        self.assertIn("important_date", index_names)

    def test_save_and_get_notice(self):
        """공지사항 저장 및 조회 테스트"""
        self.db_manager.notices = self.test_collection
        self.db_manager.init_db()

        # 테스트 데이터 생성
        notice_data = {
            "title": "테스트 공지사항",
            "content": "테스트 내용입니다.",
            "url": "http://test.com/notice/1",
            "category": "일반",
            "department": "컴퓨터과학과",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "is_important": True,
            "attachments": ["test.pdf"]
        }

        # 공지사항 저장
        notice = Notice(**notice_data)
        self.test_collection.insert_one(notice.dict())

        # 저장된 공지사항 조회
        saved_notice = self.test_collection.find_one({"url": notice_data["url"]})
        self.assertIsNotNone(saved_notice)
        self.assertEqual(saved_notice["title"], notice_data["title"])
        self.assertEqual(saved_notice["content"], notice_data["content"])
        self.assertEqual(saved_notice["category"], notice_data["category"])
        self.assertEqual(saved_notice["department"], notice_data["department"])
        self.assertEqual(saved_notice["is_important"], notice_data["is_important"])
        self.assertEqual(saved_notice["attachments"], notice_data["attachments"])

    def test_duplicate_notice(self):
        """중복 공지사항 처리 테스트"""
        self.db_manager.notices = self.test_collection
        self.db_manager.init_db()

        # 첫 번째 공지사항 저장
        notice_data = {
            "title": "테스트 공지사항",
            "content": "테스트 내용입니다.",
            "url": "http://test.com/notice/1",
            "category": "일반",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        notice = Notice(**notice_data)
        self.test_collection.insert_one(notice.dict())

        # 동일한 URL로 두 번째 공지사항 저장 시도
        with self.assertRaises(Exception):
            self.test_collection.insert_one(notice.dict())

    def test_text_search(self):
        """텍스트 검색 테스트"""
        self.db_manager.notices = self.test_collection
        self.db_manager.init_db()

        # 테스트 데이터 저장
        notices = [
            {
                "title": "Python 프로그래밍 강좌",
                "content": "Python 기초부터 고급까지 배우는 강좌입니다.",
                "url": "http://test.com/notice/1",
                "category": "교육",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "title": "Java 프로그래밍 강좌",
                "content": "Java 기초부터 고급까지 배우는 강좌입니다.",
                "url": "http://test.com/notice/2",
                "category": "교육",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
        ]

        for notice_data in notices:
            notice = Notice(**notice_data)
            self.test_collection.insert_one(notice.dict())

        # Python 관련 공지사항 검색
        python_notices = list(self.test_collection.find(
            {"$text": {"$search": "Python"}}
        ))
        self.assertEqual(len(python_notices), 1)
        self.assertEqual(python_notices[0]["title"], "Python 프로그래밍 강좌")

    def test_category_date_index(self):
        """카테고리-날짜 인덱스 테스트"""
        self.db_manager.notices = self.test_collection
        self.db_manager.init_db()

        # 테스트 데이터 저장
        notices = [
            {
                "title": "첫 번째 공지",
                "content": "내용1",
                "url": "http://test.com/notice/1",
                "category": "일반",
                "created_at": datetime(2024, 1, 1),
                "updated_at": datetime(2024, 1, 1)
            },
            {
                "title": "두 번째 공지",
                "content": "내용2",
                "url": "http://test.com/notice/2",
                "category": "일반",
                "created_at": datetime(2024, 1, 2),
                "updated_at": datetime(2024, 1, 2)
            }
        ]

        for notice_data in notices:
            notice = Notice(**notice_data)
            self.test_collection.insert_one(notice.dict())

        # 카테고리별 최신순 정렬 확인
        sorted_notices = list(self.test_collection.find(
            {"category": "일반"}
        ).sort([("created_at", -1)]))

        self.assertEqual(len(sorted_notices), 2)
        self.assertEqual(sorted_notices[0]["title"], "두 번째 공지")
        self.assertEqual(sorted_notices[1]["title"], "첫 번째 공지")

if __name__ == '__main__':
    unittest.main() 