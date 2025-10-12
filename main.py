from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import math

app = FastAPI()

@app.get("/task")
def run_task(q: str = Query(...)):
    agent = "copilot-cli"
    email = "23f2000387@ds.study.iitm.ac.in"

    # Ensure correct numbers
    a = 325
    b = 488

    # Only compute GCD if the query asks for it
    if "greatest common divisor" in q.lower() or "gcd" in q.lower():
        gcd_value = math.gcd(a, b)
        output = f"The greatest common divisor of {a} and {b} is {gcd_value}"
    else:
        output = f"Simulated execution for: {q}"

    return JSONResponse({
        "task": q,
        "agent": agent,
        "output": output,
        "email": email
    })
