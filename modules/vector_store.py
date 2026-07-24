from langchain_community.vectorstores import Chroma

def create_vector_store(chunks, embedder):
    vector_store = Chroma.from_texts(
        texts=chunks,
        embedding=embedder
        
    )
    
    return vector_store

