from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import math

app = FastAPI()

# Enable CORS for all origins (adjust if needed for security)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# POST request body model
class TaskRequest(BaseModel):
    q: str

# GET endpoint using query parameter
@app.get("/task")
def run_task_get(q: str = Query(...)):
    return process_task(q)

# POST endpoint using JSON body
@app.post("/task")
def run_task_post(request: TaskRequest):
    return process_task(request.q)_
