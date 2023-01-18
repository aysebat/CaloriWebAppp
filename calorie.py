from temperature import Temperature
class Calorie:
    """Represent amount of calsries with
    BMR = 10*weigth + 6.25*height - 5*age -10*temperature +5"""

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.25 * self.height - 5 * self.age - 10 * self.temperature + 5
        return result


if __name__ == "__main__":
    temperature = Temperature(country="italy", city="rome").get()
    calorie = Calorie(weight=70, height=175, age=32, temperature=temperature)
    print(calorie.calculate())
