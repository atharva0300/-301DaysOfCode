from collections import deque


def func():
    list = []
    list.append(2)
    for i in range(2,10):
        list.append(i)
    print(list) 
    list.insert(12, 12)
    print(list)
    list.remove(12)
    print(list)
    list.pop(2)
    print(list)
    list.pop()
    print(list)
    list.clear()
    print(list)
    for i in range(2,10):
        list.append(i)
    print(list)
    print(list.count(3))
    list.sort()
    print(list)
    list.sort(reverse = True )
    print(list)
    list.sort(reverse = False )
    print(list)
    list.reverse()
    print(list)
    print(list.copy())
    print(list.index(3))


def func2():
    print("Inside fun2 : ")
    stack = [3,4,5]
    stack.append(6)
    stack.append(7)
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)


def func3():
    queue = deque(['Eric' , 'Json' , ' James'  'Larry'])
    print(queue)
    print(queue.popleft())
    print(queue)
    queue.append('Granny')
    print(queue)

def func4():
    squares  = []
    for x in range(10):
        squares.append(x)
    print(squares)
    squares_2 = list(map(lambda x: x**2 , range(10)))
    print(squares_2)
    squares_3 = [x**2 for x in range(10)]
    print(squares_3)
    print([[x,y] for x in range(10) for y in range(5) if x!=y])
    print("\n")
    print([[x,y] for x in  [1,2,3] for y in  [3,1,4] if x!=y])
    combs = []
    for x in [1,2,3]:
        for y in [3,1,4]:
            if x!=y:
                combs.append((x,y))
    print(combs)

    vec = [-4,-2,0,2,4]
    print([x**2 for x in  vec])
    print(x for x in vec if x>0)
    print(abs(x) for x in vec)
    fresh_fruit = ['banana' , 'loganberry' , 'passion fruit']
    print(fresh_fruit)
    for i in fresh_fruit:
        print(i)
    print([weapon for weapon in fresh_fruit])
    print([weapon.strip() for weapon in fresh_fruit])
    print([(x , x**2) for x in range(6)])
    print([[x , x**2] for x in range(6)])
    from math import pi
    from math import sqrt
    print(pi)
    print([str(round(pi , i)) for i in range(1,6)])
    print([str(round(sqrt(2) , i)) for i in range(6)])
    vec  = [[1,2,3] , [4,5,6] , [7,8,9]]
    print([num for elem in vec for num in elem])


def func5():
    matrix = [
        [1,2,3,4] , 
        [5,6,7,8] , 
        [9,10,11,12]
        ]
    print([[row[i] for row in matrix] for i in range(4)])
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])
    
    transposed.clear()
    for i in range(4):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    print(transposed)

    print(list(zip(*matrix)))


def func6():
    a = [-1 , 1 , 66,25 , 333 , 333 , 1234.5]
    del a[0]
    print(a)
    del a[2:4]
    print(a)
    del a[:]
    print(a)
    for i in range(3):
        a.append(i)
    del a 
    '''print(a)     - using print(a) after del a gives an error '''

def func7():
    t = 12345 , 54321 , 'hello!'
    print(t[0])
    for i in range(len(t)):
        print(t[i])
    print("Second iteration : ")
    for i in t:
        print(i)
    u = t ,(1,2,3,4,5)
    print(u)
    v = ([1,2,3], [3,2,1])
    print(v)

def func8():
    empty = ()
    singleton = 'hello'
    print(len(empty))
    print(len(singleton))
    d = 'hello' , 'my' , 'dear ' ,'friends '
    print(len(d))
    x , y , z , j = d
    print(x , y , z , j) 

def func9():
    basket = {'apple' , 'orange' , 'banana' , 'pear' , 'grapes' , 'rasperry' , 'apple'}
    print(basket)
    print('orange' in basket)
    print('lemons' in basket)
    a = set('abracadabra')
    b = set('alacazm')
    print(a ,b)
    c = a,b
    print(c)
    print(a-b)
    print(a | b)
    print(a & b)
    print(a ^ b)
    d = {x for x in 'abracadabra' if x not in 'abc'}
    print(d)

def func10():
    tel = {'jack' : 123 , 'jill' : 456}
    print(tel)
    for i in tel.items():
        print(i)
    print(tel['jack'])
    tel['jack'] = 910
    print(tel['jack'])
    l = list(tel)
    print(l)
    s = sorted(tel)
    print(s)
    print('abcd' in tel)
    print('abcd' not in tel)
    print(len(tel))
    for i in range(len(tel)):
        print(l[i])
    print(dict([('sape' , 4132) , ('guido' , 234) , ('jack' , 976)]))
    print({x : x**2 for x in (2,4,6)})
    print(dict(sape=432 , guido = 765 , teaviv = 987))

def func11():
    knights = {'gallahed' : 'the pure' , 'robin' : 'the brave'}
    print(knights)
    for k , v in knights.items():
        print(k , v)
    for i , v in enumerate(['tic' , 'tac' , 'toe']):
        print(i ,v)
    questions = ['name' , 'quest' , 'favorite color']
    answers = ['lancelot' , 'the holy grail' , 'blue']
    for i ,v  in zip(questions , answers):
        print('What is your {0}? It is {1}.' .format(i,v))
    for i in reversed(range(1,10,2)):
        print(i)
    list = []
    print(list.reverse())
    basket = ['apple' , 'orange' , 'pear' , 'peach' , 'grapes']
    for i in sorted(basket):
        print(i)
    print("Reverse sorting : ")
    for i in sorted(basket , reverse=True):
        print(i)
    print("Sorting using set : ")
    for i in sorted(set(basket)):
        print(i)
    print("Reverse sorting using set : ")
    for i in sorted(set(basket) , reverse = True): 
        print(i)
    import math 
    raw_data = [56.2 , float('NaN') , 51.7 , 55.3 , 52.5 , float('NaN') , 47.8]
    filtered_data = []
    for value in raw_data:
        if value != math.isnan(value):
            filtered_data.append(value)
    print(filtered_data)

    filtered_data_2 = []
    for value in raw_data:
        if math.isnan(value):
            filtered_data_2.append(value)
    print(filtered_data_2)

def func12():
    s1 , s2, s3 = '' , 'basket' , 'hammer'
    nnull = s1 or s2 or s3
    print(nnull)


def func15():
    import fibo
    fibo.func13(1000)
    print(fibo.func14(1000))
    print(fibo.__name__)
    fib = fibo.func13
    fib(50)
    from fibo import func13 , func14
    func13(20)
    print(func14(20))
    # from fibo import *
    # imports everything 
    # func13(500)
    import fibo as fib
    fib.func13(40)
    print(fib.func14(40))
    from fibo import func13 as fibonacci
    fibonacci(40)
    from fibo import func14 as fibona
    print(fibona(40))








func()
func2()
func3()
func4()
func5()
func6()
func7()
func8()
func9()
func10()
func11()
func12()
func15()

