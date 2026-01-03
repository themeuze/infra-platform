from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import get_db, engine, Base
from .models import Skill

# Maak de tabellen aan in test.db
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Een extra "knop" om data toe te voegen via Swagger
@app.post("/api/expertise")
def create_skill(title: str, level: str, db: Session = Depends(get_db)):
    new_skill = Skill(title=title, level=level)
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill

@app.get("/api/expertise")
def get_expertise(db: Session = Depends(get_db)):
    print(f"DEBUG: Data wordt nu opgehaald uit database!") # Dit zie je in je terminal
    return db.query(Skill).all()

@app.get("/api/expertise")
def get_expertise(db: Session = Depends(get_db)):
    return db.query(Skill).all()