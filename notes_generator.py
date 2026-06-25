from langchain_google_genai import ChatGoogleGenerativeAI

def generate_notes(docs):

    text = ""

    for doc in docs[:30]:
        text += doc.page_content + "\n"

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )

    prompt = f"""
Create detailed study notes.

{text}
"""

    response = llm.invoke(prompt)

    return response.content