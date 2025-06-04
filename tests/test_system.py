# import requests
# from knou_crawler import fetch_notice_list, fetch_notice_detail
# from notice_summarizer import summarize_notice
# from db_manager import NoticeDBManager
# import time

# def test_crawler():
#     print("1. 크롤러 테스트 시작...")
#     try:
#         notices = fetch_notice_list(page=1)
#         if notices:
#             print(f"✓ 크롤러 성공: {len(notices)}개의 공지사항 수집")
#             return notices[0]  # 첫 번째 공지사항 반환
#         else:
#             print("✗ 크롤러 실패: 공지사항을 가져오지 못했습니다.")
#     except Exception as e:
#         print(f"✗ 크롤러 오류: {str(e)}")
#     return None

# def test_summarizer(notice):
#     print("\n2. 요약 모듈 테스트 시작...")
#     if not notice:
#         return None
#     try:
#         detail = fetch_notice_detail(notice['url'])
#         summary = summarize_notice(detail['content'])
#         print(f"✓ 요약 성공: {summary[:100]}...")
#         return summary
#     except Exception as e:
#         print(f"✗ 요약 오류: {str(e)}")
#     return None

# def test_database(notice, summary):
#     print("\n3. 데이터베이스 테스트 시작...")
#     if not notice or not summary:
#         return
#     try:
#         db = NoticeDBManager()
#         notice_data = {
#             **notice,
#             'content': '테스트 내용',
#             'summary': summary
#         }
#         if db.save_notice(notice_data):
#             print("✓ 데이터베이스 저장 성공")
#         else:
#             print("✓ 데이터베이스 중복 체크 성공")
#     except Exception as e:
#         print(f"✗ 데이터베이스 오류: {str(e)}")

# def test_api():
#     print("\n4. API 테스트 시작...")
#     try:
#         response = requests.get('http://localhost:5000/api/notices/recent')
#         if response.status_code == 200:
#             print("✓ API 엔드포인트 성공")
#             print(f"응답 데이터: {response.json()[:1]}")  # 첫 번째 항목만 출력
#         else:
#             print(f"✗ API 오류: 상태 코드 {response.status_code}")
#     except Exception as e:
#         print(f"✗ API 연결 오류: {str(e)}")

# def test_frontend():
#     print("\n5. 프론트엔드 테스트 시작...")
#     try:
#         response = requests.get('http://localhost:5000/')
#         if response.status_code == 200:
#             print("✓ 프론트엔드 페이지 로드 성공")
#         else:
#             print(f"✗ 프론트엔드 오류: 상태 코드 {response.status_code}")
#     except Exception as e:
#         print(f"✗ 프론트엔드 연결 오류: {str(e)}")

# if __name__ == "__main__":
#     print("=== Prime Notice 시스템 테스트 시작 ===\n")
    
#     # 크롤러 테스트
#     notice = test_crawler()
#     time.sleep(1)  # API 호출 간격 조절
    
#     # 요약 모듈 테스트
#     summary = test_summarizer(notice)
#     time.sleep(1)
    
#     # 데이터베이스 테스트
#     test_database(notice, summary)
#     time.sleep(1)
    
#     # API 테스트
#     test_api()
#     time.sleep(1)
    
#     # 프론트엔드 테스트
#     test_frontend()
    
#     print("\n=== 테스트 완료 ===") 