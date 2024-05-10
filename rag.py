from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain.vectorstores.utils import filter_complex_metadata
from dotenv import load_dotenv
import os

# .env 파일을 현재 작업 디렉토리에서 로드
load_dotenv() 
GENERATOR_MODEL = os.getenv("GENERATOR_MODEL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class ChatPDF:
    vector_store = None
    retriever = None
    chain = None

    def __init__(self):
        # self.model = ChatOllama(model="mistral")  # OLLAMA의 mistral 모델 이용
        self.model = ChatOpenAI(
            temperature=0,
            max_tokens=512,
            model_name=GENERATOR_MODEL,
            openai_api_key=OPENAI_API_KEY,
            streaming=True,
        )
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=100) # PDF 텍스트 분할
        self.prompt = PromptTemplate.from_template(
            """
            <s> [INST] 너는 이제부터 Question에 대해 Answer를 생성해야 합니다.
            다음 검색된 Context 부분을 사용하여 질문에 한국말로 답하세요.
            답을 모르면 모른다고 하면 됩니다.
            최대 3개의 문장을 사용하고 답변을 간결하게 유지하세요. [/INST] </s> 
            [INST] Question: {question} 
            Context: {context} 
            Answer: [/INST]
            """
        )

    def ingest(self, pdf_file_path: str):
        docs = PyPDFLoader(file_path=pdf_file_path).load()  # 랭체인의 PDF 모듈 이용해 문서 로딩
        chunks = self.text_splitter.split_documents(docs)   # 문서를 청크로 분할
        chunks = filter_complex_metadata(chunks)  

        vector_store = Chroma.from_documents(documents=chunks, embedding=FastEmbedEmbeddings())  # 임메딩 벡터 저장소 생성 및 청크 설정
        self.retriever = vector_store.as_retriever(search_type="similarity_score_threshold",
            search_kwargs={
                "k": 3,
                "score_threshold": 0.5,
            },
        )  # 유사도 스코어 기반 벡터 검색 설정

        self.chain = ({"context": self.retriever, "question": RunnablePassthrough()} | self.prompt | self.model | StrOutputParser()) # 프롬프트 입력에 대한 모델 실행, 출력 파서 방법 설정

    def ask(self, query: str):  # 질문 프롬프트 입력 시 호출
        if not self.chain:
            return "Please, add a PDF document first."
        return self.chain.invoke(query) 

    def clear(self):  # 초기화
        self.vector_store = None
        self.retriever = None
        self.chain = None 