import os
from pypdf import PdfReader
from groq import Groq

from prompts.zero_shot import ZERO_SHOT_PROMPT
from prompts.few_shot import FEW_SHOT_PROMPT

# --------------------------
# PDF LOADER
# --------------------------
def load_pdf(path: str) -> str:
    """Extract text from a PDF file."""
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# --------------------------
# LLM CALL
# --------------------------
def generate_faq_llm(text: str, mode="zero-shot") -> str:
    """
    Generate FAQs using Groq LLM.
    mode: "zero-shot" or "few-shot"
    """
    # Select prompt
    if mode == "few-shot":
        prompt = FEW_SHOT_PROMPT.replace("{document}", text)
    else:
        prompt = ZERO_SHOT_PROMPT.replace("{document}", text)

    # Initialize Groq client
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    # Call Groq LLM
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=800,
    )

    return response.choices[0].message.content

# --------------------------
# Full pipeline
# --------------------------
def process_pdf(input_data: str, mode="zero-shot", is_text=False) -> str:
    """
    Full pipeline:
    - If input is PDF → load_pdf()
    - If input is raw text → use it directly
    - Returns generated FAQ string
    """
    if is_text:
        text = input_data
    else:
        text = load_pdf(input_data)

    faq = generate_faq_llm(text, mode=mode)
    return faq

# --------------------------
# Standalone testing
# --------------------------
if __name__ == "__main__":
    pdf_path = "data/sample_doc.pdf"
    text = load_pdf(pdf_path)
    print("\n=== GENERATED FAQ ===\n")
    faq = generate_faq_llm(text, mode="zero-shot")
    print(faq)
