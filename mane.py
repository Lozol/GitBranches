def mane_function():
    number =42
    string = 'hello'

    print(locals())

    print(globals())

def test_function(arg):
    if arg is number:
	print(arg)
    else:
        print("ўось не те")


mane_function()
test_function('xa-xa')
# Task1
a = 3/2
print (a==1,5)

# Task2
one = '1'.isalpha()
print(one.real)

# Task3
lst = [1 for i in [1,2,3]]
print(3 in lst)