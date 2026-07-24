from ddgs import DDGS

def search_duckduckgo(query : str) -> str:
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results = 3))
        
    if not results:
        return "No relevant duckduckgo result found."
    
    return "\n\n".join([r["body"] for r in results])
