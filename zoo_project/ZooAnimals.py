from Mammal import Mammal
from Walker import Walker
from Fish import Fish
from Swimmer import Swimmer


class Mouse(Mammal, Walker):
    pass


class Whale(Mammal, Swimmer):
    pass


class Catfish(Fish, Swimmer):
    pass


class Otter(Mammal, Walker, Swimmer):
    pass


# if __name__ == '__main__':
#     mouse = Mouse("Mouse", "Mammal")
#     print(mouse.sound())
#     print(mouse.walk())
#
#     whale = Whale("Whale", "Mammal")
#     print(whale.sound())
#     print(whale.swim())
#
#     catfish = Catfish("Catfish", "Fish")
#     print(catfish.sound())
#     print(catfish.swim())
#
#     otter = Otter("Otter", "Mammal")
#     print(otter.sound())
#     print(otter.walk())
#     print(otter.swim())
