

import abc
from sys import getrefcount


a = 5 
def foo() : 
    global a 
    a = 10 
foo() 
print(a)
def f1() :
    # conditionals 
    a, b = 2,3
    if a<b: 
        print("a is less than b ")
    elif a>b: 
        print("a is greater than b")
    else : 
        print("a==b")
    
    s = 'string'
    if 'spam' in s : 
        has_spam = True 
    else : 
        has_spam = False 
    print(has_spam)
    has_spam = 'spam' in s 
    print(has_spam)

    # file input / output 
    f = open("test2.txt") # returns a file object 
    line = f.readline()  # invokes readline() method on the file
    while line : 
        print(line)
        # print(line , end=" ")
        line = f.readline()
    f.close()

    print("Using other way : ")
    for line in open("test2.txt"): 
        print(line , end=" ")
    print()

    # output of the program ot 
    # go into the file 
    f = open("test2.txt" , 'w')
    principle = 1000
    rate = 0.05
    year = 2
    numyears = 4
    while year<=numyears:
        principle = principle * ( 1+rate)
        f.write("\n%3d %.2f " %(year , principle))
    
        year = year +1
    f.close() 

    # input / output using sys 
    import sys 
    sys.stdout.write("Enter your name : ")
    name = sys.stdin.readline() 
    print(name)

def f2() : 
    # strings 
    a = 'hello world'
    b = 'python is cool'
    c ='atharava pingale '
    multi = '''
            This is a multi line string'''
    print(multi)
    print("a : " , a)
    d = a[4]
    print(d)

    # extracting substrings
    e = a[:5]
    f = a[6:]
    g=a[3:8]
    print(d,"\n",e,"\n",f,"\n",g,"\n")
    h = a+ ' this a another string'
    print(h)
    x= '2'
    y = '3'
    z = int(x) + int(y)
    print(z)
    p= 5 
    print(str(p))
    print(repr(p))
    print(format(p, "4d")) # Inserts spaces to the left 
    # here, inserts 4 spaces to the left 
    print("printing : " + format(p ,"4d"))
    x =3.4
    print(str(x))
    print(repr(x))
    print("printing : " +format(x , "0.5f"))
    print("printing : %0.5f " %(x))

    # lists 
    names = ['atharva ' , 'ratnadeep' , 'pingale']
    print(names[0] , names[1])
    # appending items in a list 
    names.append('awesome')
    print(names[0])
    # to insert 
    names.insert(4,'person')
    print(names[4])
    b = names[1:]
    print(b)
    c = names[2:3]
    print(c)
    a = [1,2,3] + names 
    print(a)
    names = list() 
    print(names )
    # multi lists 
    a = [1,"Dave",3.14, ["Mark", 7, 9, [100,101]], 10]
    print(a[0])
    print(a[3][0])
    print(a[3][1])
    print(len(a))

    # advanced list fetures 
    import sys 
    if len(sys.argv)!=2: 
        print("please supply a filename")
        raise SystemExit(1)
    f=open(sys.argv[1])
    lines = f.readline()
    f.close() 

    # convert all of the input values from the string 
    # to floats 
    fvalues = [float(line) for line in lines]

    # print the min and max values 
    print("The maintain value : " , min(fvalues))
    print("The maximum values is : " , max(fvalues ))

def f3()  :
    # tuples 
    stock = ('goog' , 100 , 120.12)
    a,b,c, = stock
    print(a,b,c)
    filename = "portfolio.csv"
    portfolio = []
    '''
    for line in open(filename): 
        fields = line.split(',')
        # splits eaac hline into a lit 
        name = fields[0]
        shares = int(fields[1])
        price = float(fields[2])
        stock = (name , shares , price)
        portfolio.append(stock)
    '''
    total = 0.0
    for name, shares ,price in portfolio: 
        total = total + shares * price 
    
    # sets 
    s = set([3,2,4])
    print(s)
    t = set(['a','e','i','a'])
    print(t)
    a = t | s  # union of t and s 
    print(a)
    b = t&s # intersection of t and s 
    print(b)
    c = t-a     # set difference ( items in t , but not in s)
    print(c)
    d = t^s     # symmetric difference ( item in t or s , but not in both)
    print(d)

    # using hte update() method 
    # and add 
    t.add('x')
    print(t)
    t.update([11,22,33])
    print(t)
    # remove() method 
    t.remove ('x')
    print(t)

    # dictionaries 
    stock = { 
        'name': 'goog',
        'shares' : 100,
        'price' : 12.5
    }
    print(stock.keys())
    print(stock.items())
    print(stock.values())
    stock['name'] = 'atharva'
    print(stock)
    print(stock['name'])
    prices = {} 
    # empty dictionary 
    print(prices)
    prices = dict() 
    # another way to declare a dictionary 
    # empty dictionary 
    print(prices)

    ele = list(stock)
    print(ele)
    element = list(stock.values())
    print(element)
    del stock['name']
    print(stock)
    
def f4()  :
    # iteration and looping 
    for n in [1,2,3,4,5]: 
        print(n,end=" ")
    print()
    for n in range(10): 
        print(n , end=" ")
    print()
    for n in range(1,10,2): 
        print(n , end=" ")
    print()
    a ='hello'
    for n in a : 
        print(a , end=" ")
    print()
    b = ['atharva' , 'pingael' , 'person']
    for n in b: 
        print(b , end=" ")
    print()
    c = { 'GOOG' : 490.10, 'IBM' : 91.50, 'AAPL' : 123.15 }
    for key, value in c.items() : 
        print(key ,value )
    print()
    for n in 'hello': 
        print(n,end=" ")
    print()
    
    # print all lines of the file 
    print("files contents : ")
    f = open("test2.txt")
    for line in f : 
        print(line)
    print(line)

def f5()  :
    # functions 
    def remainder (a,b): 
        return a%b
    
    print(remainder(2,3))

    # global variables inside a function 
    a = 5 
    def foo()  :
        a =6 
        print(a)
    
    foo()
    # generators 
    def countdown(n) :
        print("counting ")
        while n>0: 
            yield n     # generate a value (n)
            n= n-1 
    
    a= countdown(5)
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    # print(a.__next__())
    # Stop Iteration Error

    # Coroutines 
    def print_matches (matchtext ): 
        print("Searching : ", matchtext)
        while True : 
            line = (yield)
            if matchtext in line : 
                print(line)
    
    matcher = print_matches('python')
    matcher.__next__()
    # advanced the first yield 
    matcher.send('atharva')
    matcher.send('programmingwithpython')
    matcher.close()
    # done with the matcher function call

    #prep all o the matchers by calling next() 
    match = print_matches('python')
    matchers = [
        'python' , 'atharva' , 'pythoniscool'
    ]
    match.__next__()
    for m in matchers :
        match.send(m) 
    print("2nd : ")
    matchers2 = print_matches('atharva')
    matchers2 = [
        print_matches('python'),
        print_matches('atharva'),
        print_matches('person'),
    ]
    for m in matchers2 : 
        m.__next__()
    print()
    def person(name): 
        while True: 
            line = (yield)
            if name in line :
                print("bat found : " ,line) 
    
    l = [
        person('atharva'),
        person('batmat'),
        person('cat')
    ]

    for lemon in l: 
        lemon.__next__()

def f6() : 
    items = [12,23]
    print(items)
    items.append(12)
    print(items)
    #print(dir(items))
    print(items.__add__([99,999]))
    
    class stack(object ) :
        def __init__(self): 
            self.stack = []
        
        def push(self , object ):
            self.stack.append(object)
        def pop(self): 
            return self.stack.pop()
        def length(self): 
            return len(self.stack)
    
    try: 
        f = open("test2.txt" , "r")
    except IOError as e: 
        print(e)

    f.close()

