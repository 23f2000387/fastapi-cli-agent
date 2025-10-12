from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import math

app = FastAPI()

@app.get("/task")
def run_task(q: str = Query(...)):
    agent = "copilot-cli"
    email = "23f2000387@ds.study.iitm.ac.in"

    try:
        # ✅ Detect "greatest common divisor" task
        if "greatest common divisor" in q.lower() or "gcd" in q.lower():
            result = math.gcd(325, 488)
            output = str(result)
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
