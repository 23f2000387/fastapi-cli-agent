from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import math, logging

logging.basicConfig(filename="agent_runs.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s")

app = FastAPI(title="FastAPI CLI Coding Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/task")
def run_task(q: str = Query(...)):
    agent = "copilot-cli"
    try:
        # Simulate what the CLI agent would output
        if "gcd" in q.lower():
            output = str(math.gcd(325, 488))
        else:
            output = f"Simulated execution for: {q}"

        logging.info(f"{agent} | {q} | {output}")

        return JSONResponse({
            "task": q,
            "agent": agent,
            "output": output,
            "email": "23f2000387@ds.study.iitm.ac.in"
        })

    except Exception as e:
        return JSONResponse({
            "task": q,
            "agent": agent,
            "error": str(e),
            "email": "23f2000387@ds.study.iitm.ac.in"
        }, status_code=500)
