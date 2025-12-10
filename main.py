from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
from models import Player
from schemas import PlayerCreate, PlayerOut

# إنشاء الجداول
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# دالة جلب السيشن
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "API running successfully"}


@app.post("/players", response_model=PlayerOut)
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    new_player = Player(**player.dict())
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player


@app.get("/players", response_model=list[PlayerOut])
def get_players(db: Session = Depends(get_db)):
    return db.query(Player).all()


@app.delete("/players/{player_id}")
def delete_player(player_id: int, db: Session = Depends(get_db)):
    p = db.query(Player).filter(Player.id == player_id).first()
    if not p:
        return {"error": "Player not found"}
    
    db.delete(p)
    db.commit()
    return {"message": "Player deleted"}
