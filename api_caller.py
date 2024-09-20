from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist

app = FastAPI()

@app.post('/group')
def group():
    try:
        print("Hello!!!")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))