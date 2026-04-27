from pet import Pet

class Cat(Pet):

    def __init__(self, name):
        super().__init__(name, "Cat")

    def feed(self):
        self._hunger = self._clamp(self._hunger - 15)
        self._happiness = self._clamp(self._happiness + 5)
        return f"{self._name} nibbles delicately at the food."
    
    def play(self):
        self._happiness = self._clamp(self._happiness + 20)
        self._energy = self._clamp(self._energy - 5)
        return f"{self._name} chases a toy mouse."
    
    def purr(self):
        return f"{self._name} purrs softly."