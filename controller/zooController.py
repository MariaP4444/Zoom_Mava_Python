import model.animal as animalModel
import view.zooView as view
import model.Zoo as zooModel
import model.Habitat as habitatModel

class zooController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def menu_principal(self, vista, opcion, zoo):
        if opcion == 1:
            print("hola")
        if opcion == 2:
            datos = self.view.crear_animal()
            nuevo_animal = animalModel.Animal(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7], datos[8], datos[9])
            zoo.registroAn.append(nuevo_animal)
            vista.mostrar_mensaje_exitoso("Se ha agregado al animal")
