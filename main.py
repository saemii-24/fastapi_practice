from fastapi import FastAPI

app = FastAPI()

# @app.get("/") 데코레이터가 root 함수를 루트 URL 경로(/)에 바인딩하고,
# GET 요청을 처리한다.

@app.get("/")
async def root():
    return {"message": "Hello World"}
# 문서는 http://127.0.0.1:8000/docs 에서 볼 수 있다.
# 가공되지 않은 스키마는 http://127.0.0.1:8000/openapi.json 에서 볼 수 있다.