from sqlalchemy import Column, Integer, String
from start import Base

class Pets(Base):

    __tablename__ = "MAscotas"

    id   = Column(Integer, primary_key=True)
    name = Column(String)
    age  = Column(Integer)


    def __init__(self, name, age):
        self.name = name
        self.age  = age
    
    def __str__(self):
        return "ID: {} \nNombre de la mascota: {} \nEdad: {}".format(self.id, self.name, self.age)

#lucas = Pets("Lucas", 10)
#print(lucas)