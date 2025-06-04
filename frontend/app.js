class NoticeApp {
  constructor() {
    this.notices = [];
    this.init();
  }

  async init() {
    await this.fetchNotices();
    this.renderNotices();
  }

  async fetchNotices() {
    try {
      const response = await fetch("/api/notices/recent");
      this.notices = await response.json();
    } catch (error) {
      console.error("공지사항을 불러오는데 실패했습니다:", error);
    }
  }

  renderNotices() {
    const root = document.getElementById("root");
    const noticeList = document.createElement("div");
    noticeList.className = "notice-list";

    this.notices.forEach((notice) => {
      const noticeItem = document.createElement("div");
      noticeItem.className = "notice-item";

      // 최근 3일 이내 공지는 하이라이트
      const noticeDate = new Date(notice.date);
      const threeDaysAgo = new Date();
      threeDaysAgo.setDate(threeDaysAgo.getDate() - 3);

      if (noticeDate >= threeDaysAgo) {
        noticeItem.classList.add("recent-notice");
      }

      noticeItem.innerHTML = `
                <div class="notice-title">${notice.title}</div>
                <div class="notice-date">${notice.date}</div>
                <div class="notice-summary">${notice.summary}</div>
            `;

      noticeList.appendChild(noticeItem);
    });

    root.appendChild(noticeList);
  }
}

// 앱 초기화
document.addEventListener("DOMContentLoaded", () => {
  new NoticeApp();
});
