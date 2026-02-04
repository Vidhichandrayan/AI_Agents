# 🤖 Multi-Agent AI Task Executor

A lightweight, production-ready multi-agent AI system that converts natural language tasks into structured execution plans using an LLM, executes real third-party APIs, and verifies results—fully runnable locally.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [API Documentation](#-api-documentation)
- [Agent Details](#-agent-details)
- [Example Use Cases](#-example-use-cases)
- [Project Structure](#-project-structure)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)

## 🎯 Overview

This project demonstrates a complete agent-based AI system that showcases:

- **Agent-based design** with clear separation of concerns
- **Controlled LLM usage** for planning only (no hallucinations in data retrieval)
- **Real API integration** with external services
- **Deterministic verification** without LLM overhead
- **End-to-end workflow** from natural language to verified results

### What Makes This Different?

- ✅ LLM is used **only** for reasoning and planning
- ✅ External APIs provide **real, up-to-date data**
- ✅ Verification is **deterministic** (no hallucinations)
- ✅ Token-efficient and cost-optimized
- ✅ Modular agents that are independently testable

## ✨ Features

- 🧠 **Intelligent Planning**: Natural language understanding via LLM
- 🔧 **Real API Execution**: Integration with OpenWeatherMap and GitHub APIs
- ✓ **Automated Verification**: Rule-based validation of execution results
- 🚀 **REST API Interface**: FastAPI-powered endpoints with auto-generated docs
- 🔒 **Secure Configuration**: Environment-based API key management
- 📊 **Structured Outputs**: Clean JSON responses for easy integration

## 🏗️ Architecture

```
┌─────────────────┐
│  User Request   │
│ (Natural Lang.) │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────┐
│     Planner Agent (LLM)         │
│  - Interprets user intent       │
│  - Generates execution plan     │
│  - Output: Structured JSON      │
└────────┬────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│   Executor Agent (Tool-based)   │
│  - Calls WeatherTool API        │
│  - Calls GitHubTool API         │
│  - Handles errors gracefully    │
└────────┬────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│  Verifier Agent (Rule-based)    │
│  - Validates execution results  │
│  - No LLM usage (deterministic) │
│  - Returns success/failure      │
└────────┬────────────────────────┘
         │
         ▼
┌─────────────────┐
│  JSON Response  │
└─────────────────┘
```

### Agent Responsibilities

| Agent | Type | Responsibility | Technology |
|-------|------|----------------|------------|
| **Planner** | LLM-based | Convert natural language to structured execution plan | Groq (llama-3.1-8b-instant) |
| **Executor** | Tool-based | Execute real external APIs per plan | Python, REST APIs |
| **Verifier** | Rule-based | Validate execution success deterministically | Python logic |

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- API keys for:
  - [Groq](https://console.groq.com/) (for LLM)
  - [OpenWeatherMap](https://openweathermap.org/api) (for weather data)
  - [GitHub](https://github.com/settings/tokens) (optional, for higher rate limits)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vidhichandrayan/AI_Agents.git
   cd AI_Agents
   ```

2. **Create a virtual environment**
   
   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   **Linux/macOS:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   WEATHER_API_KEY=your_openweather_api_key_here
   GITHUB_TOKEN=your_github_token_here  # Optional
   ```
   
5. **Start the server**
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the application**
   - **API Server**: http://127.0.0.1:8000
   - **Interactive Docs**: http://127.0.0.1:8000/docs
   - **Alternative Docs**: http://127.0.0.1:8000/redoc

## 📚 API Documentation

### POST `/run`

Execute a natural language task using the multi-agent system.


## 🤖 Agent Details

### 1. Planner Agent (LLM-based)

**Purpose**: Converts natural language into structured execution plans

**Key Features**:
- Uses Groq's llama-3.1-8b-instant model
- Produces strict JSON output (no free-text explanations)
- Token-optimized prompting


### 2. Executor Agent (Tool-based)

**Purpose**: Executes real external APIs based on the plan

**Integrated Tools**:

#### WeatherTool
- **API**: OpenWeatherMap
- **Functionality**: Real-time weather data
- **Output**: Temperature, description, humidity, wind speed

#### GitHubTool
- **API**: GitHub Search API
- **Functionality**: Search public repositories
- **Output**: Top repositories sorted by stars

**Error Handling**:
- Graceful degradation per tool
- Detailed error messages
- Continues execution even if one tool fails

### 3. Verifier Agent (Rule-based)

**Purpose**: Validates execution results without using an LLM

**Validation Rules**:
- Checks for required fields in responses
- Validates data types and formats
- Confirms API call success
- Returns deterministic pass/fail status


## 💡 Example Use Cases

Test the system with these natural language prompts:


### GitHub Searches + Weather Queries
```
"Find top Python machine learning repositories"
"Show me popular AI projects on GitHub"
"List trending data science repositories"
"Get weather in Mumbai and list top AI GitHub repositories"
"What's the weather in London and find Python web frameworks"
"Show weather for Paris and search for React repositories"
```

### Testing via cURL

```bash
curl -X POST "http://127.0.0.1:8000/run" \
  -H "Content-Type: application/json" \
  -d '{"task": "Get weather in Mumbai and find AI repositories"}'
```

### Testing via Python

```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/run",
    json={"task": "What's the weather in Tokyo?"}
)

print(response.json())

```
### FastAPI Run Command
```
uvicorn main:app --reload
uvicorn main:app
```

## 📁 Project Structure

```
AI_Agents/
├── main.py                 # FastAPI application entry point
├── agents/
│   ├── planner.py         # Planner Agent (LLM-based)
│   ├── executor.py        # Executor Agent (Tool-based)
│   └── verifier.py        # Verifier Agent (Rule-based)
├── tools/
│   ├── weather_tool.py    # OpenWeatherMap integration
│   └── github_tool.py     # GitHub API integration
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .env                  # Your API keys (not in git)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

### Rate Limits

- **OpenWeatherMap**: 60 calls/minute (free tier)
- **GitHub**: 10 requests/minute (unauthenticated), 30 requests/minute (with token)
- **Groq**: Check your account limits


## 🙏 Acknowledgments

- [Groq](https://groq.com/) for fast LLM inference
- [OpenWeatherMap](https://openweathermap.org/) for weather data API
- [GitHub](https://github.com/) for repository search API
- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework

## 📧 Contact

**Vidhi Chandrayan** - [GitHub](https://github.com/Vidhichandrayan)

Project Link: [https://github.com/Vidhichandrayan/AI_Agents](https://github.com/Vidhichandrayan/AI_Agents)

---
