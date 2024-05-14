## Branch별 특징 설명
1. <a href="https://github.com/namkidong98/LLM-RAG_Tuturoial">main</a> : ChatGPT API로 LLM의 응답 생성 역할을 처리
2. <a href="https://github.com/namkidong98/LLM-RAG_Tuturoial/tree/ollama">ollama</a> : Ollama를 사용하여 로컬에 다운로드한 LLM(EEVE-Korean-10.8B)을 사용

<br>

## 설치 및 실행 방법

1. Git Clone
```
git clone https://github.com/namkidong98/Samsung_OCR-Chatbot.git
cd Samsung_OCR-Chatbot
```

2. 최상위 폴더에 .env 파일 생성 & <DUMMY>에 발급된 OpenAI의 API Key 넣기
```
#.env
# Generator
OPENAI_API_KEY = <DUMMY>
GENERATOR_MODEL = "gpt-3.5-turbo"
```

3. 가상 환경 설치 및 활성화
```linux
conda create -n samsung python=3.10
conda activate samsung
```

4. torch 설치
```linux
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

5. 나머지 dependency 설치
```linux
pip install -r requirements.txt
```

6. streamlit 실행
```linux
streamlit run app.py
```
