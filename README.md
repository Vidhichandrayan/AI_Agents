 Multi-Agent AI Task Executor

A lightweight agent-based AI system that interprets natural language tasks, plans required actions using an LLM, executes real external APIs, and verifies results — all runnable locally on localhost.

This project demonstrates agent design, controlled LLM usage, real API integration, and a working demo, as required by the assignment.

📌 Overview

The system uses three agents:

Planner Agent (LLM-based)
Decides what actions/tools are required to fulfill a user’s task.

Executor Agent (Tool-based)
Executes real external APIs (Weather, GitHub).

Verifier Agent (Rule-based)
Verifies whether execution succeeded without using an LLM.

The system avoids monolithic prompts and uses the LLM only for planning, not for data retrieval.

🏗️ Architecture
User Request
     │
     ▼
Planner Agent (LLM)
(decides steps)
     │
     ▼
Executor Agent
(calls APIs)
     │
     ▼
Verifier Agent
(validates results)
     │
     ▼
Final JSON Response

Key Design Decisions

LLM is used only for reasoning and planning

External APIs are used for real data

Verification is deterministic (no hallucinations)

Designed to be token-efficient and robust

🧠 Agents Description
1️⃣ Planner Agent

Uses an LLM (Groq – llama-3.1-8b-instant)

Converts natural language tasks into a structured execution plan

Output format (JSON):

{
  "steps": [
    { "tool": "WeatherTool", "input": "Mumbai" },
    { "tool": "GitHubTool", "input": "AI" }
  ]
}

2️⃣ Executor Agent

Executes the plan step-by-step

Calls real APIs

Supported tools:

WeatherTool

GitHubTool

3️⃣ Verifier Agent

Rule-based (no LLM)

Checks if API calls succeeded

Returns status: success, partial, or failed

🌐 Integrated APIs

This project integrates two real external APIs, as required:

OpenWeatherMap API

Fetches real-time weather data

Example output: temperature, description

GitHub Search API

Searches public repositories

Returns top repositories sorted by stars

🚀 How to Run Locally
1️⃣ Clone the repository
git clone <your-repo-url>
cd ai_agents

2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set environment variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_openweather_api_key


A .env.example file is provided for reference.

5️⃣ Run the server
python -m uvicorn main:app --reload
uvicorn main:app

Server will start at:
http://127.0.0.1:8000

🧪 Example Requests
Example 1
{
  "task": "Get weather in Mumbai and list top AI GitHub repositories"
}
Example 2
{ "task": "Get weather in London" }
Example 3
{ "task": "Find top AI repositories on GitHub" }
Example 4
{ "task": "What's the weather in Berlin and list Python repositories on GitHub" }
Example 5
{ "task": "Get weather in Tokyo" }

