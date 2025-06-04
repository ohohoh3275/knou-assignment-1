from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from pymongo import MongoClient, IndexModel, ASCENDING, TEXT

class Notice(BaseModel):
    """공지사항 모델"""
    title: str = Field(..., description="공지사항 제목")
    content: str = Field(..., description="공지사항 내용")
    url: str = Field(..., description="공지사항 URL")
    category: str = Field(..., description="공지사항 카테고리")
    department: Optional[str] = Field(None, description="학과/부서")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="공지사항 작성일")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="공지사항 수정일")
    is_important: bool = Field(default=False, description="중요 공지사항 여부")
    attachments: List[str] = Field(default_factory=list, description="첨부파일 목록")

class DatabaseManager:
    """데이터베이스 관리자 클래스"""
    def __init__(self, connection_string: str = "mongodb://localhost:27017"):
        self.client = MongoClient(connection_string)
        self.db = self.client.knou_notices
        self.notices = self.db.notices

    def init_db(self):
        """데이터베이스 초기화 및 인덱스 생성"""
        # URL에 대한 유니크 인덱스 생성
        self.notices.create_index(
            [("url", ASCENDING)],
            unique=True,
            name="unique_url"
        )

        # 제목과 내용에 대한 텍스트 인덱스 생성
        self.notices.create_index(
            [
                ("title", TEXT),
                ("content", TEXT)
            ],
            name="text_search"
        )

        # 카테고리와 작성일 기준 복합 인덱스 생성
        self.notices.create_index(
            [
                ("category", ASCENDING),
                ("created_at", ASCENDING)
            ],
            name="category_date"
        )

        # 중요 공지사항과 작성일 기준 복합 인덱스 생성
        self.notices.create_index(
            [
                ("is_important", ASCENDING),
                ("created_at", ASCENDING)
            ],
            name="important_date"
        )

    def close(self):
        """데이터베이스 연결 종료"""
        self.client.close()

# 싱글톤 인스턴스
db_manager = DatabaseManager() 