class Calorie:
    """Represent amount of calsries with
    BMR = 10*weigth + 6.25*height - 5*age -10*temperature +5"""

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        pass