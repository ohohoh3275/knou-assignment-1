// API 엔드포인트
const API_BASE_URL = "http://localhost:8000/api";

// DOM 요소
const noticeList = document.getElementById("notice-list");
const noticeDetail = document.getElementById("notice-detail");
const detailTitle = document.getElementById("detail-title");
const detailDate = document.getElementById("detail-date");
const detailCategory = document.getElementById("detail-category");
const detailBody = document.getElementById("detail-body");

// 로딩 상태 관리 함수
function showLoading(tabId) {
  const tabContent = document.getElementById(tabId);
  const loading = tabContent.querySelector(".loading");
  const content = tabContent.querySelector(
    ".notice-list, .notice-detail, .summary-container"
  );

  loading.classList.add("active");
  if (content) {
    content.style.display = "none";
  }
}

function hideLoading(tabId) {
  const tabContent = document.getElementById(tabId);
  const loading = tabContent.querySelector(".loading");
  const content = tabContent.querySelector(
    ".notice-list, .notice-detail, .summary-container"
  );

  loading.classList.remove("active");
  if (content) {
    content.style.display = "block";
  }
}

// 공지사항 목록 가져오기
async function fetchNotices() {
  showLoading("list");
  try {
    const response = await fetch(`${API_BASE_URL}/notices`);
    const notices = await response.json();
    displayNotices(notices.notices);
  } catch (error) {
    console.error("공지사항을 가져오는데 실패했습니다:", error);
    noticeList.innerHTML =
      '<p class="error">공지사항을 불러오는데 실패했습니다.</p>';
  } finally {
    hideLoading("list");
  }
}

// 공지사항 목록 표시
function displayNotices(notices) {
  noticeList.innerHTML = notices
    .map(
      (notice) => `
        <div class="notice-item">
            <div class="notice-header" onclick="toggleDetail(${notice.id})">
                <h3 class="notice-title">${notice.title}</h3>
                <div class="notice-meta">
                    <span class="notice-date">${formatDate(notice.date)}</span>
                    <span class="toggle-icon">▼</span>
                </div>
            </div>
            <div class="notice-content" id="notice-content-${
              notice.id
            }" style="display: none">
                <div class="notice-body">${notice.content}</div>
            </div>
        </div>
    `
    )
    .join("");
  return notices;
}

// 상세 내용 토글
function toggleDetail(noticeId) {
  const content = document.getElementById(`notice-content-${noticeId}`);
  const header = content.previousElementSibling;
  const toggleIcon = header.querySelector(".toggle-icon");

  if (content.style.display === "none") {
    content.style.display = "block";
    toggleIcon.textContent = "▲";
  } else {
    content.style.display = "none";
    toggleIcon.textContent = "▼";
  }
}

// 공지사항 상세 정보 가져오기
async function showDetail(noticeId) {
  try {
    const response = await fetch(`${API_BASE_URL}/notices/${noticeId}`);
    const notice = await response.json();

    detailTitle.textContent = notice.title;
    detailDate.textContent = formatDate(notice.date);
    detailCategory.textContent = notice.category;
    detailBody.innerHTML = notice.content;

    noticeList.classList.add("hidden");
    noticeDetail.classList.remove("hidden");
  } catch (error) {
    console.error("상세 정보를 가져오는데 실패했습니다:", error);
    alert("상세 정보를 불러오는데 실패했습니다.");
  }
}

// 목록 화면으로 돌아가기
function showList() {
  noticeDetail.classList.add("hidden");
  noticeList.classList.remove("hidden");
}

// 날짜 포맷팅
function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString("ko-KR", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}

// 초기 로드
document.addEventListener("DOMContentLoaded", fetchNotices);

// AI 요약 기능
document
  .getElementById("generateSummary")
  .addEventListener("click", async () => {
    const summaryType = document.getElementById("summaryType").value;
    const content = document.getElementById("detail-body").textContent;

    try {
      const response = await fetch("http://localhost:8000/api/summarize", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: content,
          type: summaryType,
        }),
      });

      const data = await response.json();
      document.getElementById("summaryContent").textContent = data.result;
    } catch (error) {
      console.error("요약 생성 중 오류 발생:", error);
      document.getElementById("summaryContent").textContent =
        "요약 생성 중 오류가 발생했습니다.";
    }
  });

// 목록 요약 기능
document
  .getElementById("generateListSummary")
  .addEventListener("click", async () => {
    const summaryType = document.getElementById("listSummaryType").value;
    const notices = await fetchNotices();

    // 모든 공지사항의 제목을 하나의 텍스트로 결합
    const allTitles = notices.map((notice) => notice.title).join("\n");

    try {
      const response = await fetch("http://localhost:8000/api/summarize", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: allTitles,
          type: summaryType,
        }),
      });

      const data = await response.json();
      document.getElementById("listSummaryContent").textContent = data.result;
    } catch (error) {
      console.error("목록 요약 생성 중 오류 발생:", error);
      document.getElementById("listSummaryContent").textContent =
        "목록 요약 생성 중 오류가 발생했습니다.";
    }
  });

// 탭 전환 기능
document.querySelectorAll(".tab-btn").forEach((button) => {
  button.addEventListener("click", () => {
    // 모든 탭 버튼에서 active 클래스 제거
    document
      .querySelectorAll(".tab-btn")
      .forEach((btn) => btn.classList.remove("active"));
    // 클릭된 버튼에 active 클래스 추가
    button.classList.add("active");

    // 모든 탭 콘텐츠 숨기기
    document.querySelectorAll(".tab-content").forEach((content) => {
      content.style.display = "none";
    });

    // 선택된 탭 콘텐츠 표시
    const tabId = button.getAttribute("data-tab");
    document.getElementById(tabId).style.display = "block";
  });
});
