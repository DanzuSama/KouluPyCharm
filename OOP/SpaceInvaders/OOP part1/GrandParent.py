class GrandParent:
    def __init__(self):
        print("GrandParend init called")

    def famaly_saying(self):
        print("We are Irish")

class Parent(GrandParent):
    def __init__(self):
        print("Parend init called")


ola = Parent()
ola.famaly_saying()
