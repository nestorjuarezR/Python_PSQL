from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Conexion a base datos(usuarios,contraseña,host,base de datos)
engine = create_engine("postgresql://nestorjr:123456@localhost/test")

Session = sessionmaker(bind=engine)
sesssion = Session()

Base = declarative_base()
