def mane_function():
    number =42
    string = 'hello'

    print(locals())

    print(globals())

# test_function не можу створити бо ругається Anaconda Prompt. Please open Anaconda prompt, and run `conda init powershell` there.
def _function(some):
    if some==5:
        print("Yes")
    else:
        print("It is not good")


mane_function()
_function(5)
# Task1
a = 3/2
print (a==1,5)

# Task2
one = '1'.isalpha()
print(one.real)

# Task3
lst = [1 for i in [1,2,3]]
print(3 in lst)

# Task5
lst1=[1,2,3]*-1
lst1*=2
print(lst1)