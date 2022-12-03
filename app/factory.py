from fastapi import FastAPI

from app.api.routers import router


def create_app():
    app = FastAPI()
    app.include_router(router)
    return app
