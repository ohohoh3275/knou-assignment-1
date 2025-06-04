from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def summarize_notice(text: str, max_length: int = 150) -> str:
    """
    공지사항 본문을 요약합니다.
    """
    # KoBART 모델 로드 (예시 모델명, 실제 모델명으로 교체 필요)
    model_name = "gogamza/kobart-base-v2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # 입력 텍스트 토큰화
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    # 요약 생성
    summary_ids = model.generate(inputs["input_ids"], max_length=max_length, num_beams=4, length_penalty=2.0, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


if __name__ == "__main__":
    # 테스트: 예시 공지사항 본문 요약
    sample_text = """
    방송통신대학교에서는 2024년 1학기 수강신청 기간이 2월 15일부터 2월 20일까지 진행됩니다.
    수강신청은 온라인으로만 가능하며, 학생들은 반드시 본인 확인 후 신청해야 합니다.
    수강신청 기간 내에 신청하지 않은 경우, 추가 수강신청 기간이 별도로 운영됩니다.
    자세한 사항은 학사안내 게시판을 참고해 주시기 바랍니다.
    """
    summary = summarize_notice(sample_text)
    print("원문:", sample_text)
    print("요약:", summary) 