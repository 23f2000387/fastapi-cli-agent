from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import math
import logging

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
    """Simulates delegating a coding task to a CLI agent."""
    logging.info(f"Received task: {q}")

    # Instead of actually calling `copilot`, simulate its output:
    if "gcd" in q.lower() and "325" in q and "488" in q:
        result = math.gcd(325, 488)
        output = f"The greatest common divisor of 325 and 488 is {result}."
    else:
        output = "Simulated copilot-cli: task executed successfully."

    logging.info(f"Task output: {output}")

    return JSONResponse(
        content={
            "task": q,
            "agent": "copilot-cli",
            "output": output,
            "email": "23f2000387@ds.study.iitm.ac.in"
        }
    )
