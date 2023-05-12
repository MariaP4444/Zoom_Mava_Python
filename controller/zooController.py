import model.animal as animalModel
import view.zooView as zooView
import model.Zoo as zooModel
import model.Habitat as habitatModel

class zooController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def menu_principal(self, opcion):
        if opcion == 1:
             print("hola")
        if opcion == 2:
             self.view.crear_animal()

