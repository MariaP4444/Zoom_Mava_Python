import model.Zoo as zooModel
import model.Habitat as habitatModel
import controller.zooController as zooController

class zooView:

    def menu_principalV(self, zoo):
        opcion = -1

        while opcion != 0:
            print("\n~~~~~~~~~~~~~~~~~~~~~ ZOO:", zoo.nombre , "~~~~~~~~~~~~~~~~~~~~~\n")
            print("1. Agregar habitat")
            print("2. Agregar animal")
            print("3. Lista de habitats y animales")
            print("4. Modificar informacion de animal")
            print("5. Visitar habitat")
            print("0. Salir")
            opcion = int(input("Escoge una opcion: "))

            controlador = zooController.zooController(zoo, self)
            controlador.menu_principal(opcion)

            if opcion == 0:
                print("Adios!")
            if opcion < 0 or opcion > 5:
                print("Opción inválida. Inténtalo de nuevo.")


    def menu_crear_habitat(self):
        nombre = input("Nombre: ")
        tempMax = input("Temperatura maxima: ")
        tempMin = input("Temperatura minima: ")

        habitat = habitatModel.(nombre, tempMax, tempMin)

    def crear_animal(self, zoo):
        tempMaxA = input("Temperatura maxima: ")
        tempMinA = input("Temperatura minima: ")

        if zoo.existeHabitatTemp():

            listaHabitatsDisp = listaHabitatsDisponibles(tempMaxA, tempMinA)
            print("Habitats disponibles para el animal")
            for elemento in listaHabitatsDisp:
                print(elemento)


           nombre = input("Nombre: ")
            especie = input("Especie: ")
            estadoDeSalud = input("Estado de Salud: ")
            especie = input("Especie: ")

        else:
