from math import prod
from operator import itemgetter

[] # empty list

list() # same as []

[1, 2, 3] # as with tuples, items are comma separated
print([1, 2, 3])

[x + 5 for x in [2, 3, 4]] # Python is magic

list((1, 3, 5, 7, 9)) # list from a tuple
print(list((1, 3, 5, 7, 9)))
list('hello') # list from a string
print(list('hello'))

print("------------------------------------------------------------------")
#------------------------------------------------------------------------------------------
a= [1, 2, 1, 3]
a.append(13) # we can append anything at the end
print(a) 
[1, 2, 1, 3, 13]
a.count(1) # how many `1s` are there in the list?
print(a.count(1)) 
a.extend([5, 7]) # extend the
print(a) 

a.index(13) # position of `13` in the list (0-based indexing)
print(a.index(13)) 
a.insert(0, 17) # insert `17` at position 0
print(a) 

a.pop() # pop (remove and return) last element
print(a) 
a.pop(3) # pop element at position 3
print(a) 

a.remove(17) # remove `17` from the list
print(a) 

a.reverse() # reverse the order of the elements in the list
print(a) 

a.sort() # sort the list
print(a) 

a.clear() # remove all elements from the list
print(a) 
print("------------------------------------------------------------------")

a = list('hello') # makes a list from a string
print(a)
a.append(100) # append 100, heterogeneous type
print(a)

a.extend((1, 2, 3)) # extend using tuple
print(a)

a.extend('...') # extend using string
print(a)
print("------------------------------------------------------------------")
a = [1, 3, 5, 7]
print(a)
min(a) # minimum value in the list
print(min(a))
max(a) # maximum value in the list
print(max(a))
sum(a) # sum of all values in the list
print(sum(a))
prod(a) # product of all values in the list
print(prod(a))
len(a) # number of elements in the list
print(len(a))
b = [6, 7, 8]
c=a + b # `+` with list means concatenation
print(c)
a * 2 # `*` has also a special meaning
print(a)
print("------------------------------------------------------------------")

a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
sorted(a)
print(a)
sorted(a, key=itemgetter(0))
print(sorted(a, key=itemgetter(0)))
sorted(a, key=itemgetter(0, 1))
print(sorted(a, key=itemgetter(0, 1)))
sorted(a, key=itemgetter(1))
print(sorted(a, key=itemgetter(1)))
sorted(a, key=itemgetter(1), reverse=True)
print(sorted(a, key=itemgetter(1), reverse=True))