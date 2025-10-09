class Dog:
    def sit(self):
        print("Dog is sitting")
    
    def bark(self,a:int):
        print("Woof " * a)

dog1 = Dog()
dog1.sit()
dog1.bark(3)