
from fastapi import FastAPI
from app.database import Base, engine
from app.vuelo_api import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def root():
    return {"mensaje": "API de Gestión de Vuelos - Lista Doblemente Enlazada"}

@app.get("/crear-bd")
def crear_base_datos():
    Base.metadata.create_all(bind=engine)
    return {"mensaje": "Base de datos creada"}
