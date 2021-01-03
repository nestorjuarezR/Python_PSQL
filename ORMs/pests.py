from models import Pets
from start import sesssion

class PetsMethods:

    @classmethod
    def create_pet(cls):
        name = input('Ingrese el nombre de la Mascota: ')
        age = int(input('Ingrese la edad de la Mascota: '))
        pet = Pets(name,age)
        sesssion.add(pet)
        sesssion.commit()
        print('Mascota registrada con exito')

    @classmethod
    def show_all(cls):
        pets = sesssion.query(Pets).all()
        print('<--- *Mascotas Registradas* --->')
        for pet in pets:
            print(pet)
            print('<----->')

    @classmethod
    def show_one(cls):
        id_pet = int(input('Ingrese el ID del registro que desea consultar: '))
        pet = sesssion.query(Pets).get(id_pet)
        print(pet)

    @classmethod
    def delete_pet(cls):
        id_pet = int(input('Ingrese el ID del registro que desea eliminar: '))
        pet = sesssion.query(Pets).get(id_pet)
        sesssion.delete(pet)
        sesssion.commit()
        print('Registro eliminado con exito')

    @classmethod
    def update_pet(cls):
        id_pet = int(input('Ingrese el ID del registro que desea actualizar: '))
        pet = sesssion.query(Pets).get(id_pet)
        pet.name = input('Ingrese el nombre de la Mascota: ')
        pet.age = int(input('Ingrese la edad de la mascota: '))
        sesssion.commit()
        print('Registro actualizado')

    @classmethod
    def filter_name(cls):
        name = input('Ingrese el nombre de la mascota: ')
        pets = sesssion.query(Pets).filter(Pets.name == name)
        for pet in pets:
            print('----')
            print(pet)

    @classmethod
    def filter_first(cls):
        name = input('Ingrese el nombre de la mascota: ')
        pets = sesssion.query(Pets).filter(Pets.name == name)    
        print(pets)   

    @classmethod
    def filter_age(cls):
        age = input('Ingrese la edad de la mascota: ')
        pets = sesssion.query(Pets).filter(Pets.age == age)  #Pets.age<=age
        for pet in pets:
            print('----')
            print(pet)


#PetsMethods.create_pet()
#PetsMethods.show_all()
#PetsMethods.show_one()
#PetsMethods.delete_pet()
#PetsMethods.update_pet()
PetsMethods.filter_age()
