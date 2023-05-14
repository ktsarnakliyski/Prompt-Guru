from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from db import Base, SessionLocal, engine, models

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow cross-origin requests from any domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/")
def read_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
