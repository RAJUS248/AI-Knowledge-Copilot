from langchain_google_genai import ChatGoogleGenerativeAI

def generate_mcqs(docs):

    text = ""

    for doc in docs[:20]:
        text += doc.page_content + "\n"

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )

    prompt = f"""
Generate 20 MCQs with answers
from this PDF.

{text}
"""

    response = llm.invoke(prompt)

    return response.content