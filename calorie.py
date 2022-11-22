class Calorie:

    def __init__(self, weight, height, age, gender, temperature):
        self.weight = float(weight)
        self.height = float(height)
        self.age = float(age)
        self.gender = gender
        self.temperature = float(temperature)

    def calculate(self):

        weight_in_kg = self.weight * 0.45359237
        height_in_centimeters = self.height * 2.54

        if self.gender == "Male":
            bmr = 88.362 + (13.397 * weight_in_kg) + (4.799 * height_in_centimeters) - (5.677 * self.age)
        elif self.gender == "Female":
            bmr = 447.593 + (9.247 * weight_in_kg) + (3.098 * height_in_centimeters) - (4.330 * self.age)
        else:
            return 0

        bmr = round(bmr, 0)

        return bmr

