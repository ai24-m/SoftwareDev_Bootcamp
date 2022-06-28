from animal import Animal
from animal import Giraffe
from animal import Camel
from animal import Tiger

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_giraffe(self, name):
        self.animals.append(Giraffe(name) )

    def add_camel(self, name):
        self.animals.append(Camel(name) )

    def add_tiger(self, name):
        self.animals.append(Tiger(name) )

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("John's Zoo")
zoo1.add_giraffe("Nala")
zoo1.add_giraffe("Kiva")

zoo1.add_camel("Rajah")
zoo1.add_camel("Rajah")

zoo1.add_tiger("Simpa")
zoo1.add_tiger("Joh")

zoo1.print_all_info()