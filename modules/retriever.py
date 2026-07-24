def retrieve_chunks(store, query: str, k: int = 5, score_threshold: float = 1.2):
    results = store.similarity_search_with_score(query, k = k)
    relevant = [doc for doc, score in results if score <= score_threshold]
    return relevant