from pet import Pet

class Fish(Pet):

    def __init__(self, name):
        super().__init__(name, "Fish")

    def feed(self):
        self._hunger = self._clamp(self._hunger - 10)
        return f"{self._name} eats a few flakes."
    
    def play(self):
        self._happiness = self._clamp(self._happiness + 8)
        self._energy = self._clamp(self._energy - 3)
        return f"{self._name} swims around its bowl."
    
    def sleep(self):
        self._energy = self._clamp(self._energy + 15)
        return f"{self._name} drifts quietly in the water."