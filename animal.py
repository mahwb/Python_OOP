class animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "Health of", self.name, "is", self.health
        return self

penguin = animal("Flappy", 150).walk().walk().walk().run().run().displayHealth()

class dog(animal):
    def __init__(self, name):
        super(dog, self).__init__(name, 150)

    def pet(self):
        self.health -= 5
        return self

dog = dog("Fido").walk().walk().walk().run().run().pet().displayHealth()

class dragon(animal):
    def __init__(self, name):
        super(dragon, self).__init__(name, 170)
    
    def fly(self):
        self.health -= 10
        return self
    
    def displayHealth(self):
        print "I am a dragon"
        super(dragon, self).displayHealth()
        return self

dragon = dragon("Smog").displayHealth()
# animalpet = animal("Can't pet", 140).pet()
# no attribute pet
# animalfly = animal("Can't fly", 140).fly()
# no attribute fly
notDragon = animal("Not Dragon", 140).displayHealth()
# does not display I am dragon