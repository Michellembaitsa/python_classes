class Student: #class name starts with cap, if more,camelcap..e.g AkiraChix,no spaces
    school="Akirachix" #this is an attribute shared
    def __init__(self,name,age): #a constructor...params always start arguments with small letters self reps the object you created in the class
        self.name=name
        self.age=age     #in terminal answer params as name="Mich",age=25...
    def speak(self): #this is a method..ie behaviors
            return f"Hello my name is {self.name} and I am {self.age} years old and I love {self.school}"


#save class codes in modules .py
# to import a class from a module, use dot notation, import class name
#modules in a directory form a package
#python is an interprated language.. that is, it is interprated in real time.

# create 3 modules...car,dog,bank object & class, attributes,behaviormethods