import requests

class GitHubTool:
    def search_repositories(self, query: str) -> dict:
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": query, "sort": "stars", "order": "desc"},
            timeout=10
        )
        r.raise_for_status()
        data = r.json()

        return {
            "top_repos": [
                {
                    "name": repo["full_name"],
                    "stars": repo["stargazers_count"],
                    "url": repo["html_url"]
                }
                for repo in data["items"][:5]
            ]
        }
