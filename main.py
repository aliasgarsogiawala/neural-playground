from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatOpenAI(model="gpt-4o-mini")

tools = [search_tool, wiki_tool, save_tool]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are a research assistant that helps generate research summaries.
Use the available tools when needed.
Return the final answer in the required structured format.
""",
    response_format=ResearchResponse,
)

query = input("What can I help you research? ")

result = agent.invoke({
    "messages": [
        {"role": "user", "content": query}
    ]
})

structured_response = result["structured_response"]

print(structured_response)
print(structured_response.topic)
print(structured_response.summary)
print(structured_response.sources)
print(structured_response.tools_used)