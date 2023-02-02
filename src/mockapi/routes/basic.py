from mockapi.main import app


@app.get("/{mockpoint}")
async def general(mockpoint: str):
    return {"result": mockpoint}
