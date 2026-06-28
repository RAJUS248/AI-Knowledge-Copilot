from langchain_google_genai import ChatGoogleGenerativeAI
from prompts import SYSTEM_PROMPT


def get_answer(question, retriever):

    docs_found = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs_found]
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.1
    )

    prompt = f"""
{SYSTEM_PROMPT}

Document Context:
{context}

User Question:
{question}

Instructions:

- Use the document context as primary source.
- If answer is partially available, provide best possible answer.
- If user asks to generate questions, notes, summaries, MCQs or interview questions, create them using the document content.
- Do not simply say information is unavailable unless nothing relevant exists.

Answer:
"""

    response = llm.invoke(prompt)

    return response.content