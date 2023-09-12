from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED
from schema.usuario_schema import UsuarioSchema
from pydantic import BaseModel
from config.db import conn
from model.usuarios import usuarios
from werkzeug.security import generate_password_hash, check_password_hash

user = APIRouter()

@user.get("/")
def root():
    return {"mensaje": "hola desde router"}
 


@user.post("/api/user",status_code=HTTP_201_CREATED)
def create_user(data_user: UsuarioSchema ):
    #print(data_user)
    new_user=data_user.dict()
    new_user["contrasena"]=generate_password_hash(data_user.contrasena, "pbkdf2:sha256:30",2)
    conn.execute(usuarios.insert().values(new_user))
    conn.commit()   
    return Response(status_code=HTTP_201_CREATED)
