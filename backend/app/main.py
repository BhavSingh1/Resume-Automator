from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Resume Automator - Backend", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "resume-automator-backend"}

class EchoRequest(BaseModel):
    text: str

@app.post("/api/echo")
def echo(req: EchoRequest):
    return {"echo": req.text}
