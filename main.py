#uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()

#아래의 경우 client 요청 경로가 items/sample로 동일할 수 있다. 
#이때는 >>먼저 쓰여진 것<<이 불러와진다.

@app.get("/items/sample")
def read_sample():
  return {"sample_id": "샘플", "sample_name": "샘플",}

@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id, "item_name": "티셔츠"}