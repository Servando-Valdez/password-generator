from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import password


app = FastAPI(
    title="Password Generator",
    description="Generator of secure passwords",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(password.router)