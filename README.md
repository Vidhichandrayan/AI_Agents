Multi-Agent AI Task Executor (LLM-Driven Planner with Real API Execution)

A lightweight multi-agent AI system that converts natural language tasks into structured execution plans using an LLM, executes real third-party APIs, and verifies results — fully runnable locally on localhost.

This project demonstrates agent-based design, controlled LLM usage, real API integration, and a complete end-to-end workflow, as required by the assignment.

📌 Overview

The system is composed of three independent agents, each with a clear responsibility:

Planner Agent (LLM-based)
Interprets the user’s natural language task and produces a structured JSON execution plan.

Executor Agent (Tool-based)
Executes real external APIs (Weather, GitHub) according to the plan.

Verifier Agent (Rule-based)
Verifies whether tool execution succeeded without using an LLM, ensuring deterministic validation.

The LLM is used only for planning, not for data retrieval.

🧠 Architecture Flow

User Request
→ Planner Agent (LLM generates execution plan)
→ Executor Agent (calls real APIs)
→ Verifier Agent (validates results)
→ Final JSON Response

🔑 Key Design Decisions

LLM is used only for reasoning and planning

External APIs are used for real, up-to-date data

Verification is deterministic (no hallucinations)

Designed to be token-efficient and robust

Agents are modular and independently testable

🤖 Agents Description
Planner Agent

Uses an LLM (Groq – llama-3.1-8b-instant)

Converts natural language tasks into a strict JSON plan

No explanations or free-text output

Example Planner Output

{
  "steps": [
    { "tool": "WeatherTool", "input": "Mumbai" },
    { "tool": "GitHubTool", "input": "AI" }
  ]
}

Executor Agent

Executes tools defined in the plan

Calls real external APIs

Handles failures gracefully per tool

Verifier Agent

Rule-based (no LLM usage)

Confirms whether each tool executed successfully

Produces a final verification status

🌐 Integrated APIs

This project integrates two real third-party APIs, as required:

OpenWeatherMap API

Fetches real-time weather data

Example outputs: temperature, description, wind speed

GitHub Search API

Searches public repositories

Returns top repositories sorted by stars

🚀 Running the Project Locally
1. Clone the repository
git clone https://github.com/Vidhichandrayan/AI_Agents.git
cd AI_Agents

2. Create and activate a virtual environment
python -m venv venv


Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Set environment variables

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_openweather_api_key
GITHUB_TOKEN=optional_github_token


A .env.example file can be used as reference.

5. Run the server
uvicorn main:app --reload



Server will start at:

http://127.0.0.1:8000


API documentation:

http://127.0.0.1:8000/docs

🧪 Example Prompts to Test

1. You can test the system using the /run endpoint with the following example tasks:

2. Get weather in Mumbai and list top AI GitHub repositories

3. What's the weather in Tokyo?

4.  Find top Python machine learning repositories on GitHub

5. Get weather in Berlin and list Python repositories

6. What's the weather in New York and find data science repositories