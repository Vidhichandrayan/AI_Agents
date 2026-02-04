import json
import re
from llm.openai_client import call_llm


class Planner:
    def create_plan(self, task: str) -> dict:
        prompt = f"""
Task: {task}

Available tools:
- WeatherTool(city)
- GitHubTool(query)

Rules:
- Decide required tools
- Return ONLY valid JSON
- No explanations

Output format:
{{
  "steps": [
    {{"tool": "WeatherTool", "input": "city"}},
    {{"tool": "GitHubTool", "input": "query"}}
  ]
}}
"""

        raw = call_llm(prompt)

        match = re.search(r"\{[\s\S]*\}", raw)
        if not match:
            raise ValueError(f"No JSON found in LLM response: {raw}")

        try:
            plan = json.loads(match.group())
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON from planner: {match.group()}")

        
        if "steps" not in plan or not isinstance(plan["steps"], list):
            raise ValueError("Planner JSON missing steps")

        return plan
