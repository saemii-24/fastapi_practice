# fastapi 임포트
from typing import Union
from fastapi import FastAPI

# fastapi 인스턴스 생성
app = FastAPI()

# @app.get("/") 데코레이터가 root 함수를 루트 URL 경로(/)에 바인딩하고,
# GET 요청을 처리한다.

#함수(작동방식("경로"))
@app.get("/")
def root():
    return {"message": "Hello World"}
# 문서는 http://127.0.0.1:8000/docs 에서 볼 수 있다.
# 가공되지 않은 스키마는 http://127.0.0.1:8000/openapi.json 에서 볼 수 있다.

# 1. 딕셔너리 반환
@app.get("/dict")
async def get_dict():
    return {"key1": "value1", "key2": "value2"}

# 2. 리스트 반환
@app.get("/list")
async def get_list():
    return ["item1", "item2", "item3"]

# 3. 단일 값 (문자열) 반환
@app.get("/string")
async def get_string():
    return "Hello, world!"

# 4. 단일 값 (정수) 반환
@app.get("/integer")
async def get_integer():
    return 42
  
  
# 경로 매개변수
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
  
  
#타입 넣은 배개변수
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

#쿼리 매개변수
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
#파이썬 리스트를 이용해 특정 범위의 아이템을 선택
#슬라이싱 구문 start:stop은 리스트의 start 인덱스부터 stop-1 인덱스까지의 아이템을 포함


#http://127.0.0.1:8000/items/?skip=0&limit=10

#선택적 매개변수
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

#쿼리 매개변수 형변환

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

#필수 쿼리 매개변수
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item