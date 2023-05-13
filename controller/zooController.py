import model.animal as animalModel
import view.zooView as view
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
            datos = self.view.crear_animal(self.model)
            nuevo_animal = animalModel.Animal(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7], datos[8], datos[9])
            self.model.registroAn[datos[3]] = nuevo_animal
            print("success")
            #self.view.mostrar_mensaje_exitoso(f"Se ha agregado a {datos[0]} correctamente")
        if opcion == 5:
            id = self.view.preguntar_id()
            if self.model.buscar_animal_id(id) is None:
                print("no existe id")
                #self.view.mostrar_mensaje_error(f"El id '{id}' no corresponde a ningun animal")}
            else:




