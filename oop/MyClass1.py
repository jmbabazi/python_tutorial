#class object can be used to access different attributes
#class object can also be used to create new instances (instantiation) of that class. The procedure to create an object is similar to a function call
# >>> ob = MyClass() This will create a new instance object called ob. We can access attributes of objects using the object name prefix.

#This will create a new instance object named ob. We can access attributes of objects using the object name prefix.
#Attributes may be data or method. Method of an object are corresponding functions of that class. Any function object that is a class attribute defines a method for objects of that class.
#This means to say, since MyClass.func is a function object (attribute of class), ob.func will be a method object.

class MyClass1:
	'''This is my second class'''

	a = 10
	def func(self):
		print('Hello')

# create a new MyClassOne
ob = MyClass1()

print(MyClass1.func)

print(ob.func)

ob.func()

MyClass1.func(ob)

##Output
# <function MyClass1.func at 0x7f710c21d598>
# <bound method MyClass1.func of <__main__.MyClass1 object at 0x7f710d7e6860>>
# Hello
# Hello
