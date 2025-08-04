from fastapi import FastAPI, Cookie

app = FastAPI()

# 클라이언트의 쿠키내 존재하는 ads_id 값을 수신해서 json형태로 결과를 출력하는 코드
@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}