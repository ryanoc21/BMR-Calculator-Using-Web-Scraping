"""
Represent the amount of calories required to eat daily.
BMR = 10*weight + 6.25*height -5*age + 5 -10*temperature
"""


class Calorie:

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        bmr = 10 * self.weight \
              + 6.25 * self.height \
              - 5 * self.age \
              + 5 - 10 * self.temperature

        return bmr
