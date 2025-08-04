from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

# path parameter는 라우팅 역할을 하는 데코레이터로부터 정의가 됨
# 함수의 파라미터로 그 경로값을 수신
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")], #path parameter 값 정의
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results