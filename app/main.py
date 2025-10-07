from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config import settings
from app.database import engine, Base
from app.api.v1.endpoints import wishlist
from app import events


@asynccontextmanager
async def lifespan(app: FastAPI):
    await events.event_publisher.connect()

    Base.metadata.create_all(bind=engine)

    yield

    await events.event_publisher.close()


app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan
)

app.include_router(
    wishlist.router,
    prefix=settings.API_V1_STR,
    tags=["wishlist"]
)

@app.get("/")
async def root():
    return {"message": "Wishlist service is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}