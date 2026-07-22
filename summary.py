from langchain_google_genai import ChatGoogleGenerativeAI

def generate_summary(docs): 
 
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        temperature=0.2  
    )  
 
    text = "\n".join(  
        doc.page_content 
        for doc in docs[:50]
    )

    prompt = f"""
    Summarize this PDF.

    Include:
    - Main topics
    - Key concepts
    - Important takeaways

    PDF Content:
    {text}
    """

    response = llm.invoke(prompt)

    return response.content
