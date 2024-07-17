#uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  return {"message":"서버를 만들어요"}
