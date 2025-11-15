import streamlit as st
from pipeline import process_pdf  # Import the pipeline function

st.set_page_config(page_title="AI FAQ Generator", layout="wide")

st.title("📄 AI FAQ Generator")
st.write("Upload a PDF or paste text to automatically generate high-quality FAQs.")

# --- Sidebar Settings ---
st.sidebar.header("Settings")
mode = st.sidebar.radio(
    "Choose FAQ Mode",
    ["Zero-Shot", "Few-Shot"]
)

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
text_input = st.text_area(
    "Or paste text manually",
    height=250,
    placeholder="Paste any paragraph, article, or documentation here…"
)

if st.button("Generate FAQ"):
    if uploaded_file:
        with st.spinner("Reading PDF and generating FAQs..."):
            pdf_path = "uploaded.pdf"
            with open(pdf_path, "wb") as f:
                f.write(uploaded_file.read())
            faqs = process_pdf(pdf_path, mode=mode.lower())

        st.success("FAQ Generated!")
        st.write("---")
        st.subheader("📘 Generated FAQs")
        st.write(faqs)

    elif text_input.strip():
        with st.spinner("Generating FAQs from text..."):
            faqs = process_pdf(text_input, mode=mode.lower(), is_text=True)

        st.success("FAQ Generated!")
        st.write("---")
        st.subheader("📘 Generated FAQs")
        st.write(faqs)

    else:
        st.error("Please upload a PDF or enter some text!")
