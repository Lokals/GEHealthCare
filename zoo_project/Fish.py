from Animal import Animal


class Fish(Animal):

    def sound(self):
        return "I am a {0}. And I am a {1}.".format(self.name, self.species)
