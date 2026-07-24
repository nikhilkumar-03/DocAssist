from langchain_core.prompts import PromptTemplate

rag_prompt = PromptTemplate(
    template = """
    Answer the question based only on the context below. 
    If the answer isn't in the context, say "I don't know."
    
    Context :
    {context}
    
    Question: {question}
    Answer :""",
    
    input_variables = ["context", "question"]
)