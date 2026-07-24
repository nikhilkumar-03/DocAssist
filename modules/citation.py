def format_citation(source_label: str, chunks=None):
    if source_label == "document":
        return {
            "source": "Uploaded Document",
            "details": [c.page_content[:150] + "..." for c in chunks] if chunks else []
        }
    label_map = {
        "wikipedia": "Wikipedia",
        "duckduckgo": "DuckDuckGo Search",
        "arxiv": "arXiv"
    }
    return {
        "source": label_map.get(source_label, "Unknown"),
        "details": []
    }