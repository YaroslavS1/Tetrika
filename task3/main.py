from fastapi import FastAPI
from typing import Dict
from task3 import appearance

app = FastAPI()


@app.post("/")
async def timeline(params: Dict[str, list]):
    result = appearance(params)
    return result
