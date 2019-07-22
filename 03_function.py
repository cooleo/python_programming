def fib(n):
    """ Print a Fibonacci series up to n . """
    a, b = 0, 1
    while a < n:
        print (a, end=' ')
        a, b = b, a +b
        print()


fib(200)


""" function with return value """
def fib2(n):
    """ Return a list containing the fibonacci series up to n """
    result = []
    a = 0
    b = 1
    while a < n: 
        result.append(a)
        a = b
        b = a + b
    return result


f100 = fib2(100)
print(f100)

""" Default Argument Value """

def ask_ok(promt, retries=4, reminder= 'Please try again!'):
    while True:
      ok = input(promt)
      if ok in ('y', 'ye', 'yes'):
        return True
      if ok in ('n', 'no', 'nope'):
        return False
    retries = retries - 1

    if retries < 0: 
        raise ValueError('invalid user response')
    
    print(reminder)

ask_ok('Do you really want to quit?')
ask_ok('Ok to overwrite the file?', 2)
ask_ok('Ok to overwirte the file?', 2, 'Come on, only yes or no!')


i = 5
def f(arg=i):
 print(arg)

i = 6
f()

""" The default value is evaluated only one, this make a difference when the default is a multable object such as a list, dictionary, or instances of most classes
"""
def f(a, L=[]):
    L.append(a)
    return L 

print(f(1))
print(f(2))
print(f(3))

""" if you dont' want the default to be shared between subsequent calls, you 
can write the function like this instead:"""

def (a, L=None)
 if L is None:
     L = []
 L.append(a)
 return L 

""" Keyword arguments """
""" 
 Functions can also be called using keyword arguments of form kwarg=value.
 For instance, the following function:
"""

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print(" -- This parot wouldn't", action, end='')
    print("if you put", voltage, "volts through it.")
    print("--- Lovely plumage, the", type)
    print("--It's ", state, "!")


parrot(1000) # 1 positional argument 
parrot(voltage=1000) # 1 keyword argument 
parrot(voltage=1000000, action='VOOOOOM') # 2 keyword arguments 
parrot(action='VOOOOOM', voltage=1000000) # 2 keyword arguments 
parrot('a million', 'bereft of life', 'jump') # 3 positional arguments 
parrot('a thousand', state='pushing up the daisies') # 1 positional, 1 keywor


"""
When a final formal parametter of form **name is present, it receives a dictionary contain all the keyword arguments except for those corresponging to 
a formal parameter

This maybe combined with a formal parameter of the form *name which receives a tuple contain the postional arguments byond 
the formal parameter list 

(*name must occur before **name)

"""
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any ", kind,  "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
     print(arg)
    for kw in keywords:
     print (kw, ":", keywords[kw])

cheeseshop(
    "Limburger", 
    "It's very runny, sir.", 
    "It's really very, VERY runny, sir.", 
    shopkeeper="Michael Palin", 
    client="John Cleese", 
    sketch="Cheese Shop Sketch")

