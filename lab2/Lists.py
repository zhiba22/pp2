# 4-built in data types in Python 

thislist = ["apple", "banana", "cherry"] #List
print(thislist)

''' LIST ITEMS 
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.'''

print(len(thislist)) #len() method
list1 = ["abc", 34, True, 40, "male"] #allows different data types
#<class 'list'> - From Python's perspective, lists are defined as objects with the data type 'list'
thislist = list(("apple", "banana", "cherry")) #list() constructor to make a list

mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2]) #banana
print(len(mylist)) #4

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #['cherry', 'orange', 'kiwi']
print(thislist[:4]) #["apple", "banana", "cherry", "orange"]
print(thislist[2:]) #"cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #["orange", "kiwi", "melon"]

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) #["apple", "blackcurrant", "watermelon", "orange", "kiwi", "mango"]

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #["apple", "blackcurrant", "watermelon", "cherry"]

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #["apple", "watermelon"]

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.insert(2, "watermelon")
thislist.append("orange")
thislist.extend(tropical)
print(thislist) #["apple", "banana", "watermelon", "cherry"]
print(thislist) #["apple", "banana", "watermelon", "cherry", "orange"]
print(thislist) #["apple", "banana", "watermelon", "cherry", "orange", "mango", "pineapple", papaya""]

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #removes only specified item
thislist.pop(1)
thislist.pop() #removes the last element
del thislist[0]
del thislist #completely deletes
thislist.clear() #just no items in list

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
