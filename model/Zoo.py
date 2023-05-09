

class Zoo:
    def __init__(self):
        self.nombre = "ZooMAVA"
        self.cantAnimales = 0
        self.zooNoVacio = False
        self.habitats = {}
        self.registroAn = {}
        self.dietaCarnivora = []
        self.dietaHerbivora = []

    def existeHabitatTemp(self, temMax, temMin):
        for habitat in self.habitats:
            if habitat.getTempMax() <= temMax and habitat.getTempMin() >= temMin:
                return True
        return False

    def registrarHabitat(self, nombre, tMin, tMax):
        if self.habitatRepetido(nombre):
            print("Este habitat ya existe")
        else:
            pHabitat = Habitat(nombre, tMin, tMax)
            self.habitats.append(pHabitat)
            self.setZooVacio(True)

    def listaHabitatsDisponibles(self, temMax, temMin):
        habitatsAnimal = []
        for habitat in self.habitats:
            if habitat.getTempMax() <= temMax and habitat.getTempMin() >= temMin:
                habitatsAnimal.append(habitat.getNombre())
        return habitatsAnimal