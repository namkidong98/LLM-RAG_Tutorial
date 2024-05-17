## Branch별 특징 설명
1. <a href="https://github.com/namkidong98/LLM-RAG_Tuturoial">main</a> : ChatGPT API로 LLM의 응답 생성 역할을 처리
2. <a href="https://github.com/namkidong98/LLM-RAG_Tuturoial/tree/ollama">ollama</a> : Ollama를 사용하여 로컬에 다운로드한 LLM(EEVE-Korean-10.8B)을 사용

<br>

## 설치 방법

1. Git Clone
```
git clone -b ollama https://github.com/namkidong98/LLM-RAG_Tutorial.git
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

5. HuggingFace에서 모델 다운     
https://huggingface.co/heegyu/EEVE-Korean-Instruct-10.8B-v1.0-GGUF/tree/main에서    
ggml-model-Q5_K_M.gguf을 다운받아 models폴더 안에 저장한다     

<img width=600 src="https://github.com/namkidong98/Samsung_OCR-Chatbot/assets/113520117/4af7058a-5869-4827-bb7a-aa0a85e86ea7">

<br><br>

6. Ollama 설치 후 Modelfile로 create

https://ollama.com/download에서 OS에 맞게 Ollama를 설치하고 실행한다    
다음 명령어를 실행     
```
ollama list
ollama create EEVE-Korean-10.8B -f models/Modelfile
ollama list                            # EEVE-Korean-10.8B:latest 생성된 것을 확인
ollama run EEVE-Korean-10.8B           # 이렇게 터미널에서 테스트 가능 
```
<img width=600 src="https://github.com/namkidong98/Samsung_OCR-Chatbot/assets/113520117/a4332c8d-6de6-4073-a2ff-670dbb121939">

<br>

7. streamlit 실행
```
streamlit run app.py
```
