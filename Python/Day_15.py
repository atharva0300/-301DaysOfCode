
a=42 
def foo() : 
    global a  #assigns global a
    print(a)
foo() 
print(a)    # valus of a is the same

def f1() :
    a =[1,2,3,4]
    b = list(a)
    print(b is a )
    b.append(100)
    print(b)
    print(a)
    c = [1,2]
    b.append(c)
    print(b)
    b[5][1] = 100
    print(b)
    items = {
        'number' : 12
    }
    print(items)
    items['person'] = 13
    import math 
    items['math'] = math 
    items['error'] = ValueError
    print(items)
    string = "GOOG,  12, 12.123"
    field_types = [str , int , float]
    raw_fields = string.split(',')
    fields = [key(val) for key,val in zip(field_types, raw_fields)]
    print(fields)
    x = 12 
    print(isinstance(x , int )) 
    import fractions 
    a= 10+4j
    print(a)
    print(a.real)
    print(a.imag)
    b = 4.5
    print(b)
    print(b.is_integer())
    print(b.as_integer_ratio())
    a = [1,2,3,4,5]
    a = repr(a)
    b = str(a)
    print(a)
    # returns a string form
    print(b)
    # if str() is undefined , then repr() is invoked 
    # if repr() is undefined, then str() is invoked 
    # bool() , len() , hash() 
    a = [1,2,3,4,5]
    print(isinstance(x,int))
    print(len(a))
    x = a[2]
    a[1] = 7 
    del a[2]
    print(a)
    print(5 in a )
    class DistanceFrom(object): 
        def __init__(self, origin):
            self.origin = origin
        def __call__(self , x):
            return abs(x - self.origin)

    num = [1,37,42,101,13,9,-20]
    num.sort(key = DistanceFrom(10))
    print(num)

def f2():
    #Operators and Expressions
    a = [3,4,5]
    b = [a]
    c = 4*b
    print(c)
    a[0] = -7
    print(c)
    a = [3,4,5]
    c = [list(a) for j in range(4)]
    print(c)
    items = [1,2,3]
    a,b,c = items 
    print(a,b,c)
    letters = 'acb'
    a,b,c, = letters
    print(a,b,c)
    datetime = ((5,19,2008) , (10,30,"am"))
    (month , date , year) ,(hour,  minute , am_pm) = datetime
    print(date, month , year)
    print(hour , minute,  am_pm)
    a = [1,2,3,4,5,6,7,8]
    del a[1:5:2]
    print(a)
    a = [1,2,3,4,5]
    a[1::2] = [10,11]  
    print(a)
    a = [1,2,3,4,5,6,7,8]
    a[1::2] = [11,22,33,44]
    print(a)
    del a[1::2]
    print(a)
    a = 42
    b = 13.1234
    c = 'HELLO'
    d = {'x' :13 ,'y': 1.321 , 'r' : 'world'}
    e = 123456789

    r = 'a is %d' %a
    print(r)
    r = '%10d %f' %(a,b)
    print(r)
    r = '%+010d %E' %(a,b)
    print(r)
    r = '%*.*f' %(5,3,b)
    print(r)
    r = 'e : %d' %e
    print(r)
    stock = {
        'name' : 'GOOG',
        'shares' : 100,
        'price' : 490.10123
    }
    r = '%(shares)d of %(name)s at %(price)0.2f' %stock
    print(r)
    name = 'atharva'
    age = 41 
    r=  '%(name)s is %(age)d years old' %vars()
    print(r)

    # Advanced string formatting 
    # using s.format( *args, **kwargs)
    r = '{0} {1} {2}' .format('GOOG' , 100 , 490.1034)
    print(r)
    r = '{name} {shares} {price}' .format(name ='GOOG' ,shares = 12, price =123.123)
    print(r)
    r = 'Hello {0}, your age is {age}' .format('atharva' , age =12)
    print(r)
    r= 'Use {{and}} to output single curly braces ' .format()
    print(r)

    stock = {
        'name' : 'GOOG', 
        'shares' : 100,
        'price' : 123.123
    }
    r = '{0[name]} {0[shares]} {0[price]} ' .format(stock)
    print(r)
    x = 4+3j 
    r = '{0.real} {0.imag} ' .format(x)
    print(r)

    r = '{name:8} {shares:8d} {price:0.2f} ' .format(name='GOOG' , shares=100 , price=123.123)
    print(r)
    # Column printing 
    naem = 'atharva'
    r ='{0:<10} ' .format(name)
    print(r)
    r = '{0:>10} ' .format(name)
    print(r)
    r = '{0:^10}' .format(name)
    print(r)
    r = '{0:=^10}'.format(name)
    print(r)

    x = 42 
    r = '{0:10d} ' .format(x)
    print(r)
    r = '{0:10x} ' .format(x)
    print(r)
    r = '{0:10b} ' .format(x)
    print(r)
    r = '{0:010b} ' .format(x)
    print(r)
    y = 3.1415926
    r = '{0:10.2f} ' .format(y)
    print(r)
    name = 'atharva'
    r = '{0!r:^20} ' .format(name)
    print(r)
    r = '{0!r:^10} ' .format(name)
    print(r)

    # dictionaries and operations
    d = {}
    d[1,2,3] = 'foo'
    d[1,0,3] = 'bar'
    print(d)
    d[(1,2,3)] = 'atharva'
    print(d)
    a = 3
    b = [1,2]
    c ='Hello %s %s'
    a = a +1 
    b[1] = b[1] + 10
    c %= ("Monty" , "Python")
    print(a)
    print(b)
    print(c)

    # Attribute (.) operator 
    def foo(x,y,z) : 
        return x+y+z 
    
    from functools import partial 
    f=partial(foo , 1,2)
    print(f(3))

    # Conversion functions 
    a = int("34")
    #b = long("0xfe76214",16)
    #b = float("3.1415926")
    c = eval("3, 5, 6 ")
    print(a)
    #print(b)
    print(c)
    x =5 
    y = 4 
    print(x is not y and x < y )

