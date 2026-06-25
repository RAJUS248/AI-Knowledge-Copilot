from langchain_google_genai import ChatGoogleGenerativeAI

def generate_index(docs):

    text = ""

    for doc in docs[:10]:
        text += doc.page_content + "\n"

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    prompt = f"""
Extract the table of contents.

List:

- Chapters
- Headings
- Topics
- Sections

Return as numbered list.

{text}
"""

    response = llm.invoke(prompt)

    return response.content