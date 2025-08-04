from fastapi import FastAPI

app = FastAPI()

# 원래는 DB와 연동해서 데이터를 받아와야하지만
# 간단하게 하기 위해 임시로 작성
fake_items_db = [{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"}]

# 데코레이터 파라미터에서 path파라미터를 지정하지 않았음
# 함수에서 파라미터를 수신한다고 하면(skip, limit) -> 쿼리파라미터를 수신한다는 의미
# http://127.0.0.1:8000/items/?skip=0&limit=2
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]