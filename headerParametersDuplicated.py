from fastapi import FastAPI, Header

app = FastAPI()

# 헤더가 같은 이름으로 여러개 수신되는 경우 -> 리스트로 지정
@app.get("/items/")
async def read_items(x_token: list[str] | None = Header(default=None)):
    return {"X-Token values": x_token}