from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

# 숫자데이터 검증을 위해서는 gt,lt,ge,le 파라미터 활용 가능
# greater than, less than, greater or equal, less or equal
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)], 
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results