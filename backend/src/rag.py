from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_openai import ChatOpenAI
from operator import itemgetter

from decouple import config

from src.qdrant import vector_store

model = ChatOpenAI(
    model_name="gpt-3.5-turbo-0125",
    openai_api_key=config("OPENAI_API_KEY"),
    temperature=0,
)

prompt_template = """
Answer the question based on the context, in a concise manner, in markdown and using bullet points where applicable.

Context: {context}
Question: {question}
Answer:
"""

prompt = ChatPromptTemplate.from_template(prompt_template)

retriever = vector_store.as_retriever()

def create_chain(top_k=4):  # Allow dynamic top_k
    chain = (
        {
            "context": retriever.with_config(top_k=top_k),
            "question": RunnablePassthrough(),
        }
        | RunnableParallel({
            "response": prompt | model,
            "context": itemgetter("context"),
            })
    )
    return chain

def get_answer_and_docs(question: str, top_k=4):  # Allow dynamic top_k
    chain = create_chain(top_k=top_k)
    response = chain.invoke(question)
    answer = response["response"].content
    context = response["context"]
    return {
        "answer": answer,
        "context": context
    }