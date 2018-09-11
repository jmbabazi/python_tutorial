#As soon as you define a class, a new class object is created with the same name. This class object allows us to access the different attributes as well as to instantiate new objects of that class.
#__doc__ gives docstring of that class. Specials attributes in it that begin double underscores (__)
class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print ('Hello')

print(MyClass.a)

print(MyClass.func)

print(MyClass.__doc__)
