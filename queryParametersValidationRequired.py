from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

# 입력값에 None을 입력하면 필수값이 아닌 값 자체가 Optional하게 됨
# None도 Optional형태로 입력받는 것과 입력 가능한 필수값으로 둔 형태는 구분해야함
# ...을 입력하므로써 Annotated는 필수로 입력 해야함 -> None입력 괜춘 but 입력X는 오류
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q":q})
    return results