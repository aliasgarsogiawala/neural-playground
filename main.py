from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatOpenAI(model="gpt-4-turbo")
llm2 = ChatAnthropic(model="claude-4-5-sonnet")

