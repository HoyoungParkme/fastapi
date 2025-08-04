from fastapi import FastAPI

app = FastAPI()

# path 부분을 변수로 사용하고 싶다면 아래와 같이 사용
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

