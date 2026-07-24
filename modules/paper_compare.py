from langchain_core.prompts import PromptTemplate

compare_prompt = PromptTemplate(
    input_variables=['paper1', 'paper2'],
    template = """ Compare the following two research papers.
    Highlight their differences in approach, methodology, and key contributions.
    
    Paper 1:
    {paper1}
    
    Paper2:
    {paper2}
    
    Comparision :"""
)

def compare_papers(chunks1, chunks2, llm, sample_size: int = 5):
    text1 = "\n\n".join(chunks1[:sample_size])
    text2 = "\n\n".join(chunks2[:sample_size])
    
    prompt = compare_prompt.format(paper1 = text, paper2 = text2)
    response = llm.invoke(prompt)
    return response.content