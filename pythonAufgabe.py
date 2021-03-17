class Hund:
    def __init__(self,name):
        self.name = name

    @staticmethod
    def makeSound():
        print("Wouuf")

    @staticmethod
    def makeSound2(sound):
        print(sound)

hund1 = Hund("Rex")

print(hund1.name)
Hund.makeSound()
Hund.makeSound2("Test")