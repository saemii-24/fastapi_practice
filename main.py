#uvicorn main:app --reload
from fastapi import FastAPI, Query, Header, Response
from typing import Annotated, Union
from pydantic import BaseModel
import asyncio

app = FastAPI()

#아래의 경우 client 요청 경로가 items/sample로 동일할 수 있다. 
#이때는 >>먼저 쓰여진 것<<이 불러와진다.

# /items/sample 경로로 요청이 들어올 때
@app.get("/items/sample")
def read_sample():
    return {"sample_id": "샘플", "sample_name": "샘플"}

# /items/{item_id} 경로로 요청이 들어올 때
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "item_name": "티셔츠"}

items = ["티셔츠", "스커트", "부츠", "코트"]

# /items 경로로 요청이 들어올 때, skip과 limit 쿼리 매개변수를 사용
@app.get("/items")
#ge = 이상 / le = 이하 | gt = 초과 / lt = 미만
def read_items(skip: int = 0, limit: Annotated[int, Query(ge=1, le=10)] = 10):
    return {"items": items[skip:skip + limit]}


class Item(BaseModel):
  name:str
  price:float
  description:Union[str,None]=None

@app.post("/items/")
def create_item(item:Item):
  print(f"데이터를 등록합니다: {item.name},{item.price},{item.description}")
  return item

#클라이언트가 HTTP 요청을 보낼 때 포함된 특정 헤더 값을 서버에서 받아서 처리
@app.get("/sample/")
def read_sample(response: Response, authorization: Union[str, None] = Header(default=None)):
    print(authorization)
    response.headers["custom-header"] = "12345"
    return {"message": "헤더 정보를 습득했습니다."}
  
#비동기처리
@app.get("/sleep_time/")
async def sleep_time(sec:int):
  await asyncio.sleep(sec)
  return {"message": f"{sec}초"}