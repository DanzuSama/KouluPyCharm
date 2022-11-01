class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.printData()

    def printData(self):
        print(self.brand, self.model, str(self.year))


skoda = Car('Skoda', 'Fabia', 2000)
car = Car('Skoda1', 'Fabia1', 2001)
