import asyncio
from playwright.async_api import async_playwright
from typing import List, Dict, Any

class NoticeCrawler:
    def __init__(self):
        self.base_url = "https://smart.knou.ac.kr/smart/5923/subview.do"
        
    async def get_notice_detail(self, page, subject_element) -> Dict[str, Any]:
        """공지사항의 상세 내용을 가져옵니다."""
        try:
            # 제목 요소 클릭
            await subject_element.click()
            await page.wait_for_load_state("networkidle")
            
            # 상세 내용 가져오기
            content = await page.locator(".view-con").text_content()
            print(content)
            return {"content": content.strip()}
        except Exception as e:
            print(f"상세 내용 크롤링 중 오류 발생: {str(e)}")
            return {"content": ""}
        
    async def async_playwright(self) -> List[Dict[str, Any]]:
        """Playwright를 사용하여 페이지 연결을 테스트합니다."""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            
            try:
                # 페이지 접속 및 로딩 대기
                await page.goto(self.base_url, wait_until="networkidle")
                
                notices = []
                subjects = page.locator(".td-subject")
                dates = page.locator(".td-date")
                count = await subjects.count()
                
                for i in range(count):
                    title = await subjects.nth(i).text_content()
                    date = await dates.nth(i).text_content()
                    
                    # 상세 내용 가져오기
                    detail = await self.get_notice_detail(page, subjects.nth(i))
                    
                    notices.append({
                        "id": i,
                        "title": title,
                        "date": date,
                        "content": detail["content"]
                    })
                    
                    # 뒤로 가기
                    await page.go_back()
                    await page.wait_for_load_state("networkidle")

                print(f"크롤링된 공지사항 수: {len(notices)}")
                
                return notices
                
            except Exception as e:
                print(f"크롤링 중 오류 발생: {str(e)}")
                return []
                
            finally:
                await browser.close()
    
    def get_notices(self) -> List[Dict[str, Any]]:
        """동기적으로 페이지 연결을 테스트합니다."""
        return asyncio.run(self.async_playwright())

