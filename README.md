# 법률 문서 분석 챗봇

이 프로젝트는 Google의 Gemini API를 활용하여 PDF 형식의 법률 문서를 분석하고, 사용자의 질문에 답변하는 AI 챗봇을 구현한 것입니다.

## 주요 기능

- PDF 파일 업로드 및 텍스트 추출
- 법률 문서 기반 질의응답
- 사용자 친화적인 웹 인터페이스 (Streamlit 사용)
- 법률 전문가 역할의 AI 응답 생성

## 필요 조건

- Python 3.7 이상
- Streamlit
- Google Generative AI 라이브러리
- python-dotenv
- PyPDF2

## 설치 방법

1. 저장소를 클론합니다:
   git clone https://github.com/dq-hustlecoding/legal-document-chatbot.git
   cd legal-document-chatbot
2. 가상 환경을 생성하고 활성화합니다:
   python -m venv venv
   source venv/bin/activate # On Windows use venv\Scripts\activate
3. 필요한 패키지를 설치합니다:
   pip install streamlit google-generativeai python-dotenv PyPDF2
4. `.env` 파일을 생성하고 Google API 키를 추가합니다:
   GOOGLE_API_KEY=your_actual_api_key_here

## 사용 방법

1. 다음 명령어로 애플리케이션을 실행합니다:
   streamlit run src/main.py
2. 웹 브라우저에서 표시된 로컬 URL을 엽니다.

3. 인터페이스에서 PDF 파일을 업로드합니다.

4. 법률 문서에 관한 질문을 입력하고 "질문하기" 버튼을 클릭합니다.

5. AI가 생성한 답변을 확인합니다.

## 주의 사항

- 이 챗봇은 법률 조언을 제공하기 위한 것이 아니며, 전문적인 법률 자문을 대체할 수 없습니다.
- 중요한 법률 문제에 대해서는 반드시 자격을 갖춘 법률 전문가와 상담하세요.

## 기여 방법

프로젝트 개선에 기여하고 싶으시다면 pull request를 보내주세요. 큰 변경사항의 경우, 먼저 issue를 열어 논의해 주시기 바랍니다.

## 라이선스

이 프로젝트는 [MIT 라이선스](LICENSE)하에 배포됩니다.
