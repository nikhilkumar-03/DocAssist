import streamlit as st
import os

from modules.pdf_loader import load_pdf
from modules.text_splitter import split_text
from modules.embeddings import get_embedding_model
from modules.vector_store import create_vector_store
from modules.llm import get_llm
from modules.rag_chain import answer_question
from modules.citation import format_citation
from modules.summarizer import summarize_paper

st.set_page_config(page_title="DocAssist", layout="centered")
st.title("DocAssist")
st.write("Upload a research paper and ask questions about it.")

if "store" not in st.session_state:
    st.session_state.store = None
if "chunks" not in st.session_state:
    st.session_state.chunks = None

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    save_path = os.path.join("uploaded_papers", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Process Paper"):
        with st.spinner("Reading and indexing the paper..."):
            text = load_pdf(save_path)
            chunks = split_text(text)
            embedder = get_embedding_model()
            store = create_vector_store(chunks, embedder)

            st.session_state.store = store
            st.session_state.chunks = chunks

        st.success("Paper processed! You can now ask questions below.")

if st.session_state.store is not None:
    st.subheader("Summarize Paper")
    if st.button("Generate Summary"):
        llm = get_llm()
        with st.spinner("Summarizing..."):
            summary = summarize_paper(st.session_state.chunks, llm)
        st.markdown("### Summary")
        st.write(summary)

    st.subheader("Ask a question")
    question = st.text_input("Enter your question")

    if st.button("Get Answer") and question:
        llm = get_llm()
        with st.spinner("Thinking..."):
            answer, source_label, used_chunks = answer_question(
                st.session_state.store, llm, question
            )
            citation = format_citation(source_label, used_chunks)

        st.markdown("### Answer")
        st.write(answer)

        st.markdown(f"**Source:** {citation['source']}")
        if citation["details"]:
            with st.expander("View source snippets"):
                for snippet in citation["details"]:
                    st.write(snippet)