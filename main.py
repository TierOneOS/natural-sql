import uvicorn

if __name__ == "__main__":
    uvicorn.run("api.index:app", port=3000, reload=True)