def f3() :
    # Program structure and Control Flow 
    d = {
        'name' : 'GOOG',
        'shares' : 100,
        'price' : 123.123
    }
    for key,value in d.items() : 
        print(key, value)
    print()
    # using enumerate() 
    for key , value in enumerate(d.items()):
        print(key , value) 
    
    a = int(input("Enter a number 1 : "))
    b = int(input("Ener number 2 : "))
    i=0
    while i<a and i<b : 
        print("Inside while loop {0} " .format(i))
        i = i+1 
    print()

    # Exceptions 
    a=1
    if ( a==1 ): 
        try : 
            a = 1/0
            print("Divison : " ,a)
        except ZeroDivisionError: 
            print("This is a zero Division Error")
    
    # Defining new exceptions 
    class Errors(Exception): 
        pass 
    
    class ListTransaction(object): 
        def __init__(self , thelist) :
            self.thelist= thelist
        def __enter__(self): 
            self.workingcopy = list(self.thelist)
            return self.workingcopy
        def __exit__(self , type,  value , tb) :
            if type is None:
                self.thelist[:] = self.workingcopy
            return False
        
    items = [1,2,3]
    with ListTransaction(items) as working :
        working.append(4)
        working.append(5)
    print(items)        # produces [1,2,3,4,5]
    
    try : 
        with ListTransaction(items) as working : 
            working.append(6)
            working.append(7)
            raise RuntimeError('We\'re hosed !')
    except RuntimeError: 
        pass 
    print(items)        #produces [1,2,3,4,5]

