from fastapi import FastAPI
from pydantic import BaseModel
import traceback

from agents.Planner import Planner
from agents.Executor import Executor
from agents.Verifier import Verifier

app = FastAPI()

planner = Planner()
executor = Executor()
verifier = Verifier()

class TaskRequest(BaseModel):
    task: str

@app.post("/run")
def run_task(req: TaskRequest):
    try:
        plan = planner.create_plan(req.task)
        results = executor.execute(plan)
        verification = verifier.verify(results)

        return {
            "status": "success",
            "plan": plan,
            "results": results,
            "verification": verification
        }

    except Exception as e:
       
        print("🔥 INTERNAL ERROR 🔥")
        traceback.print_exc()

        return {
            "status": "error",
            "message": str(e),
            "type": type(e).__name__
        }
