FEW_SHOT_PROMPT = """
You are an AI FAQ generator.

Your job is to read the document and create 6–12 high-quality FAQs.
Each FAQ must follow these rules:
- Start with “Q:” and “A:”
- Answers must be short, clear, and helpful
- Do NOT copy sentences directly from the document
- Only include relevant and meaningful FAQs
- Tone must be professional and easy to understand

Below is an example of the style to mirror:

Example FAQ:
Q: What is this product?
A: It is an API gateway that authenticates users and connects to backend services.

Q: How do I authenticate?
A: Authentication can be done using OAuth2, API keys, or JWT tokens.

---

Now generate FAQs for the following document.

Document:
{document}
"""