def f7() :
    # string literals 
    f= 1.23e3
    print(f)
    print("person \\abcd")

    def person() :
        guess = 'bat'
        while True : 
            line = (yield)
            if guess in line : 
                print("bat found : " , line)
    
    a = person()
    a.__next__()
    l = [
        a.send('athava'),
        a.send('batman'),
        a.send('catwoman'),
        a.send('batwings')
    ]

    for lemon in l: 
        lemon
    
    # containers 
    # doc strings 
    def fact(n): 
        if n==1 :
            return 1
        else :
            return n*fact(n-1)
    a = fact(5)
    print(a)
    print(fact.__doc__)

    # decorators 
    class foo(object): 
        @staticmethod
        def bar() :
            pass
    a =3+4j
    print(a.real)
    print(a.imag)
    l = [1,2,3]
    if l is list: 
        print('yes, its a list')
    if isinstance(l,list): 
        print("yes, isinstance of list")
    d = dict () 
    if isinstance(d,dict): 
        print("yes, is a dict")
    
    import sys 
    print(sys.getrefcount(d))
    a = 10
    d['name'] = 12
    if d is not dict : 
        print("no")
    print(sys.getrefcount(d))
    del d 
    a = [1,2,3,4]
    b = a 
    print(b is a )
    print(sys.getrefcount(a))
    print(sys.getrefcount(b))
    a =[1,2,[3,4]]
    b = list(a)  # creates a shallow copy of a 
    print(b is a )
    # not equal to a

    b.append(100)
    print(b) 
    
    import copy
    a = [1,2,[3,4]]
    b = copy.deepcopy(a)
    # creates a deep copy of a in b 
    print(b is a )
    # prints false 

    # first class objects 
    line ='atharva,pingale,awesome '
    raw_line = line.split(',')
    print(raw_line)
    l = [1,2,3]
    print(all(l))
    print(any(l))
    l = []
    print(all(l))
    print(any(l))
    l = [1,2,3]
    print(sum(l))
    l = [1,5,2,4]
    a = l.sort() 
    print(l)
    m = l.reverse()
    print(m)
    print(l)
    l.sort() 
    print(l)
    print(l.index(2))
    string ='atharvaiscool'
    print(string.find('p'))
    print(string.replace('a' ,'0'))
    print(string.encode('ascii'))
    print(string.encode('utf-8'))
    a = "Your name is {0} and your age is {1}"
    print(a.format('person' , 23))
    print(string.capitalize())
    print(string.upper()) 
    print(string.lower())
    print(len(string))
    print(string.count('a'))
    print(string.find('a'))
    print(string.isalpha())
    print(string.isnumeric())
    c = '12' 
    print(c.isnumeric())
    print(string.istitle())
    print(string.join('.'))
    print(string.replace('a' , '.'))
    print(string.split('a'))
    print(string.swapcase())
    print(string.title())
    print(string.zfill(0))

    d = dict()
    d = {
        'name' : 12,
        'age' : 13
    }
    print(d)
    print(d.keys())
    print(d.values())
    print(d.items())
    #print(d.popitem('name' , 12))
    print(d)
    d['age'] = 13
    print(d)
    e = {
        'person' : 14
    }
    print(d.update(e))
    print(d)
    print(12 in d)
    print('name' in d )
    print(12 in d.values())
    print(d.get('name'))
    print(d.popitem())
    print(d)
    d.clear() 
    print(d)

    # sets 
    s = set([1,2,3,3,2])
    print(s)
    print(len(s))
    print(s.copy() )
    s2 = set([1,2,44])
    print(s.difference(s2))
    print(s2.difference(s))
    print(s2.issubset(s))
    print(s2.issuperset(s))
    print(s2.symmetric_difference(s))
    print(s2.intersection(s))
    print(s.add(11))
    print(s)
    print(set.difference_update(s2))
    print(s.discard(2))
    print(s)
    print(s.pop())
    print(s)
    print(s.remove(1))
    print(s)
    print(s.update(s2))
    s.clear()
    print(s)


def f8() : 
    # user defined functions 
    class foo(object): 
        def con(self,num): 
            return num

    print(type(foo))
    f = foo()
    print(type(f))
    p = foo() 
    un_p = foo.con
    print(un_p(p,100))
    l = [1,2,3]
    iter = l.__iter__()
    while True : 
        try : 
            x = iter.__next__() 
            print(x)
        except StopIteration: 
            break
    
    






#f1()
#f2()
#f3() 
#f4()
#f5() 
#f6()
#f7()
f8()     
