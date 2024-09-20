import json
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from dotenv import dotenv_values
from datetime import datetime
from utils.helper import model_gpt_4o_mini, format_docs
from langchain_core.output_parsers import StrOutputParser
from prompts.prompt import qa_system_prompt
config = dotenv_values(".env")
openai_api_key=config['OPENAI_API_KEY'] 


qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt),
        ("human", "{question}"),
    ]
)

output_parser = StrOutputParser()

rag_chain = qa_prompt | model_gpt_4o_mini| output_parser

def qna_bot(question):
    ans=rag_chain.invoke({"question": question})
    # print(ans)
    return ans