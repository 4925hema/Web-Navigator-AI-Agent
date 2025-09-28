Understanding & Proposed Solution:

We built a locally running AI agent that interprets natural language instructions and autonomously interacts with the web. The agent combines a local LLM (Ollama/GPT4All) for comprehension and planning with Playwright (headless Chrome) for browser automation. Users can issue commands like “search for laptops under 50k and list top 5,” and the system performs searches, clicks, fills forms, scrapes data, and returns structured outputs (JSON/CSV) entirely offline. Python + LangChain orchestrates multi-step reasoning, retries, and task chaining. Optional enhancements include task memory, error handling, voice input, GUI interaction, and exportable results.

Prototype Flow & Team Contributions:

Frontend (React): Input box for commands, displays structured results; communicates with backend via fetch API.

Server (Python Flask/FastAPI + LangChain): Receives frontend commands, sends to LLM for instruction parsing, generates browser actions, orchestrates execution flow.

Browser Execution (Playwright): Automates searches, clicks, form filling, data extraction; returns structured JSON results.

Backend-Frontend Integration: Ensures API responses are displayed neatly in the UI with error handling.

Data Persistence (MongoDB): Stores instructions, execution results, and metadata for task memory, enabling later retrieval and export to CSV/JSON.

Uniqueness & Impact:
Fully local execution ensures privacy and independence from cloud services. The agent transforms natural language into actionable web tasks, reducing manual effort and enabling structured outputs for analysis. Its multi-step reasoning, task memory, and GUI interface make it accessible to both technical and non-technical users.

Impact: Accelerates research, competitive analysis, and repetitive web tasks, empowering developers, researchers, and businesses to interact with web data efficiently while maintaining full control over execution and data security.

Tech Stack: Ollama / GPT4All, LangChain, Python, Playwright, Flask, React, MongoDB.
