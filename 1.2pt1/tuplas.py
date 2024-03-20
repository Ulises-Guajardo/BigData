t = () # empty tuple
type(t)
class tuple:
    one_element_tuple = (42, ) # you need the comma!
    three_elements_tuple = (1, 3, 5) # braces are optional here



#---------------------------------------------------------------------------------------------------
    a, b, c = 1, 2, 3 # tuple for multiple assignment
    
    print(a, b, c) # implicit tuple to print with one instruction
    
    3 in three_elements_tuple # membership test
    True


#-------------------------------------------------------------------------------------------------------
a, b = 1, 2
c = a # we need three lines and a temporary var c
a = b
b = c
print(a, b) # a and b have been swapped

    
#Now let's see how we would do it in Python:
x, y = 0, 1
x, y = y, x # this is the Pythonic way to do it
print(x,y)
    