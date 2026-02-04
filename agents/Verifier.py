class Verifier:
    def verify(self, results: dict) -> dict:
        if not results:
            return {"status": "failed"}

        for k, v in results.items():
            if isinstance(v, dict) and "error" in v:
                return {"status": "partial"}

        return {"status": "success"}
