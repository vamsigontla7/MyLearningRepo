class Parent() :
    def __init__(self, lastname, eyecolor) :
        print("Constructor of Parent called")
        self.last_name = lastname
        self.eye_color = eyecolor
#billy_cyrus = Parent("Cyrus", "blue")
#print(billy_cyrus.last_name)

class Child(Parent) :
    def __init__(self, lastname, eyecolor, numberoftoys) :
        print("Child Initialized")
        Parent.__init__(self, lastname,eyecolor)
        self.number_of_toys = numberoftoys
miley_cyrus = Child("Cyrus", "Brown", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.eye_color)
print(miley_cyrus.number_of_toys)
