from fastapi import FastAPI


def create_app():
    app = FastAPI()

    @app.get("/test")
    async def root():
        return {"message": "Hello World"}

    return app

