
def add(*args):
    return sum(args)
print(add(2,4,5))

'''
[ *args ] keyword simply means more than one argument/parameter is to be passed into a function
This is done because the python syntax has strict rules for amount of arguments passed into a function
Thus this specified the amount
'''

def calculate(**kwargs):
    for key,value in kwargs.items():
        print(value)
    print(kwargs["add"])

calculate(add = 3 , multiply = 5)

'''
[ *k-w-args ] keyword also simply means more arguments but in this case,can be passed in a form of dictionary
with key and value identities.  
'''