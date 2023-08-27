from fastapi import FastAPI
from routers import password

app = FastAPI(
    title="Password Generator",
    description="Generator of secure passwords",
)

app.include_router(password.router)