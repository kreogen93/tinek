import uvicorn


if __name__ == "__main__":
    uvicorn.run("app.factory:create_app", reload=True, host="127.0.0.1", port=8080, factory=True)
