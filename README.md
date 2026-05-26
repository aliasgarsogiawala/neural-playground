# Research AI Agent 🧠🔎

A tool-calling AI research assistant built in Python using LangChain and Claude.

This project takes a user query, searches the web and Wikipedia for relevant information, and returns a structured research response. It can also save outputs to a local file for later reference.

Built while learning AI agents, tool calling, and practical LLM workflows in Python.

---

## Features

- AI-powered research assistant
- Tool-calling agent architecture
- Web search integration
- Wikipedia search integration
- Structured responses using Pydantic
- Save research outputs locally
- Modular Python codebase

---

## How It Works

The agent:

1. Accepts a research question from the user
2. Chooses which tools to use
3. Searches for information
4. Collects and summarizes findings
5. Returns a structured response
6. Optionally saves the output to a file

---

## Tech Stack

- Python 3
- LangChain
- Anthropic Claude API *(or any LLM provider)*
- Pydantic
- DuckDuckGo Search
- Wikipedia API
- dotenv

---

## Project Structure

```bash
research-ai-agent/
│
├── main.py          # Entry point
├── tools.py         # Agent tools
├── .env             # API keys
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the repo

```bash
git clone https://github.com/yourusername/research-ai-agent.git
cd research-ai-agent
```

### Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

---

## Run Locally

```bash
python main.py
```

Then enter your research query:

```bash
What is reinforcement learning?
```

Example output:

```bash
Topic: Reinforcement Learning
Summary: ...
Sources: ...
Saved to: output.txt
```

---

## What I Learned

Through this project I explored:

- Building AI agents in Python
- Tool calling with LangChain
- LLM orchestration
- Structured output parsing
- Prompt engineering
- Working with external APIs
- Designing modular AI workflows

---

## Future Improvements

- Memory / conversation history
- Streamlit web UI
- PDF export for reports
- Multi-agent workflows
- Better source citations
- Search across custom documents
- RAG integration

---

## Author

Built by **Aliasgar Sogiawala**

Learning AI by building real projects with Python.