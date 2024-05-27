## Branch별 특징 설명
1. <a href="https://github.com/namkidong98/LLM-RAG_Tuturoial">main</a> : ChatGPT API로 LLM의 응답 생성 역할을 처리
2. <a href="https://github.com/namkidong98/LLM-RAG_Tuturoial/tree/ollama">ollama</a> : Ollama를 사용하여 로컬에 다운로드한 LLM(EEVE-Korean-10.8B)을 사용
3. <a href="https://github.com/namkidong98/LLM-RAG_Tuturoial/tree/ngrok-ollama">ngrok-ollama</a> : Colab GPU를 사용하여 Ollama를 구동하여 EEVE-Korean-10.8B을 사용

<br>

## 설치 방법

1. Git Clone
```
git clone -b ngrok-ollama https://github.com/namkidong98/LLM-RAG_Tutorial.git
cd LLM-RAG_Tutorial
```

2. 가상 환경 설치 및 활성화
```
conda create -n samsung python=3.10
conda activate samsung
```

3. torch 설치
```
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

4. 나머지 dependency 설치
```
pip install -r requirements.txt
```

<br>

5. Colab(or GPU 서버)에서 ollama_colab.ipynb을 업로드하여 실행
<img width=800 src="https://github.com/namkidong98/LLM-RAG_Tutorial/assets/113520117/664672c8-ad70-4bd8-b5dd-07a51755ad49">

- ollama branch의 5번(huggingface 모델 다운로드), 6번(modelfile 작성 및 ollama create)를 처리하는 코드
- 해당 서버에서 발급되는 URL을 llm_rag.py의 BASE_URL에 할당
<img width=800 src="https://github.com/namkidong98/LLM-RAG_Tutorial/assets/113520117/3654f4cc-a4cc-421b-87e6-35413edc3ef8">

<br><br>

6. streamlit 실행
```
streamlit run app.py
```
