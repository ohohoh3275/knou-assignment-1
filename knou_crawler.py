import requests
from bs4 import BeautifulSoup
from typing import List, Dict

# 예시 URL (실제 공지사항 URL로 교체 가능)
BASE_URL = "https://www.knou.ac.kr/knou/board/notice/list.do"


def fetch_notice_list(page: int = 1) -> List[Dict]:
    """
    공지사항 목록 페이지에서 공지 리스트를 크롤링합니다.
    """
    params = {"pageIndex": page}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    notices = []
    # 실제 HTML 구조에 맞게 selector 수정 필요
    for row in soup.select("table.board_list tbody tr"):
        title_tag = row.select_one("td.title a")
        date_tag = row.select_one("td.date")
        if not title_tag or not date_tag:
            continue
        notices.append({
            "title": title_tag.get_text(strip=True),
            "url": title_tag["href"],
            "date": date_tag.get_text(strip=True)
        })
    return notices


def fetch_notice_detail(notice_url: str) -> Dict:
    """
    공지사항 상세 페이지에서 본문을 크롤링합니다.
    """
    if not notice_url.startswith("http"):
        notice_url = "https://www.knou.ac.kr" + notice_url
    response = requests.get(notice_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    # 실제 HTML 구조에 맞게 selector 수정 필요
    content = soup.select_one("div.board_view")
    return {
        "content": content.get_text(strip=True) if content else ""
    }


if __name__ == "__main__":
    # 테스트: 1페이지 공지사항 5개만 출력
    notices = fetch_notice_list(page=1)
    for notice in notices[:5]:
        print(f"제목: {notice['title']}")
        print(f"날짜: {notice['date']}")
        print(f"URL: {notice['url']}")
        detail = fetch_notice_detail(notice['url'])
        print(f"본문: {detail['content'][:100]}...")
        print("-" * 40) 