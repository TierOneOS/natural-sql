import uvicorn
from api.index import app

if __name__ == "__main__":
    uvicorn.run("api.index:app", port=8000, reload=True)