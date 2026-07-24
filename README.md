# DocAssist

DocAssist is a Retrieval-Augmented Generation (RAG) app that lets you upload any PDF and ask questions about its content. If the answer isn't found in the document, DocAssist automatically falls back to external tools — Wikipedia, DuckDuckGo, and arXiv — to still give you a useful answer.

## Features

- **Upload any PDF** — not limited to academic papers, works with any document
- **Ask natural language questions** about the uploaded content
- **Smart fallback chain** — if the answer isn't in the document, DocAssist automatically searches Wikipedia → DuckDuckGo → arXiv, in that order
- **Document summarization** — generate a quick summary of the uploaded PDF
- **Source citations** — see exactly where an answer came from (document, Wikipedia, DuckDuckGo, or arXiv)

## How it works

1. **Upload & Process** — the PDF is loaded, split into chunks, embedded, and stored in an in-memory vector store (Chroma)
2. **Ask a question** — the question is embedded and matched against the most relevant chunks from the document
3. **Answer generation** — an LLM (via Groq) generates an answer using the retrieved context
4. **Fallback (if needed)** — if no relevant answer is found in the document, DocAssist queries Wikipedia, then DuckDuckGo, then arXiv, and returns the first useful result

## Tech Stack

- **Frontend:** Streamlit
- **LLM:** Groq (`llama-3.3-70b-versatile`) via `langchain-groq`
- **Embeddings:** `sentence-transformers/all-MiniLM-L6-v2` (local, via `langchain-huggingface`)
- **Vector Store:** Chroma (in-memory)
- **PDF Parsing:** PyMuPDF
- **Fallback Tools:** Wikipedia, DuckDuckGo Search, arXiv

## Project Structure

```
DocAssist/
├── app.py                     # Streamlit app entry point
├── modules/
│   ├── pdf_loader.py          # PDF text extraction
│   ├── text_splitter.py       # Chunking logic
│   ├── embeddings.py          # Embedding model setup
│   ├── vector_store.py        # Chroma vector store setup
│   ├── llm.py                 # Groq LLM setup
│   ├── retriever.py           # Chunk retrieval logic
│   ├── rag_chain.py           # Core RAG + fallback logic
│   ├── prompt.py              # Prompt template
│   ├── summarizer.py          # Document summarization
│   ├── citation.py            # Source citation formatting
│   ├── wikipedia_tool.py      # Wikipedia fallback tool
│   ├── duckduckgo_tool.py     # DuckDuckGo fallback tool
│   └── arxiv_tool.py          # arXiv fallback tool
├── requirements.txt
└── README.md
```



Developed by **Nikhil Kumar**