from fastapi import FastAPI

app = FastAPI()

# 변수명:자료형 | 기본값 or 옵션값 설정
# 아래 함수내 로직에서는 q값이 들어오는 경우에만 dict 형태인 results안의 q 값을 업데이트
# 그 이후 results을 response로 내보냄
@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id" : "Foo"}, {"item_id" : "Bar"}]}
    if q:
        results.update({"q":q})
    return results
