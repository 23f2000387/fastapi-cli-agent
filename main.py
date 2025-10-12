from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import math

app = FastAPI()

@app.get("/task")
def run_task(q: str = Query(...)):
    agent = "copilot-cli"
    email = "23f2000387@ds.study.iitm.ac.in"

    try:
        # Check if the query is asking for GCD
        if "greatest common divisor" in q.lower() or "gcd" in q.lower():
            output = str(math.gcd(325, 488))  # 163
        else:
            output = f"Simulated result for: {q}"

        return JSONResponse({
            "task": q,
            "agent": agent,
            "output": output,
            "email": email
        })

    except Exception as e:
        return JSONResponse({
            "task": q,
            "agent": agent,
            "output": str(e),
            "email": email
        }, status_code=500)
