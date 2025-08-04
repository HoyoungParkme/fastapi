from fastapi import FastAPI
from pydantic import BaseModel

# DB역할을 하는 빈 리스트
fake_items_db = []

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

# 아래서 만든 5개의 함수가 end point가 되어서 docs에 나옴


# request boy에 item모델 데이터를 수신
# 단 바로 return하지말고 fake_items_db에 해당 값을 추가하고 입력된 값을 리턴
@app.post("/items/")
async def create_item(item: Item):
    fake_items_db.append(item)
    return item

# 조회함수
# items path에 get 요청이 들어오면 item 목록을 반환하도록 작성
# 파라미터 함수에서 배웠던것 처럼 페이지 네이션을 위해 skip, limit을 쿼리 파라미터로 수신
# 단일 items조회는 path파라미터를 수신하여 item_id 조회
# 단일 조회는 path, 다중 조회는 쿼리?
@app.get("/items/")
async def read_item_list(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# item_id는 fake_items_db의 인덱싱에 대응시킬려고 하고 있음
# 인덱스를 사용할거기 때문에 0을 위해 -1
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return fake_items_db[item_id-1]

# 업데이트
# 어떤걸 수정할지 보기 위해 item_id를 받고 어떻게 수정할건지 보기 위해 request body를 받아야함
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    fake_items_db[item_id-1] = item
    return fake_items_db[item_id-1]

# item_id를 받아 fake_itmes_db에서 인덱스로 조회해서 찾아서 삭제
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    fake_items_db.remove(fake_items_db[item_id-1])
    return {item_id: item_id}

