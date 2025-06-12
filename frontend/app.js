// API 엔드포인트
const API_BASE_URL = "http://localhost:8000/api";

// DOM 요소
const noticeList = document.getElementById("notice-list");
const noticeDetail = document.getElementById("notice-detail");
const detailTitle = document.getElementById("detail-title");
const detailDate = document.getElementById("detail-date");
const detailCategory = document.getElementById("detail-category");
const detailBody = document.getElementById("detail-body");

// 공지사항 목록 가져오기
async function fetchNotices() {
  try {
    const response = await fetch(`${API_BASE_URL}/notices`);
    console.log(response);
    const notices = await response.json();

    displayNotices(notices.notices);
  } catch (error) {
    console.error("공지사항을 가져오는데 실패했습니다:", error);
    noticeList.innerHTML =
      '<p class="error">공지사항을 불러오는데 실패했습니다.</p>';
  }
}

// 공지사항 목록 표시
function displayNotices(notices) {
  noticeList.innerHTML = notices
    .map(
      (notice) => `
        <div class="notice-item" onclick="showDetail('${notice.id}')">
            <h3 class="notice-title">${notice.title}</h3>
            <div class="notice-meta">
                <span class="notice-date">${formatDate(notice.date)}</span>
            </div>
        </div>
    `
    )
    .join("");
  return notices;
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
