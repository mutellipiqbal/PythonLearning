class Animal():
    def __init__(self, name, color):
        self.name = name
        self.color = color


    def food(self):
        print "All animal eate eachother."

    def voice(self):
        print "Do you like animal voice?"

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, "My dog", "brown")

    def DogVoice(self):
        print "I dont like dog's barking."

x = Dog()
x.voice()
x.DogVoice()

        
    


    
        
