import json
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from dotenv import dotenv_values
from datetime import datetime
from utils.helper import model_gpt_4o_mini, format_docs
from langchain_core.output_parsers import StrOutputParser
from prompts.prompt import qa_system_prompt,qa_system_prompt_2
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from pathlib import Path

config = dotenv_values(".env")
openai_api_key=config['OPENAI_API_KEY'] 

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

persist_directory = Path(f"./data/kb_retriever")

def format_docs(documents):
    return "\n\n".join(doc.page_content for doc in documents)

def dict_question(input: dict):
        return input["question"]

db=FAISS.load_local(str(persist_directory), embeddings, allow_dangerous_deserialization=True)

retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 5})

qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt),
        ("human", "{question}"),
    ]
)

qa_prompt_bs = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt_2),
        ("human", "{question}"),
    ]
)

output_parser = StrOutputParser()


rag_chain = qa_prompt | model_gpt_4o_mini| output_parser

bs_chain = (
            RunnablePassthrough.assign(context=dict_question | retriever | format_docs)
        | qa_prompt_bs
        | model_gpt_4o_mini
    )

def qna_bot(question):
    ans=rag_chain.invoke({"question": question})
    # print(ans)
    return ans


def qna_bot_bs(question):
    ans=bs_chain.invoke({"question": question})
    return ans.content 