def mane_function():
    number =42
    string = 'hello'

    print(locals())

    print(globals())
    print('some code adding')
    return number*2

mane_function()
my_test = mane_function()
print(my_test)

mane_function()
# Task1
a = 3/2
print (a==1,5)

# Task2
one = '1'.isalpha()
print(one.real)

# Task3
lst = [1 for i in [1,2,3]]
print(3 in lst)

# Task4
def func(num):
    return num+15

func(5)
print(num)
