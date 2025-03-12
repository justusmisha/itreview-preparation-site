import uvicorn
from fastapi import FastAPI
from api.v1.yandex_endpoints import router as yandex_router


app = FastAPI()

app.include_router(yandex_router, prefix="/api", tags=["Yandex"])

if __name__ == "__main__":
    uvicorn.run(host="0.0.0.0", port=8000, log_level="info", app=app)