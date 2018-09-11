# This program creates a class with name Parrot and defines attributes. The attributes are the characteristics of an object
# object is a collection of data (variables) and methods (functions) that act on those data.
#Class is the blue print for the object. Think of class as a sketch (prototype) for the house. It contains all the details about the floor, doors, windows etc. based on these secriptions we build the house. House is the object.
#object can be called instance
#we can create many objects from a class
#The process of creating an object it called instantiation
#Function defintions begin with the word def
# defining a class, you begin with the word class
#docstring is the first string and it has a brief descripton of the class (recommended but not mandatory)
#class creates a new local namespace where all its attributes are defined.
#Attributes maybe data or functions
#

class Parrot:

	# class attribute
	species = "bird"

	# instance attribute
	def __init__(self, name, age):
		self.name = name
		self.age = age

# instantiate the parrot class. This means allocating memory for the new objects and calling the constructor (instatiation is the creation of an instance. An instance is a specific object from  a particular class). blu and woo are references (value) to our new object.
blu = Parrot("Blu", 10) #creates a new instance called blu
woo = Parrot("Woo", 15) #creates a new instance called woo

#access the class attributes. We access the class attributue using __class__.species. Class attributes are same for all instannces of a class.
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(blu.__class__.species))

#access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))


