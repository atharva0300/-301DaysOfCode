from collections import deque
from math import pi , sqrt


def if_case():
    x = int(input("Eneter an integer :  "))
    if x<0:
        print("Number is negative")
    elif x==0:
        print("Numebr is 0")
    else : 
        print("Number is positive ")

def for1():
    words = ['car' , 'window' , 'defenestrate']
    for i in words:
        print(i , len(i))

def for2():
    for i in range(5):
        print(i)

def for3():
    print(list(range(5,10)))
    print(list(range(0, 10,3)))
    print(list(range(-10,-100 , -30)))

def for4():
    a = ['Mary' , 'had' , 'a' , 'little' , 'lamb']
    for i in range(len(a)):
        print(i , a[i])
    print(range(0,10))
    print(sum(range(0,10)))

def for5():
    for n in range(2,10):
        for x in range(2,n):
            if n%x==0:
                print(n , 'equals' , x , '*' , n//x)
                break
        else :
            print(n , 'is  a prime number')
def for6():
    for num in range(2,10):
        if num%2==0:
            print("Even number : " , num)
        else :
            print("Odd number : " , num)

def for7():
    pass

def fib(n):
    a,b = 0,1
    while a<n:
        print(a)
        a,b = b , a+b

def fib2(n):
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b = b,a+b
    return result 

def ask_ok(prompt , retries=4 , message = 'Please try again'):
    while True : 
        ok = input(prompt)
        if ok in ('y' ,'ye' , 'yes'):
            return True 
        if ok in ('no' , 'nope' , 'n'):
            return False 
        retries = retries -1 
        if retries <0:
            raise ValueError('invalid user response ')
        print(message)
    
xyz=5
def for8(arg=xyz):
    print(arg)
    
def for9(a , l=[]):
    l.append(a)
    return l

def for10(a , l=None):
    if l is None:
        l = []
    l.append(a)
    return l

def for11(voltage , state = 'a stiff' , action = 'voom' , type = 'Norweigna Blue'):
    print("-- This parrot wouldn't " , action , end=" " )
    print("If you put " , voltage , "volts through it")
    print("-- Lovely plumage , the " , type )
    print("-- It's " , state , " !")

def for12(a):
    pass

def for13(kind , *arguments , **keywords):
    print("-- Do you have any " , kind , " ? ")
    print("-- I'm sorry , we're all out of " , kind )
    for arg in arguments:
        print(arg)
    print("-"*40)
    for kw in keywords:
        print(kw , " : " , keywords[kw])

def for14(arg):
    print(arg)

def for15(arg , /):
    print(arg)

def for16(* , arg):
    print(arg)

def for17(pos_only , / , standard , * , kwd_only):
    print(pos_only , standard , kwd_only)

"""
def for18(name , **kwds):
    return 'name' in kwds
"""

def for19(name , / , **kwds):
    return 'name' in kwds

def for20(*args , sep="/"):
    return sep.join(args)

def for21(n):
    return lambda x: x+n

def for22():
    ''' This Doc string does literally nothing
    
    Empty space 
    '''
    pass

def for23(ham : str , eggs: str = 'eggs') -> str:
    print("Annotations : " , for23.__annotations__)
    print("Arguments : " , ham , eggs)
    return ham + eggs

def lists():
    print("Inside Lists ")
    list = []
    list.append(2)
    print(list)
    list.insert(2, 12)
    print(list)
    for i in list:
        print(i)
    list.remove(12)
    print(list)
    for i in range(3,10):
        list.append(i)
    print("List before popping : " , list)
    list.pop()
    print(list)
    list.clear()
    print(list)
    for i in range(3,10):
        list.append(i)
    print(list)
    print(list.index(5))
    list.append(6)
    print(list.count(6))
    list.sort()
    print(list)
    list.reverse()
    print(list)
    list.sort(reverse =False)
    print(list)
    list.sort(reverse =True)
    print(list)
    print(list.copy())
    l2 = list
    print("Copied list l2 : " , l2)


def stacks():
    print("Inside Stacks ")
    stack = [3,4,5]
    stack.append(6)
    stack.append(7)
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)

