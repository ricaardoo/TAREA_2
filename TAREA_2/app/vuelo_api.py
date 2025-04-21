
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_session
from app.models import Vuelo
from app.schemas import VueloCreate, VueloOut

router = APIRouter()

@router.post("/vuelos/", response_model=VueloOut)
def crear_vuelo(vuelo: VueloCreate, db: Session = Depends(get_session)):
    try:
        vuelo_nuevo = Vuelo(**vuelo.dict())
        db.add(vuelo_nuevo)
        db.commit()
        db.refresh(vuelo_nuevo)
        return vuelo_nuevo
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/vuelos/")
def listar_vuelos(db: Session = Depends(get_session)):
    return db.query(Vuelo).all()

@router.get("/vuelos/total")
def cantidad_vuelos(db: Session = Depends(get_session)):
    return db.query(Vuelo).count()

@router.get("/vuelos/primero")
def obtener_primero(db: Session = Depends(get_session)):
    return db.query(Vuelo).first()

@router.get("/vuelos/ultimo")
def obtener_ultimo(db: Session = Depends(get_session)):
    return db.query(Vuelo).order_by(Vuelo.id.desc()).first()
