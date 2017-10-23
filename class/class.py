class person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def showInfo(self):
        print "Name and surname: " +self.name + " " +self.surname
   

information = person("Mutellip", "ikbal")
print (information.name)

#or

information.showInfo()
