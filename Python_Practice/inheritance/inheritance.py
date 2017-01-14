class Parent() :
    def __init__(self, lastname, eyecolor) :
        print("Parent Constructor called")
        self.last_name = lastname
        self.eye_color = eyecolor
    def show_info(self) :
        print("LastName ::: "+self.last_name)
        print("Eye Color ::: "+self.eye_color)

class Child(Parent) :
    def __init__(self, lastname, eyecolor, numberoftoys) :
        print("Child Constructor Called")
        Parent.__init__(self, lastname,eyecolor)
        self.number_of_toys = numberoftoys
    def show_info(self) :
        print("LastName ::: "+self.last_name)
        print("Eye Color ::: "+self.eye_color)
        print("Number of Toys ::: "+str(self.number_of_toys))

billy_cyrus = Parent("Cyrus", "blue")
#billy_cyrus.show_info()
miley_cyrus = Child("Cyrus", "brown", 6)
miley_cyrus.show_info()
