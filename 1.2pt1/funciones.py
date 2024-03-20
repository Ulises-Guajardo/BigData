def outer():
    test = 1 # outer scope
    def inner():
        test = 2 # inner scope
        print('inner:', test)
    inner()
    print('outer:', test)

test = 0 # global scope
outer()
print('global:', test)


print("------------------------------------------------------")

def func(a, b, c):
    print(a, b, c)

func(42, b=1, c=2)


print("------------------------------------------------------")
def func(a, b, /, c):
    print(a, b, c)
func(1, 2, 3) # prints: 1 2 3
func(1, 2, c=3)