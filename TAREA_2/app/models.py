
from sqlalchemy import Column, String, Integer, Enum, DateTime
from app.database import Base
import enum

class EstadoVuelo(str, enum.Enum):
    programado = "programado"
    emergencia = "emergencia"
    retrasado = "retrasado"

class Vuelo(Base):
    __tablename__ = "vuelos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, nullable=False)
    estado = Column(String, nullable=False)
    hora = Column(DateTime, nullable=False)
    origen = Column(String, nullable=False)
    destino = Column(String, nullable=False)
    aerolinea = Column(String, nullable=False)
    duracion = Column(Integer, nullable=False)
