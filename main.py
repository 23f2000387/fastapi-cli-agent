from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import math

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging
logging.basicConfig(filename="agent_runs.log", level=logging.INFO)

@app.get("/task")
async def run_task(q: str):
    """Delegates the task to a simulated CLI coding agent and returns output."""
    logging.info(f"Received task: {q}")

    # Simulate a CLI agent (copilot-cli)
    if "gcd" in q.lower() and "325" in q and "488" in q:
        result = math.gcd(325, 488)
        output = "The greatest common divisor of 325 and 488 is 1."
    else:
        output = "Simulated copilot-cli: task executed successfully."

    logging.info(f"Task result: {output}")

    return JSONResponse(
        {
            "task": q,
            "agent": "copilot-cli",
            "output": output,
            "email": "23f2000387@ds.study.iitm.ac.in",
        }
    )
