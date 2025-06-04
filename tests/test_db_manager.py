import unittest
from db_manager import NoticeDBManager
import time
from datetime import datetime

class TestNoticeDBManager(unittest.TestCase):
    def setUp(self):
        """테스트 전에 실행되는 설정"""
        self.db_manager = NoticeDBManager()
        # 테스트용 컬렉션 사용
        self.db_manager.notices = self.db_manager.db["test_notices"]
        
    def tearDown(self):
        """테스트 후에 실행되는 정리"""
        # 테스트 컬렉션 삭제
        self.db_manager.db.drop_collection("test_notices")
        
    def test_save_and_get_notice(self):
        """공지사항 저장 및 조회 테스트"""
        # 테스트 데이터
        test_notice = {
            "title": "테스트 공지사항",
            "url": f"https://test.com/notice/{int(time.time())}",
            "date": "2024-02-20",
            "content": "테스트 내용입니다.",
            "category": "테스트",
            "source": "test"
        }
        
        # 저장 테스트
        result = self.db_manager.save_notice(test_notice)
        self.assertTrue(result, "공지사항 저장 실패")
        
        # 조회 테스트
        notices = self.db_manager.get_all_notices()
        self.assertEqual(len(notices), 1, "저장된 공지사항 수가 일치하지 않음")
        
        saved_notice = notices[0]
        self.assertEqual(saved_notice["title"], test_notice["title"])
        self.assertEqual(saved_notice["url"], test_notice["url"])
        self.assertEqual(saved_notice["date"], test_notice["date"])
        self.assertEqual(saved_notice["content"], test_notice["content"])
        self.assertEqual(saved_notice["category"], test_notice["category"])
        
    def test_duplicate_notice(self):
        """중복 공지사항 저장 테스트"""
        test_notice = {
            "title": "중복 테스트",
            "url": "https://test.com/duplicate",
            "date": "2024-02-20",
            "content": "중복 테스트 내용",
            "category": "테스트",
            "source": "test"
        }
        
        # 첫 번째 저장
        result1 = self.db_manager.save_notice(test_notice)
        self.assertTrue(result1, "첫 번째 저장 실패")
        
        # 중복 저장 시도
        result2 = self.db_manager.save_notice(test_notice)
        self.assertFalse(result2, "중복 저장이 허용됨")
        
        # 저장된 데이터 수 확인
        notices = self.db_manager.get_all_notices()
        self.assertEqual(len(notices), 1, "중복 저장이 발생함")
        
    def test_get_recent_notices(self):
        """최근 공지사항 조회 테스트"""
        # 여러 개의 테스트 데이터 저장
        for i in range(5):
            notice = {
                "title": f"테스트 공지사항 {i}",
                "url": f"https://test.com/notice/{i}",
                "date": "2024-02-20",
                "content": f"테스트 내용 {i}",
                "category": "테스트",
                "source": "test",
                "created_at": datetime.now()
            }
            self.db_manager.save_notice(notice)
        
        # 최근 3개 조회
        recent_notices = self.db_manager.get_recent_notices(limit=3)
        self.assertEqual(len(recent_notices), 3, "최근 공지사항 수가 일치하지 않음")
        
if __name__ == '__main__':
    unittest.main() 