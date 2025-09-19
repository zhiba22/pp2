# x = "John" / x='John' are the same
# a = 5 / A = 5 are not the same


#if 5 > 2 
    #print("Yes")

"""
x = y = z = "Hello worlD"
x, y, z = "Orange", "Banana", "Cherry"
"""
'''
my-var = 20 is not legal
my_var = 20 / Myvar = 20 / _myvar = 20 are legal to use 
'''
fruits = ['apple', 'banana', 'cherry']
a , b, c =fruits
print(a)#result will be apple

a = "Hello"
b = "World"
print (a+b) # HelloWorld

a = 4
b = 5
print(a+b) #9

x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x) #Python is awesome

x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x) #Python is fantastic

'''
print(type())
int for integers 1,2,3
str for strings "ghjkr,f"
list for ["aefea", "wefge", "asdgfer"]
tuple ("wpoiu", "waefvf", "ajiolk")
dictionary x = {"name" : "John", "age" : 36}
bool x = True
'''

print(int(35.88)) #35
print(float(35)) #35.0
print(str(35.88)) #35.88

x = 'Welcome'
print(x[3]) #c

x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]

txt = 'The best things in life are free!'
if 'free' in txt:
  print('Yes, free is present in the text.')