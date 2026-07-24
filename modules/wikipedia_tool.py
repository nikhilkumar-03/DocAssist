import wikipedia

def search_wikipedia(query : str) ->str:
    try:
        return wikipedia.summary(query, sentences = 3)
    
    except Exception as e:
        return "No relevant Wikipedia result found.({e})"