class Pet:
    MIN_STAT = 0
    MAX_STAT = 100

    def __init__(self, name, species):
        self._name = name
        self._species = species
        self._hunger = 50
        self._happiness = 50
        self._energy = 50

    @staticmethod
    def _clamp(value):
        if value < Pet.MIN_STAT:
            return Pet.MIN_STAT
        if value > Pet.MAX_STAT:
            return Pet.MAX_STAT
        return value
        
    def feed(self):
        self._hunger = self._clamp(self._hunger - 20)
        return f"{self._name} eat some food."
    
    def play(self):
        self._happiness = self._clamp(self._happiness + 15)
        self._energy = self._clamp(self._energy - 10)
        return f"{self._name} plays for awhile."
    
    def sleep(self):
        self._energy = self._clamp(self._energy + 30)
        return f"{self._name} takes a nap."
    
    def status(self):
        return(
            f"{self._name} the {self._species} | "
            f"Hunger: {self._hunger} | "
            f"Happiness: {self._happiness} | "
            f"Energy: {self._energy}"
        )
    
    def __str__(self):
        return f"{self._name} the {self._species}"