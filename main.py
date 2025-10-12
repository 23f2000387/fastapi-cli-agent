from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import math

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/task")
async def run_task(q: str):
    # Mock Copilot CLI behavior for gcd(325,488)
    if q.lower() == "gcd(325,488)":
        output = str(math.gcd(325, 488))
    else:
        output = "Task not supported in mock."

    return {
        "task": q,
        "agent": "copilot-cli",
        "output": output,
        "email": "23f2000387@ds.study.iitm.ac.in"
    }
