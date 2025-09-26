''' BOOLEAN VALUES
When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10 > 9)
print(10 == 9)
print(10 < 9)'''
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

''' EVALUATE VALUES AND VARIABLES
The bool() function allows you to evaluate any value, and give you True or False in return'''
print(bool("Hello")) #True
print(bool(15)) #True

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

''' MOST VALUES ARE TRUE
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.'''
bool("abc") #True
bool(123) #True
bool(["apple", "cherry", "banana"]) #True

''' SOME VALUES ARE FALSE
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", 
the number 0, and the value None. And of course the value False evaluates to False.'''
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

'''
One more value, or object in this case, evaluates to False, 
and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:'''
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #False

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") #YES

'''
Check if an object is an integer or not:'''
x = 200
print(isinstance(x, int))