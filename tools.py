from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool
from datetime import datetime

# Local utility to persist research output to a file
def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """Save research data to a text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_text = f"""
--- Research Output ---
Timestamp: {timestamp}

{data}

"""

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Use this tool to save the final structured research output to a text file.",
)

# Web search wrapper
search = DuckDuckGoSearchRun()


def _web_search_wrapper(query, *args, **kwargs):
    return search.run(query, *args, **kwargs)


search_tool = Tool(
    name="web_search",
    func=_web_search_wrapper,
    description="Use this tool to search the web for recent or current information.",
)

# Wikipedia setup — keep the runner separate from the Tool to avoid recursion
api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=500,
)

wiki_runner = WikipediaQueryRun(api_wrapper=api_wrapper)


def _wiki_query_wrapper(query: str, *args, **kwargs):
    return wiki_runner.run(query, *args, **kwargs)


wiki_tool = Tool(
    name="wikipedia_query",
    func=_wiki_query_wrapper,
    description="Use this tool to query Wikipedia for summaries and content.",
)