import os
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

# ====== STEP 1: PATH SET KARO ======
DATA_FOLDER = r"D:\\python\\python projects"

# ====== STEP 2: PDF DATA LOAD KARO ======
def load_documents(data_folder):
    loader = DirectoryLoader(data_folder, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

# ====== STEP 3: TEXT SPLIT KARO ======
def split_documents(documents):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)
    return docs

# ====== STEP 4: VECTOR DB BANAO ======
def create_vector_db(docs):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

# ====== STEP 5: CHATBOT BANAYE ======
def create_chatbot(vectorstore):
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    chatbot = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo"),
        retriever=retriever
    )
    return chatbot

# ====== STEP 6: RUN CHATBOT ======
def main():
    print("Loading documents...")
    documents = load_documents(DATA_FOLDER)
    docs = split_documents(documents)
    vectorstore = create_vector_db(docs)
    chatbot = create_chatbot(vectorstore)

    chat_history = []
    print("AI Chatbot Ready! Type 'exit' to quit.")

    while True:
        user_input = input("Symptoms ya query: ")
        if user_input.lower() == "exit":
            break
        response = chatbot({"question": user_input, "chat_history": chat_history})
        print("AI:", response["answer"])
        chat_history.append((user_input, response["answer"]))

if __name__ == "__main__":
    main()
