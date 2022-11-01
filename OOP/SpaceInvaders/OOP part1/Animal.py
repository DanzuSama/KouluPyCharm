import turtle



class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def printMyName(self):
        print('My name: ' + self.name + str(self.age) + self.color)

class Dog(Animal):
    pass

tiger = Animal('Bob', 5 , 'gru')
tiger.printMyName()


turtle.forward(200)
turtle.end_fill()
turtle.done()