from fastapi import FastAPI
from pydantic import BaseModel

# description, tax는 값을 지정받지 않으면 None 설정
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

# 클래스에서 정의된 Item을 하단의 데코레이터에서 사용
# items라는 path가 post를 수신하도록 하고 우리가 선언한 Item을 파라미터로 받도록 설정
@app.post("/items/")
async def create_item(item: Item):
    return item
