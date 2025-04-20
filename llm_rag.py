from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter
import os

class LLMWithRAG:
    def __init__(self, api_key):
        self.llm = ChatOpenAI(temperature=0, openai_api_key=api_key)
        self.embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    def build_vectorstore_from_url(self, url):
        loader = WebBaseLoader(url)
        docs = loader.load()
        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(docs)
        vectorstore = FAISS.from_documents(chunks, self.embeddings)
        return vectorstore

    def query(self, question, vectorstore):
        qa = RetrievalQA.from_chain_type(llm=self.llm, retriever=vectorstore.as_retriever())
        return qa.run(question)