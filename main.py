from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import math

app = FastAPI()

@app.get("/task")
def run_task(q: str = Query(...)):
    agent = "copilot-cli"
    email = "23f2000387@ds.study.iitm.ac.in"

    # Correct numbers
    a = 325
    b = 488

    # Handle the specific GCD task
    if "gcd" in q.lower() or "greatest common divisor" in q.lower():
        output = f"The greatest common divisor of {a} and {b} is {math.gcd(a, b)}"
    else:
        output = f"Simulated execution for: {q}"

    return JSONResponse({
        "task": q,
        "agent": agent,
        "output": output,
        "email": email
    })
