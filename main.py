from fastapi import FastAPI 

app = FastAPI(title="ToDo-project📝")

@app.get("/home/" , summary="Главная страница1️⃣")
async def home () :
    return {
        "message" : "Главная страница"
    }