from modules.retriever import retrieve_chunks
from modules.prompt import rag_prompt
from modules.wikipedia_tool import search_wikipedia
from modules.duckduckgo_tool import search_duckduckgo
from modules.arxiv_tool import search_arxiv


def answer_question(store, llm, question: str):
    chunks = retrieve_chunks(store, question)

    if chunks:
        context = "\n\n".join([c.page_content for c in chunks])
        prompt = rag_prompt.format(context=context, question=question)
        response = llm.invoke(prompt)
        answer_text = response.content.strip()

        if answer_text.lower() not in ["i don't know.", "i don't know"]:
            return answer_text, "document", chunks

    wiki_result = search_wikipedia(question)
    if "No relevant" not in wiki_result:
        return wiki_result, "wikipedia", []

    ddg_result = search_duckduckgo(question)
    if "No relevant" not in ddg_result:
        return ddg_result, "duckduckgo", []

    arxiv_result = search_arxiv(question)
    return arxiv_result, "arxiv", []