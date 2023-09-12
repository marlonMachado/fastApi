from pydantic import BaseModel
from typing import Optional

#clase que hereda de BaseModel
class UsuarioSchema(BaseModel):
    id: str | None = None 
    username:str
    nombre:str
    apellido:str
    contrasena:str

    
    