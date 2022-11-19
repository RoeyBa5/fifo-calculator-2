from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from handlers import fifo

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app = FastAPI()
app.include_router(fifo, prefix='/api', tags=['fifo'])
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)
