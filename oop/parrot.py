# This program creates a class with name Parrot and defines attributes. The attributes are the characteristics of an object
class Parrot:

	# class attribute
	species = "bird"

	# instance attribute
	def __init__(self, name, age):
		self.name = name
		self.age = age

# instantiate the parrot class. This means allocating memory for the new objects and calling the constructor (instatiation is the creation of an instance. An instance is a specific object from  a particular class). blu and woo are references (value) to our new object.
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

#access the class attributes. We access the class attributue using __class__.species. Class attributes are same for all instannces of a class.
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(blu.__class__.species))

#access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))