def queues():
    print("Inside Queues")
    queue = deque(["Eric" , "Michael" , "Json"])
    queue.append("Terna")
    queue.append("Graham")
    print(queue)
    print(queue.popleft())
    '''print(queue.popright())  - Doesn't work '''
    print(queue)
    
def list_comprehensions():
    print("Inside List Comprehensions ")
    squares = []
    for x in range(10):
        squares.append(x**2)
    list = []
    print(squares)
    print(list(x**2 for x in range(10)))    
    squares_2= [x**2 for x in range(10)]
    print(squares_2)
    c = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
    print(c)
    combs  = []
    for x in [1,2,3]:
        for y in [3,1,4]:
            if x!=y:
                combs.append((x,y))
    print(combs)
    vec = [-4 , -2 , 0, 2 , 4]
    print([x**2 for x in vec])
    print([x for x in vec if x>=0])
    print([abs(x) for x in vec])
    fresh_fruits = ['banana' , 'loganberry' , 'passion fruit']
    print([weapon.strip() for weapon in fresh_fruits])
    print([weapon for weapon in fresh_fruits])
    print([(x, x**2) for x in range(6)])
    v = [[1,2,3] , [4,5,6] , [7,8,9]]
    print([num for elem in v for num in elem])
    print([str(round(pi , i)) for i in range(1,6)])
    for i in range(1,6):
        print(round(sqrt(2), i))

def nested_list_comprehensions():
    matrix = [
        [1,2,3,4] , 
        [5,6,7,8] , 
        [9,10,11,12], 
    ]
    print("Inside nested_list_comprehensions")
    print(matrix)
    print([[row[i] for row in matrix] for i in range(4)])
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])
    print(transposed)
    transposed.clear()
    for i in range(4):
        for row in matrix: 
            transposed.append([row[i]])
    print(transposed)
    transposed.clear()
    for i in range(4):
        transposed_row = []
        for row in matrix : 
            transposed_row.append(row[i])
            transposed.append(transposed_row)
    print(transposed)





if_case()
for1()
for2()
for3()
for4()
for5()
for6()
for7()
fib(12)
f = fib
f(30)
print(fib(0))
print(fib2(12))
ask_ok('Do you really want to quit')
xyz = 34
for8()
print(for9(12))
print(for9(2))
print(for9(1))
print(for10(34))
print(for10(4))
print(for10(3))
for11(1000)
for11(1000 , 'soft')
for11(1000 , 'Brittle' , type='Indian breed' , action = 'Singing')
""" Can only insert key-word argument after a non-keyword argument"""
for12(a=0)
for12(12)
for13("Hamburger" , "Its very runny, sir " , "It's really very very runny , sir" , shopkeeper='Michael Palin' , client = "John Cleese" , sketch = "Cheese shop sketch")
for14(2)
for15(2)
for16(arg = 2)
for17(1 , 1, kwd_only = 1)
for17(3 , standard = 3 , kwd_only =3)
"""for18(1 , **{'name' : 2}) """
print(for19(1,  **{'name' : 2}))
print(for20("Earth" , "Mars" , "Venus"))
print(for20("Earth" , "Mars" , "Venus" , sep = '.'))
print(list(range(3,5)))
args = [3,6]
print(list(range(*args)))
d = {"voltage" : "four million" , "state" : "bleedin demised" , "action" : "Voom" }
print(for11(**d))
g = for21(42)
print(g(5))
print(g(3))
list = [(1 , 'one') , (2 , 'two') , (3, 'three') , (4,'four')]
list.sort(key=lambda pair: pair[1])
print(list)
print(for22.__doc__)
print(for23('spam '))

lists()
stacks()
queues()
list_comprehensions()
nested_list_comprehensions()