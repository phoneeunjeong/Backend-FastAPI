from fastapi import FastAPI

import uvicorn

from server.apps import checker, teacher


app = FastAPI()

app.include_router(checker.router)
app.include_router(teacher.router)

if __name__ == '__main__':
    uvicorn.run("server.main:app", reload=True)
