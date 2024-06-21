import streamlit as st
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader

# .env 파일 로드
load_dotenv()

# Gemini API 키 설정
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

genai.configure(api_key=GOOGLE_API_KEY)


def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def get_ai_response(prompt, context):
    model = genai.GenerativeModel("gemini-pro")

    # 안전 설정
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    }

    # 프롬프트 엔지니어링
    full_prompt = f"""
    당신은 경험이 풍부한 법률 전문가입니다. 다음 법률 문서의 내용을 바탕으로 사용자의 질문에 친절하고 구체적으로 답변해 주세요.
    답변 시 다음 지침을 따르세요:
    1. 법률 용어를 사용할 때는 간단한 설명을 덧붙여 주세요.
    2. 가능한 한 문서의 구체적인 부분을 인용하여 답변의 근거를 제시하세요.
    3. 답변이 불확실한 경우, 그 사실을 명시하고 추가 법률 자문을 받을 것을 권유하세요.
    4. 답변은 논리적이고 단계적으로 구성하여 사용자가 쉽게 이해할 수 있도록 해주세요.

    법률 문서 내용:
    {context}

    사용자 질문: {prompt}

    답변:
    """

    response = model.generate_content(full_prompt, safety_settings=safety_settings)
    return response.text


st.title("법률 문서 분석 챗봇 (Gemini API)")

# 파일 업로더
uploaded_file = st.file_uploader("PDF 파일을 업로드하세요", type="pdf")

if uploaded_file is not None:
    pdf_text = extract_text_from_pdf(uploaded_file)
    st.session_state["pdf_text"] = pdf_text
    st.write("PDF 파일이 성공적으로 업로드되어 분석되었습니다.")

# 사용자 입력
user_input = st.text_input("법률 문서에 대해 질문하세요:")

if st.button("질문하기"):
    if user_input and "pdf_text" in st.session_state:
        with st.spinner("AI가 응답을 생성 중입니다..."):
            response = get_ai_response(user_input, st.session_state["pdf_text"])
        st.write("AI 응답:", response)
    elif "pdf_text" not in st.session_state:
        st.warning("먼저 PDF 파일을 업로드해 주세요.")
    else:
        st.warning("질문을 입력해주세요.")

# 대화 기록
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.write(f"{message['role']}: {message['content']}")
