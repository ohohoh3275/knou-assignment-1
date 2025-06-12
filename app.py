from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from app.models.db_manager import NoticeDBManager
from app.crawler.notice_crawler import NoticeCrawler
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

app = FastAPI(
    title="KNOU Notice API",
    description="한국방송통신대학교 공지사항 API",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 데이터베이스 매니저 초기화
db_manager = NoticeDBManager()
crawler = NoticeCrawler()

@app.get("/api/notices")
async def get_notices_api():
    try:
        notices = await crawler.async_playwright()
        return {"notices": notices}  # 리스트를 딕셔너리로 감싸서 반환
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)