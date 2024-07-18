import requests
import asyncio
import time

# res = requests.get("http://127.0.0.1:8000/items/sample")

# print(res.status_code)
# print(res.text)

#http://127.0.0.1:8000/docs
#http://127.0.0.1:8000/docs


res = requests.get("http://127.0.0.1:8000/items")

print(res.status_code)
print(res.text)

postRequest = requests.post("http://127.0.0.1:8000/items/", json={
  "name":"티셔츠", "price":2000, "description":"흰 티셔츠"
})

print(postRequest.status_code)
print(postRequest.text)

headerRes = requests.get("http://127.0.0.1:8000/sample/", headers={"Authorization": "bearer A1B2C3D4"})

print(headerRes.status_code)
print(headerRes.text)
print(headerRes.headers)

# 비동기적으로 HTTP 요청을 보내고, 결과를 처리한다. 
# 지정된 시간 동안 대기하는 엔드포인트를 제공하고,
# 클라이언트는 이 엔드포인트에 요청을 보낸 후 응답을 처리한다

async def sleep_time(sec):
    loop = asyncio.get_running_loop()
    res = await loop.run_in_executor(None, lambda: requests.get(f"http://127.0.0.1:8000/sleep_time/?sec={sec}"))
    return res.text

async def main():
    print(f"메인 개시 {time.strftime('%X')}")
    response_text = await asyncio.gather(sleep_time(1), sleep_time(2))
    print(response_text)
    print(f"메인 종료 {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(main())