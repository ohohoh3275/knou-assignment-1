from bs4 import BeautifulSoup
import requests
from datetime import datetime
from typing import List, Dict, Optional

class NoticeCrawler:
    def __init__(self):
        self.web_url = "https://smart.knou.ac.kr/smart/5923/subview.do"
        
    def get_notices(self) -> List[Dict]:
        try:
            return self._crawl_web()
        except Exception as e:
            print(f"크롤링 중 오류 발생: {str(e)}")
            return []
    
    def _crawl_web(self) -> List[Dict]:
        """일반 웹사이트에서 공지사항 크롤링"""
        response = requests.get(self.web_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        notices = []

        print(">>>>>>>>>>>>>>>>notice ")
        print(soup)
        for row in soup.select("table.board_list tbody tr"):
            title_tag = row.select_one("td.title a")
            date_tag = row.select_one("td.date")
            if not title_tag or not date_tag:
                continue
                
            notice = {
                "title": title_tag.get_text(strip=True),
                "url": title_tag["href"],
                "date": date_tag.get_text(strip=True),
                "source": "web"
            }
            
            # 상세 내용 크롤링
            detail = self.get_notice_detail(notice["url"])
            notice.update(detail)
            
            notices.append(notice)
            
        return notices
    
    def get_notice_detail(self, notice_url: str) -> Dict:
        """
        공지사항 상세 내용을 크롤링합니다.
        
        Args:
            notice_url (str): 공지사항 URL
            
        Returns:
            Dict: 공지사항 상세 정보
        """
        if not notice_url.startswith("http"):
            notice_url = "https://www.knou.ac.kr" + notice_url
            
        response = requests.get(notice_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        content = soup.select_one("div.board_view")
        return {
            "content": content.get_text(strip=True) if content else "",
            "category": self._extract_category(soup)
        }
    
    def _extract_category(self, soup: BeautifulSoup) -> str:
        """공지사항 카테고리 추출"""
        category_tag = soup.select_one("span.category")
        return category_tag.get_text(strip=True) if category_tag else "일반" 