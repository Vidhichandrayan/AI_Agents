🤖 Multi-Agent AI Task Executor

A production-ready multi-agent AI system that converts natural-language tasks into structured execution plans using an LLM, executes real third-party APIs, and verifies results deterministically — fully runnable locally on localhost.

This project was built to satisfy the assignment requirements around agent design, LLM usage, real API integration, and end-to-end execution, while keeping the system clean, testable, and explainable.

📌 Overview

The system is composed of three independent agents, each with a clearly defined responsibility:

Planner Agent (LLM-based)
Interprets the user’s natural-language task and produces a strict JSON execution plan.

Executor Agent (Tool-based)
Executes real external APIs (Weather, GitHub) according to the plan.

Verifier Agent (Rule-based)
Verifies whether tool execution succeeded without using an LLM, ensuring deterministic validation.

Important:
The LLM is used only for planning, never for data retrieval or answer generation.

🧠 Architecture Flow
User Request (Natural Language)
        ↓
Planner Agent (LLM → JSON plan)
        ↓
Executor Agent (Real API calls)
        ↓
Verifier Agent (Rule-based validation)
        ↓
Final Structured JSON Response

🔑 Key Design Principles

LLM used only for reasoning and planning

All data fetched via real external APIs

Verification is deterministic (no hallucinations)

No hard-coded responses

Token-efficient and cost-aware

Modular agents that can be tested independently

✅ Assignment Compliance (Pass / Fail)

This project meets all mandatory requirements:

✔ Multi-agent design (Planner, Executor, Verifier)

✔ LLM usage with structured outputs (JSON planning only)

✔ At least two real third-party APIs integrated

OpenWeatherMap API

GitHub Search API

✔ Complete end-to-end execution

✔ No hard-coded responses

✔ Runs locally on localhost with one command

✔ GitHub repository submission

🤖 Agent Details
🧠 Planner Agent (LLM-Based)

Uses Groq (llama-3.1-8b-instant)

Converts natural language into a strict JSON plan

No free-text explanations, no markdown output

Example Planner Output

{
  "steps": [
    { "tool": "WeatherTool", "input": "Mumbai" },
    { "tool": "GitHubTool", "input": "AI" }
  ]
}

⚙️ Executor Agent (Tool-Based)

Executes tools defined in the plan

Calls real APIs

Handles failures per tool without crashing the system

Integrated Tools

WeatherTool → OpenWeatherMap

GitHubTool → GitHub Search API

✅ Verifier Agent (Rule-Based)

No LLM usage

Confirms whether each tool executed successfully

Produces final status: success, partial, or failed

🌐 Integrated APIs
🌦 OpenWeatherMap API

Real-time weather data

Temperature, description, wind speed, humidity

🧑‍💻 GitHub Search API

Searches public repositories

Returns top repositories sorted by stars

🚀 Running the Project Locally
1️⃣ Clone the repository
git clone https://github.com/Vidhichandrayan/AI_Agents.git
cd AI_Agents

2️⃣ Create and activate a virtual environment

Windows

python -m venv venv
venv\Scripts\activate


Linux / macOS

python -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set environment variables

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_openweather_api_key
GITHUB_TOKEN=optional_github_token


.env is ignored via .gitignore.
Use .env.example as a reference.

▶️ Run the Application (One Command)
uvicorn main:app --reload


The API will be available at:

API: http://127.0.0.1:8000

Docs: http://127.0.0.1:8000/docs

🧪 Example Prompts to Test

Use the /run endpoint with the following tasks:

Get weather in Mumbai and list top AI GitHub repositories

What's the weather in Tokyo?

Find top Python machine learning repositories on GitHub

Get weather in Berlin and list Python repositories

What's the weather in New York and find data science repositories

📁 Project Structure
AI_Agents/
├── main.py               # FastAPI entry point
├── agents/
│   ├── Planner.py        # Planner Agent (LLM-based)
│   ├── Executor.py       # Executor Agent (Tool-based)
│   └── Verifier.py       # Verifier Agent (Rule-based)
├── api_use/
│   ├── weather_api.py    # OpenWeatherMap integration
│   └── github_api.py     # GitHub API integration
├── llm/
│   └── openai_client.py  # Groq LLM client
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

⚠️ Known Limitations & Trade-offs

LLM usage intentionally limited to planning

Executor does not re-plan based on intermediate results

API rate limits may restrict frequent calls

No streaming responses (synchronous execution)

Focused on correctness and clarity over autonomy

📌 Final Notes

All outputs are generated dynamically using real APIs

No responses are hard-coded

The system is designed to be simple, explainable, and evaluatable

👤 Author

Vidhi Chandrayan
GitHub: https://github.com/Vidhichandrayan

Project Repository:
👉 https://github.com/Vidhichandrayan/AI_Agents