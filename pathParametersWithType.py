from fastapi import FastAPI

app = FastAPI()

# 파라미터 타입을 지정하고 싶은경우 함수 부분에서 설정
# 원래 이런식으로 타입 지정하면 뒤에 문자열 넣으면 에러나야하는데
# 이거 왜 안나지?
@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}
