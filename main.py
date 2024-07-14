from fastapi import FastAPI
from app.routes import auth
from app.routes import posts

app = FastAPI()

app.include_router(auth.router)
app.include_router(posts.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


