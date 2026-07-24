import arxiv
import time

def search_arxiv(query: str, max_results: int = 3) -> str:
    try:
        client = arxiv.Client()
        search = arxiv.Search(query=query, max_results=max_results)
        results = []
        for r in client.results(search):
            results.append(f"{r.title}\n{r.summary[:300]}...")
        return "\n\n".join(results) if results else "No relevant arXiv result found."
    except Exception as e:
        return f"arXiv search temporarily unavailable ({e})"