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
            print("3. Agregar animal a un habitat")
            print("4. Lista de habitats y animales")
            print("5. Modificar informacion de animal")
            print("6. Visitar habitat")
            print("0. Salir")
            opcion = int(input("Escoge una opcion: "))

            controlador = zooController.zooController(zoo, self)
            controlador.menu_principal(self, opcion, zoo)

            if opcion == 0:
                print("Adios!")
            if opcion < 0 or opcion > 6:
                print("Opción inválida. Inténtalo de nuevo.")


    def menu_crear_habitat(self):
        nombre = input("Nombre: ")
        tempMax = input("Temperatura maxima: ")
        tempMin = input("Temperatura minima: ")

        habitat = habitatModel.(nombre, tempMax, tempMin)

    def crear_animal(self, zoo):
        listaDatos = []
        juguetes_temp = []

        ##ingresa nombre
        listaDatos.append(input("Ingrese el nombre del animal:"))

        ##Ingresa especie
        listaDatos.append(input("Ingrese la especie del animal:"))

        ##Ingresa estado de salud
        listaDatos.append(input("Ingrese el estado de salud del animal:"))

        listaDatos.append(zoo.cantAnimales)
        zoo.cantAnimales += 1

        while True:
            try:
                print("Ingrese la edad del animal:")
                edad = int(input())
                if edad <= 0 or edad > 100:
                    raise ValueError("La edad debe ser un entero positivo menor o igual a 100")
                break
            except ValueError:
                print("Se ingresó un argumento inválido. Por favor ingrese un número entero.")

            listaDatos.append(input(edad))

        tempMaxA = input("Ingrese la temperatura minima: ")
        listaDatos.append(input(tempMaxA))

        while True:
            try:
                print("Ingrese la temperatura maxima del animal: ")
                tempMinA = int(input())
                if tempMinA < tempMaxA:
                    raise ValueError("La temperatura maxima es menor que la temperatura minima")
                break
            except ValueError:
                print("Se ingresó un argumento inválido. Por favor ingrese un numero menor a la temperatura maxima.")

        listaDatos.append(tempMinA)

        while True:
            try:
                print("Ingrese las horas de sueño del animal:")
                cant_max_dormir = int(input())
                if cant_max_dormir <= 0:
                    raise ValueError("La cantidad de horas de sueño debe ser un entero positivo")
                break
            except ValueError:
                print("Se ingresó un argumento inválido. Por favor ingrese un número entero.")

            listaDatos.append(cant_max_dormir)

        while True:
            try:
                print("Ingrese el número de juguetes que va a tener el animal:")
                cant_juguetes = int(input())
                if cant_juguetes <= 0:
                    raise ValueError("La cantidad de juguetes debe ser un entero positivo")
                break
            except ValueError:
                print("Se ingresó un argumento inválido. Por favor ingrese un número entero.")

        for i in range(cant_juguetes):
            print(f"Ingrese el nombre del juguete {i + 1}:")
            juguete_nom = input().lower()
            juguetes_temp.append(juguete_nom)

        listaDatos.append(juguetes_temp)

        while True:
            print("\nTipo de dieta disponible:")
            print("\n - Carnivoro \n - Herbivoro \n - Omnivoro")
            print("Ingrese el tipo de alimentación del animal:")
            alimentacion = input().lower()
            if zoo.lista_dietas_disponibles(alimentacion):
                break
            else:
                print("La dieta ingresada no está disponible. Por favor ingrese una dieta válida.")

        listaDatos.append(alimentacion)


        #nuevo_animal = Animal(nombre_temp, especie, estado_salud, id_animal_nuevo, temp_max_a, temp_min_a, 0,
        #                      cant_max_dormir, False, False, edad, juguetes_temp, alimentacion)


        # Agrega los alimentos que van por defecto
        #nuevo_animal.elegir_alim(alimentacion)

        return listaDatos

        self.animales[id_animal_nuevo] = nuevo_animal
        print(f"{nuevo_animal.get_nombre()} fue llevado a su nueva hábitat {self.get_nombre()}")


#############

    def crear_animal(self, zoo):
        tempMaxA = input("Temperatura maxima: ")
        tempMinA = input("Temperatura mia: ")

        if zoo.existeHabitatTemp():

            listaHabitatsDisp = listaHabitatsDisponibles(tempMaxA, tempMinA)
            print("Habitats disponibles para el animal")
            for elemento in listaHabitatsDisp:
                print(elemento)
            habitat = input("Seleccione un habitat: ")
            print()


    nombre = input("Nombre: ")
    especie = input("Especie: ")
    estadoDeSalud = input("Estado de Salud: ")
    especie = input("Especie: ")

    else:

#######################

    def mostrar_mensaje_exitoso(self, mensaje):
        st.success(mensaje)

    def mostrar_mensaje_error(self, mensaje):
        st.error(mensaje)
