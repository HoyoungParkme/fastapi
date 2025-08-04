from fastapi import FastAPI, Query

app = FastAPI()

# Annotated와 함께 사용하지 않아도 됨
# FastAPI 0.95미만에서 주로 사용하던 방식
@app.get("/items/")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
