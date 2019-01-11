
"""
x=5
print(type(x))
"""

"""
x="5"
y=3
print(int(x)+y)
"""

"""
x="5"
y=3
print(x+str(y))
"""

"""
x="Hello,World"
print(x[5:])
"""

"""
x="   helllo  world    "#removes white spaces 
print(x.strip())
"""

"""
x="Hello World"
print(len(x))#Length of the string
"""

"""
x="HELLO WORLD"
print(x.lower())
"""

"""
x="hello world"
print(x.upper())
"""

"""
x="Hello world"
print(x.replace("H","j"))
"""

"""
x="Hello World"
y=x.split(" ")
print(y)
"""

"""
print("Enter the input")
x=input()
print("the Number is "+ x)
"""

"""
x=5
print(bin(x))
"""

"""
x=5
y=3
print(bin(x&y))
"""

"""
x=5
y=3
print(bin(x|y))
"""

"""
x=5
print(~x) #(-x-1)
"""

"""
x=5
y=3
print(bin(x^y))
"""

"""
x=5
print(bin(x<<2))
print(bin(x>>2))
"""

"""
#Boolean
x=5
y=3
print(not(x>y))
"""

"""
x=5
print(x>2 and x>3)
print(x>2 or x>3)
"""

"""
x=["Apple","Banana"]
y=["Apple","Banana"]
z=x
print(x is y) #Not same object
print(z is x)#Same Object
"""

"""
x=["Apple","Banana"]
y="Apple"
print(y in x)
"""


#list
"""
thislist=["a","b","c"]
print(thislist)#a,b,c
print(thislist[1])#b
thislist.insert(1,"d")#a,d,b,c
print(thislist)
thislist.remove(thislist[1])
print(thislist)#a,b,c
thislist.remove("a")
print(thislist)#b,c
thislist.append("a")
print(thislist)#b,c,a
thislist1 = thislist.copy()
print(thislist1)#b,c,a
print(thislist.count("a"))#1
thislist.pop()
print(thislist)#b,c
thislist.reverse()
print(thislist)#c,b
thislist.sort()
print(thislist)#b,c
print(thislist.index("b"))#0
thislist.extend(thislist1)
print(thislist)#b,c,b,c,a
del thislist[1:]
print(thislist)#b
thislist.clear()
print(thislist)
"""


#tuple
"""
a=("apple","Banana","Cherry")
print(len(a))#3
print(a.count("apple"))#1
print(a.index("Banana"))#1
del(a)
print(a)#not defined
"""

"""
#set
a={"a","b","c","d"}
a.add("e")
print(a)#c,b,d,e,a
b={"a","c","d"}
c=a.difference(b)
print(c)#e,b
print(a)#a,b,c,d
a.difference_update(b)
print(a)#e,b
a.discard("e")
print(a) #b
a.add("a")
print(a)#a,b
a.intersection_update(b)
print(a)#a
print(a.isdisjoint(b))#a,b, have intersection or not
print(a.issubset(b))#every element in a is in b
print(b.issuperset(a))#b has every element in a
b.remove("a")
print(b)#d,c
a.add("c")#a,c

a.symmetric_difference_update(b)#a,d elements except intersection
print(a)#a,d
c=a.union(b)
print(c)#a,c,d
a.update(b)
print(a)#a,c,d
"""

#DICT
"""
thisdict= {
	"Brand" : "Tata",
	"Model" : "Manza",
	"Year"  : "2007"
}
print(thisdict["Model"])#Manza
print(thisdict.get("Model"))#Manza
thisdict["Brand"] = "Maruti"
print(thisdict["Brand"])#Maruti
for x in thisdict.values():
	print (x)#Maruti,Manza,2007
for x,y in thisdict.items():
	print(x,y)
thisdict.pop("Model")
print(thisdict)
thisdict.popitem()
print(thisdict)
x=("Keys1","Keys2")
y=0
thisdict=dict.fromkeys(x,y)
print (thisdict)
"""

"""
#if
x=5;
y=6;
print(x) if x>y else print(y) if y>x else print("o")
if(x>y):
	print(x)
elif(y>x):
	print(y)
else:
	print("Equal")
"""

"""
#for
x=("Manza","breeze","Ford")
y=("hii","Hello","Hey")
for i in x:
	print (i)#Manza,Breeze,ford

for i in x:
	for j in y:
		print (i,j)


for i in range(6):
	print (i)#0,1,2,3,4,5

for i in range(2,5):
	print(i)#2,3,4
for i in range(2,10,2 ):
	print(i) #2,4,6,8
"""

"""
#functions
def my_function():
	print("This is the function")

my_function()

def function(x,y):
	return x+y

print("" +str(function(2,3)))#5

def function2(std= "Seven"):
	return std

print(function2("Hii"))#Hii
print(function2())#Seven
"""

"""
#Array
cars = ["Tata","Ford","Toyoto"]
print(cars[0])#tata
cars.pop()
print(cars)#tata,ford
cars.append("Maruti")
print(cars)#tata,ford,maruti
print(cars.index("Tata"))#0
print(cars.count("Tata"))
cars.reverse()
print(cars)#maruti,ford,tata
cars.sort()
print(cars)#ford,maruti,tata
"""

#Classes,Objects
"""
class myclass:
	def __init__(self,x):
		self.x=x

	def function(self):
		print(self.x)

obj1 = myclass(2)
obj1.function()#2





class cls:
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def function1(self):
		print((self.x+self.y))#3

obj2 = cls(2,1)
obj2.function1()
"""

"""
class cls:
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def function(self):
		print("The Name is " +self.x+" and his age is "+ str(self.y))#john,19

myobj=cls("John",19)
myobj.function()
"""

#iter
"""
class cls:
	def __iter__(self):
		self.x=1
		return self

	def __next__(self):
		while(self.x<20):
			y=self.x
			self.x+=1
			return y
		else:
			raise StopIteration

myobj = cls()
myiter=iter(myobj)

for x in myiter:
	print (x)
"""


#Module
"""
import platform
x=platform.system()
print(x)
"""

"""
#date
import datetime

x=datetime.datetime.now()#Today date
print(x)
print(x.year)
print(x.strftime("%A"))
y=datetime.datetime(2020,5,17)
print(y)
"""


#json
"""
import json
arr = ["Name","age"]
x=json.dumps(arr)
print(x)
arr1=json.loads(x)
print(arr1)
y=None
z=json.dumps(y)
print(z)#null
"""

"""
import json
arr={
	"Name" :"Agas",
	"Age" : 15,
	"cars" : [
		{"Model" : "BMW",
		"Year"  : 2019},
		{"Model":"Tata",
		"Year":2018}
		]
}
x=json.dumps(arr)
print(x)
x=json.dumps(arr,indent=4)
print(x)
x=json.dumps(arr,indent=4,sort_keys=True)
print(x)
"""

