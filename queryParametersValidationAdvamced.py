from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

# 파이썬은 변수에 -를 포함할 수 없음
# 하이푼을 key로 사용하는 경우에는 alias로 설정
@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            title = "Query string",
            alias = "item-query", 
            description = "Query string for the items to search \
                in the database that have a good match",
            min_length = 3,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results