import random

class Junk:
    def __init__(self, name, value, weight) -> None:
        self.name = name

        if isinstance(value, list):
            self.value = random.randint(value[0], value[1])
        else:
            self.value = value

        self.weight = weight

    def __str__(self) -> str:
        if(len(self.name) >10):
            return f"Scrap: {self.name} - \t${self.value}\t - \t{self.weight}Kg"
        else:
            return f"Scrap: {self.name}\t - \t${self.value}\t - \t{self.weight}Kg"