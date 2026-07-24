from langchain_core.prompts import PromptTemplate

summary_prompt = PromptTemplate(
    input_variablees = ['text'],
    template = """Summarize the following research paper content in a clear , concise way .
    Cover the main problem, method, and key findings.
    
    Content:
    {text}
    
    Summary:"""
)

def summarize_paper(chunks, llm , sample_size : int = 10):
    sample_chunks = chunks[:sample_size]
    combined_text = "\n\n".join(sample_chunks)
    prompt = summary_prompt.format(text= combined_text)
    response = llm.invoke(prompt)
    return response.content