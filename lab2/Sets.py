#UNORDERED, UNINDEXED, NO DUPLICATES
set1 = {"apple", "banana", "cherry"}

#False and 0 
#True and 1 ARE CONSIDERED AS TEH SAME VALUES

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#REMOVING 
thisset.remove("banana") #will raise an error
thisset.discard("banana") # will not raise an error
thisset.pop() #will delete a random element
thisset.clear()
del thisset

''' The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates. '''

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))