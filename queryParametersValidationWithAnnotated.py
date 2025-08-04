from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


# python 3.9 이상에서는 Annotated 모듈을 이용하여 확장된 형태 검증을 수행할수있다.
# Annotated을 활용하면 doc에 더 상세하게 나와 협업시 유리
# 기본적으로 변수입력은 같지만 , 뒤에 변수를 설명하는 메타데이터 값을 옵션으로 집어놈\
# 보이는 예시에서는 Query를 사용하여 optional한 값이지만 값이 입력되면 50자 미만 문자만 수신 가능하도록 설정
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id" : "Foo"}, {"item_id" : "Bar"}]}
    if q:
        results.update({"q":q})
    return results