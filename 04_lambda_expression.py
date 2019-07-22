
"""
Small anonymous fucntions can be created with lambda keyword.
This function return the sum of it's two arguments:
lambda a, b: a + b

Lambda functions can be used wherever function objects are required.
They are synatcically restricted to a single expression.
Semantically, they are just syntactic sugar for a normal function defintion.
Like nested function defintions, lambda functions can refrence variables from containing scope:

"""
def make_incrementor(n):
     return lambda x: x + n

f = make_incrementor(42)
print(f(1)) # 43



"""
The above example uses lambda expression to return a function. Another use is to pass a small function as an argument:
"""

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

pairs.sort(key=lambda pair: pair[1])

print(pairs)

