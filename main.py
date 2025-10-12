from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import subprocess

app = FastAPI()

# Allow GET requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/task")
async def run_task(q: str):
    try:
        # Call your CLI coding agent, e.g., copilot-cli
        result = subprocess.run(
            ["copilot", "exec", q],  # Example: replace with your actual CLI command
            capture_output=True,
            text=True,
        )
        output = result.stdout
    except Exception as e:
        output = str(e)

    return {
        "task": q,
        "agent": "copilot-cli",
        "output": output,
        "email": "23f2000387@ds.study.iitm.ac.in"
    }
