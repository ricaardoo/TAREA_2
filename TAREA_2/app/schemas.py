
from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class VueloCreate(BaseModel):
    codigo: str
    estado: Literal["programado", "emergencia", "retrasado"]
    hora: datetime
    origen: str
    destino: str
    aerolinea: str
    duracion: int

class VueloOut(VueloCreate):
    pass
