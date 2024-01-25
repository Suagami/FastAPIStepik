from typing import Dict

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.post("/calculate/")
async def calculate(a: int, b: int) -> dict[str, int]:
    return {'result': a + b}
