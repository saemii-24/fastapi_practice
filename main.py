# fastapi 임포트
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