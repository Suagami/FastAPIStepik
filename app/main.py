from fastapi import FastAPI
from models.models import User, Feedback

app = FastAPI()


@app.get("/")
async def read_root():
    return {'message':'hi'}



# Пример пользовательских данных (для демонстрационных целей)
fake_db = []

# Конечная точка для получения информации о пользователе по ID
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"error": "User not found"}

@app.post("/feedback/")
def post_feedback(feedback: Feedback):
    fake_db.append(feedback)
    print(fake_db)
    return {"message": f"Feedback received. Thank you, {feedback.name}!"}