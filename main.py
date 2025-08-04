from typing import Union
from fastapi import FastAPI

app = FastAPI()

# 데코레이터
# 데코레이터를 통해 get, post등 http method requset를 fastapi app의 method를 통해 수신 가능
@app.get("/")
def read_root():
    return {"Hello": "World"}

# get 메서드를 수신함
# 파라미터 {item_id}에는 path가 들어감
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

