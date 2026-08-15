import uvicorn
from fastapi import FastAPI

app = FastAPI(title="FastAPI Basic Project")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from FastAPI!"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
