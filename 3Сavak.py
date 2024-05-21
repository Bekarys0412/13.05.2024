class Animal:
    def say_hello(self):
        for i in range(0, 4):
          print("Hello")



class Hello_cat(Animal):
    def say_hello(self, count):
        for i in range(0, count):
           print("may")




class Hello_dog(Animal):
    def say_hello(self, count):
        for i in range(0, count):
            print("gaf")
     
        
cat = Hello_cat()
dog = Hello_dog()
cat.say_hello(count=2) 
dog.say_hello(count=3)