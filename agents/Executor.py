from api_use.weather_api import WeatherTool
from api_use.github_api import GitHubTool

class Executor:
    def __init__(self):
        self.weather = WeatherTool()
        self.github = GitHubTool()

    def execute(self, plan: dict) -> dict:
        results = {}

        for step in plan.get("steps", []):
            tool = step["tool"]
            value = step["input"]

            if tool == "WeatherTool":
                results["weather"] = self.weather.get_weather(value)

            elif tool == "GitHubTool":
                results["github"] = self.github.search_repositories(value)

        return results
