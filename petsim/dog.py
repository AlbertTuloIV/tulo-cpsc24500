from pet import Pet

class Dog(Pet):

    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self._breed = breed
    
    def feed(self):
        self._hunger = self._clamp(self._hunger - 30)
        return f"{self._name} the {self._breed} wolfs down the food."
    
    def play(self):
        self._happiness = self._clamp(self._happiness + 25)
        self._energy = self._clamp(self._energy - 20)
        return f"{self._name} runs around wagging its tail!"
    
    def fetch(self):
        self._happiness = self._clamp(self._happiness + 10)
        self._energy = self._clamp(self._energy - 20)
        return f"{self._name} fetches the ball and brings it back."
    
    def status(self):
        base = super().status()
        return f"{base} | Breed: {self._breed}"