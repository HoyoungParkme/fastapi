from fastapi import FastAPI, Header

app = FastAPI()

# 쿠키 파라미터와 구분되도록 타입을 지정한다.
# None 뒤에 Header -> 헤더파라미터, Cookie -> 쿠키파라미터
@app.get("/items/")
async def read_items(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}
