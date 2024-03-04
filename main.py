from fastapi import FastAPI
import uvicorn
from src.routes import users, auth

app = FastAPI()

app.include_router(auth.router, prefix='/api')
app.include_router(users.router, prefix='/api')
app.include_router(users.router_birth, prefix='/api')


@app.get('/')
async def home():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
