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



    def BMI_result(self):
        height_m = self.height / 100.0
        bmi = round(self.weight / (height_m * height_m),2)
        if bmi < 18.5:
            return f"Your BMI: {bmi}, Underweight"
        if 18.5 < bmi< 24.9:
            return f"Your BMI: {bmi}, Healthy Weight"
        if 25.0 < bmi < 29.9:
            return f"Your BMI: {bmi}, Overweight"
        else:
            return f"Your BMI: {bmi}, Obesity"

if __name__ == "__main__":
    temperature = Temperature(country="italy", city="rome").get()
    calorie = Calorie(weight=70, height=175, age=32, temperature=temperature)
    print(calorie.calculate())
    print(calorie.BMI_result())
