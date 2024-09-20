from langchain_openai import ChatOpenAI
from dotenv import dotenv_values
from langchain_community.utilities import SQLDatabase
from langchain_openai import OpenAIEmbeddings



config = dotenv_values(".env")
openai_api_key=config['OPENAI_API_KEY'] 


model_gpt_4o_mini = ChatOpenAI(
      # model_name="gpt-4o-mini",
    model="gpt-4o-mini-2024-07-18",
    streaming=True,
    temperature=0.05, 
    api_key=openai_api_key
)


def format_docs(documents):
    return "\n\n".join(doc.page_content for doc in documents)
