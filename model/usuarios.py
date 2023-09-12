from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

usuarios = Table("usuarios",meta_data,
                 Column("id",Integer,primary_key=True),
                 Column("username",String(255),nullable=False),
                 Column("nombre",String(255),nullable=False),
                 Column("apellido",String(255),nullable=False),
                 Column("contrasena",String(255),nullable=False)
                )