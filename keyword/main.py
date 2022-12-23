from typing import List
from core.extract import Extractor
from core.prep import Preper
from fastapi import FastAPI
from pydantic import BaseModel
from helpers.logger import get_logger
from fastapi.responses import JSONResponse

app = FastAPI()

class ExtractRequest(BaseModel):
    method: str
    data: List[str]
    n_best: int
    
@app.post("/v1/keyword")
async def identiy_topic(q: ExtractRequest) -> List[str]:
    try:
        get_logger().info(f"method={q.method} n_best={q.n_best} data={q.data[0][:256]}...")
    except:
        get_logger().info(f"fail to log {q}")
    q.data = Preper().preprocess(" . ".join(q.data))
    return JSONResponse(content={'data': Extractor.extract(q.method, q.data, q.n_best)}, status_code=200)

    