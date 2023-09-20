from db import engine
from fastapi import FastAPI, Request
from sqlmodel import SQLModel
from models import ProductInput, Product, Category, CategoryInput
from routers import product, category
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(product.router)
app.include_router(category.router)
origins = ["*"]  # You can replace "*" with specific origins as needed

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify HTTP methods you want to allow
    allow_headers=["*"],  # You can specify allowed headers
)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
