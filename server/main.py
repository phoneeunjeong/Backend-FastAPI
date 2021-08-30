from fastapi import FastAPI

import uvicorn


app = FastAPI()


if __name__ == '__main__':
    uvicorn.run("server.main:app", reload=True)