def f4() : 
    # Functions and Functional Programming 
    def foo(x , items=[]): 
        items.append(x)
        return items 
    print(foo(1))
    print(foo(2))
    print(foo(3))

    # To check empty list 
    def foo2(x , items = None ): 
        if items is None:
            items = []
        items.append(x)
        return items 

    print()
    print(foo2(1))
    print(foo2(2))
    print(foo2(3))
    import sys
    def printf(fmt , *args ): 
        # Call another function and pass along args 
        print(sys.stdout , fmt , *args )
    
    printf(12, (1,2))

    # keyword arguments 
    def foo(w,x,y,z) :
        pass 
    
    foo(x =12 ,y = 13 , z = 'hello' , w = 'persion')

    def make_table(data,**kwargs ): 
        #Get configuration parameters form params ( a dict )
        fgcolor = kwargs.pop('fgcolor' , 'black')
        bgcolor = kwargs.pop('bgcolor' , 'white')
        width = kwargs.pop('width' , None)
        print(fgcolor )
        print(bgcolor)
        print(width)
        #if kwargs: 
        #   raise TypeError( "Unsupported configuration options %s " %list(kwargs ))
    
    items = 10 
    make_table(items , fgcolor='black' , bgcolor= 'white' , borderstyle ='grooved' ,cellpadding=10 , wodth = 400)

    d = {
        'name' : 'atharva',
        'age': 12
    }
    app = (1,2,3)

    def foo(*args , **kwargs ): 
        for i in args: 
            print(i)
        for key , value in kwargs.items():
            print(key , value)
        
    foo(app , d)
    a= [1,2,3,4,5]
    def square(items): 
        for i,x in enumerate(items): 
            items[i] = x*x      # Modify items in-place 
        return items
    
    print(square(a))   

    # factor program
    def factor(a): 
        d=2
        while (d<=(a/2)): 
            if (a%d==0): 
                return ((a/d),d)
            d = d +1 
        return (a,1)

    x,y= factor(124)
    print(x)
    print(y)
    a=42 
    def foo(): 
        a=13
        print(a)    # a becomes 13 here 
    foo() 
    print(a)    # a is still 42 

    def countdown(start ): 
        n = start 
        def display(n) :
            print("T minus : " , n)
        while n>0: 
            display (n) 
            n = n-1 
    
    countdown(5)
    print("Second countdown : ")
    def countdown(start): 
        n = start 
        def display(n):
            print("T-minus : " , n)
        def decrement(): 
            # n = n-1  # error 
            nonlocal n
            n = n-1 
        while n>0: 
            display(n)
            decrement()
    
    countdown(5)
    i=0
    def foo(): 
        nonlocal i 
        i = i+1 
        print(i) 
    
    foo()

    def helloworld() :
        return 'Hello world'
    
    def callf(func) : 
        return func()
    
    print(callf(helloworld))

    x = 42 
    def callf(func) :
        return func() 
    def helloworld(): 
        return ('athava here %d' %x)
    
    print(callf(helloworld))
    #print(helloworld.__globals__)

    def bar() :
        x = 13 
        def helloworld2() :
            return ('atharva here %d' %x)
        return callf(helloworld2)

    
    def callf(func): 
        return func()
    
    print(bar())

    def countdown(n):
        def next() :
            nonlocal n 
            r= n
            n = n-1 
            return r 
        return next 
    # Example use 
    next = countdown(10)
    while True :
        v = next()  # get the next value 
        print(v,end=",")
        if not v: 
            break
    print()

def f5()  :
    # Decorators 
    def make_pretty(func): 
        def inner()  :
            print("I got decorated")
            func() 
        return inner

    def ordinary(): 
        print("I'm ordinary ")

    ordinary = make_pretty(ordinary)
    ordinary()

    # using decorator 
    @make_pretty
    def ordinary() :
        print("I am ordinary ")

    
    def print_result(func): 
        print("Result : ")
        print(func()) 
    
    @print_result
    def addition2(): 
        return 2+3

    # Generators and yields 
    def countdown(n): 
        print("Counting down from %d " %n)
        while n>0: 
            yield n 
            n = n-1 
        return
    
    c =countdown(5)
    for i in range(0,5) : 
        print(c.__next__())
    print("\nSecond iteration : ")
    d = countdown(5)
    
    

    
    
    

    
    
    
    
    




    
    
    
    




#f1()
#f2()
#f3()
#f4()
f5() 
