

def f1() :
    # Iterator Operators 
    import operator 
    import time 
    # defining lists 
    l1 = [1,2,3]
    l2=  [2,3,4]

    # getting t1 time 
    t1 = time.time() 

    # calculating results 
    a,b,c = map(operator.mul,l1,l2)
    t2 = time.time() 
    print("Result : " , a,b,c)
    print("Time : %.20f " %(t2-t1))

    # Calculatign result using hte naive method 
    t1 = time.time() 
    print("Result :  ")
    for i in range(3): 
        print(l1[i]*l2[i])
    
    t2 = time.time() 
    print("Time taken : %.20f" %(t2-t1))

    # Types of iterators 
    # Infinite iterators 
    # Combinatorics intrators 
    # Terminating iterators 

    # Infinite Iterators 
    # count(start, step )
    import itertools 
    # for in loop
    for i in itertools.count(5,5): 
        if i==35 : 
            break
        else : 
            print(i)
    
    # cycle(iterator)

    count =0
    list = [1,2,3]
    for i in itertools.cycle(list): 
        if count>4: 
            break
        else  :
            print(i , end= " ")
            count =count +1 
        print()
    count =0
    for i in itertools.cycle('A'): 
        if count>4: 
            break
        else  :
            print(i , end= " ")
            count =count +1 
    print() 
    # repeat ( val , num)
    print("Repeating 'A' 4 times : " , itertools.repeat('A' , 4)) 
    print("Repeating 'B' 4 times : ")
    #print("Priting a 2 times : " , list(itertools.repeat('A',2))) 

    # Combinatoric iterators 

    # product ()
    print("The cartesian product using repeat : ")
    #print(list[itertools.product([1,2],repeat=2)])
    print()

    # Permutations() 
    # import the product function from itertools module






def f2() : 
    # import the product function from itertools module
    from itertools import permutations

    print ("All the permutations of the given list is:")
    print (list(permutations([1, 'geeks'], 2)))
    print()
    #Terminating iterators
    print ("All the permutations of the given string is:")
    print (list(permutations('AB')))
    print()

    print ("All the permutations of the given container is:")
    print(list(permutations(range(3), 2)))

    # combinations 
    from itertools import combinations 
    print("All the combinations of list in sorted order ( without replacement ) : ")
    print(list(combinations(['A',2],2)))
    print()

    print("ll the combination od string in sorted order ( without replacement ) : " )
    print(list(combinations('AB',2)))
    print()

    print("All the ocmbination of list in sorted order ( without replacement ) : ")
    print(list(combinations(range(2),1)))
    print(list(combinations(range(2),2)))
    print()

    # combinations with replacements 
    from itertools import combinations_with_replacement
    print("All the combinations of string in sorted order ( with replacmeents ) : ")
    print(list(combinations_with_replacement("AB",2)))

    print("All the combination of list in sorted order ( with replacements ) : ")
    print(list(combinations_with_replacement([1,2],2)))

    print("All the combinations of a container in sorted order ( with replacements ) : ")
    print(list(combinations_with_replacement(range(2) ,1)))

    # Terminating iterators 

    # accumulate(iter , func ) 
    l1 = [1,4,5,7]
    from itertools import accumulate
    import operator
    # usig accumulate () 
    # prints the successive summation of elements 
    print("The sum of each iteration is : " , end=" ")
    print(list(accumulate(l1)))

    # prints the usccessive summation of elements 
    print("The product after each iteration is : ", end=" ")
    print(list(accumulate(l1,operator.mul)))

    # chain(iter1, iter2)
    from itertools import chain
    l1 = [1,4,7,5]
    l2 = [1,2,3,6]
    print("All the values in the mentioned chain are : " , end=" ")
    print(list(chain(l1,l2)))

    # chain.from_iterable()

    import itertools
    l2 = [11,22,33,44]
    l3 = [l1,l2]
    print("All the value form chain.from_iterable() : " )
    print(list(chain.from_iterable(l3)))

    # compress (iter ,selector )
    from itertools import compress

    print("The compress vlues inthe string are : " , end=" ")
    print(list(compress('atharva' , [1,0,1,1,0,0,1])))

    # dropwhile(func,seq)
    
    from itertools import dropwhile
    l1 = [2,4,34,41,67,12]
    print("The values after condition returns false : ")
    print(list(dropwhile(lambda x: x%2==0 , l1)))

    # filterfalse(func, seq)

    from itertools import filterfalse

    print("The values that returns false to function are : ")
    print(list(filterfalse(lambda x : x%2==0 , l1)))

    # islice(iterable, start , stop , step)
    from itertools import islice 

    l1 = [2,4,5,7,8,10,20]
    # starts printing from the 2nd index till 6th skipping 2 
    print("The sliced list values are : " , end=" ")
    print(list(islice(l1 , 2,6,2)))

    # starmap(func, tuple list )

    from itertools import starmap

    l1 = [(1,10,5) ,(8,4,1) ,(5,4,9) ,(11,10,1)]
    # using starmap() for selection value according to function 
    # selects min of all the tuple values 
    print("The values according to function are : " , end=' ')
    print(list(starmap(min , l1)))
    print("The values according to function are : " , end=' ')
    print(list(starmap(max , l1)))

    # takewhile(func , iterable )

    from itertools import takewhile

    l1 = [2,4,6,7,8,10,20]
    # using takewhile() 
    print("Using takewhile : " , end=" ")
    print(list(takewhile(lambda x: x%2==0,l1)))

    # tee ( iterator , count )

    import itertools 

    l1 = [2,4,6,7,8,10,20]
    iteration = iter(l1)

    # using tee() to make a list of iterators 
    #makes list of 3 iterators having same values 
    it= itertools.tee(iteration , 3)

    # printing the values of the iterators 
    print("The iterators are : ")
    for i in range(3 ): 
        print(list(it[i]))

    # zip_longest(iterable1,  iterable2, fillval)
    from itertools import zip_longest
    # usingthe zip_longest 
    print("Using zip_longest : " , end=" ")
    print(*(zip_longest('atharva' , 'boy' , fillvalue = '_')))

def f3() : 
    # Python __iter__() and __next__() 
    #  iter(object )
    # iter(callable , sentinal)

    listA = ['a' , 'e' , 'i' ,'o' , 'u']

    iteration = iter(listA)
    try : 
        print(next(iteration))
        print(next(iteration))
        print(next(iter(iteration)))
        print(next(iter(iteration)))
        print(next(iter(iteration)))
        print(next(iter(iteration))) # Stop Iteration error 
    except : 
        print("Stop iteration reached ")

    # Code 2 
    print("Using while loop : ")
    list = [11,22,33,44,55]
    iteration = iter(list)
    while True : 
        try : 
            print(next(iteration))
        except : 
            print("Stop iteartion reached ")
            break
    
    # Code 3 
    print("Using __iter__() and __next__() ")
    list = ['cats' , 'bats ',  'hats ' ,'mats ']
    iteration = list.__iter__() 
    while True : 
        try: 
            print(iteration.__next__())
        except : 
            print("Stop iteration reached ")
            break

    # Using OOPS 
    class counter : 
        def __init__( self , start,  end): 
            self.num = start
            self.end=  end
        def __iter__(self) :
            return self
        def __next__(self): 
            if self.num>self.end: 
                raise StopIteration
            else : 
                self.num = self.num +1 
                return self.num-1
    
    # Driver Code 
    if __name__ =='__main__': 
        a,b = 2,5
        c1 = counter(a,b)
        c2 = counter(a,b)
        # way 1 to print without iter () 
        for i in c1: 
            print("Eating more pizzas, counting : ",  i ,end="\n")
        
        print("Print the range using iter : ")
        # Way -2 using iter() 
        print() 
        object = iter(c2)
        while True : 
            try : 
                print("Eating more pizzas, counting " , next(object))
            except : 
                # Whne StopIteratino is reached , print a custom message 
                print("Dead on overfood , GAME  OVER ")
                break

def f4(): 
    import itertools 
    # differece etwee iterator and iterable 
    for city in ['berlin' , 'vienna' , 'zurich']: 
        print(city )
    print() 
    for city in ("berlin" , 'vienna' , 'zurich'): 
        print(city)
    print() 
    for char in 'atharva' :
        print(char , end=" ")
    print()

    cities = ['berlin' , 'vienna' , 'zurich']
    iteration = iter(cities)
    for i in range(3): 
        print(next(iteration))
    print()

    # function is able to check object 
    # is iterable or not 
    def iterable (obj):
        try : 
            iter(obj)
            return True 
        except TypeError: 
            return False 
    
    # Driver Code 
    for element in [34, [4,5] , (4,5),'atharva',4.5]: 
        print(element , " is iterable " , iterable(element))

def f5(): 
    # a geerator function that yields 1 for the first time 
    # 2nd time and 4rd time 

    def simpleGenerator(): 
        yield 1 
        yield 2 
        yield 3 
    
    # Driver code 
    for value in simpleGenerator(): 
        print(value )
    print()

    # Generator object 
    def simpleGenerator () : 
        yield 1 
        yield 2 
        yield 3 
    
    # x is a generator 
    x = simpleGenerator() 
    for value in range(3): 
        print(x.__next__())
    
    # fibbonacci numbers generator
    print("Fibbonacci nmubers generator : ")
    def fib(limit): 
        # initialie the first 2 fibonacci numbers 
        a,b = 0,1 
        # One by one yeld next fibonacci numbers 
        while a< limit : 
            yield a 
            a,b =  b, a+b
    
    y = fib(5)
    # using loop
    for value in fib(5): 
        print(value, end=" ")
    print()


def f6() : 
    # Generator Expressions 
    def p(names): 
        for i in names: 
            yield i
    
    list = ['atharva' , 'aditya' , 'motu' , 'patlu']
    for i in p(list) :
        print(i)
    
    def generator(): 
        t=1 
        print("First result : " , t)
        yield t

        t=t+1 
        print("Second Result  : " , t)

        t=t+1 
        print("Third result : " , t)
        yield t 
    
    call = generator()
    call.__next__()
    call.__next__()

    # Pyhon code to illustrate generate expression
    generators = (num**2 for num in range(10))
    for num in generators: 
        print(num)
    print("Printing cubes : ")
    cubes= (i**3 for i in range(10))
    for i in cubes: 
        print(i)

def f7() : 
    # Functions in python 
    def evenodd(n): 
        if n%2==0: 
            print("even")
        else : 
            print("Odd")
    
    # Driver Code to call the function 
    evenodd(10)
    evenodd(3)

    # Docstring 
    def say_hi(): 
        '''
        This is a docstring buddy 
        '''
    
    print(say_hi.__doc__)

    # return statement 
    def square_value(num) : 
        ''' 
        This is a doctring brother 
        '''
        return num**2 
    
    print(square_value(10))
    print(square_value(4))
    print(square_value.__doc__)

    # Pass by refernce or pass by value 
    def myfunc(num): 
        num[0] = 20
    
    # Driver Code 
    list = [10,11,22,33,44,55]
    myfunc(list)
    print(list)
    # the list gets updated 
    # even when the value of the list 
    # was changed inside the function 
    # This is called 
    # call by value 
    print("Exmaple 2 : ")
    def myfun(x): 
        # Afer below line link of x with previous 
        # object gets broken.
        # A new object is assigned 
        # to x 
        x = [1,2,3]
        # This x is different than the x 
        # that the function took as an argument 
        # This x is a 
        # new list 
    # And not hte old one 
    # This means that the reference link was broken
    
    list = [11,22,33,44]
    myfun(list)
    print(list)
    # Here none of the value 
    # of the list 
    # gets updated 

    def myfun(x): 
        # After below line link of x with previous 
        # object gets broken. A new object is assigned 
        # to x 
        x = 20 
    
    # Driver Code ( Note that lst is not 
    # modified )
    # after function call 
    x = 10 
    myfun(x)
    print(x)
    # prints 10 
    # as the reference of x 
    # gets broken 

    # Example 
    def swap(x,y): 
        temp= x 
        x= y 
        y = temp
    
    # Driver Code 
    x=2 
    y=3 
    swap(x,y)
    print(x,y)
    # Prints 2 3 
    # because , the reference 
    # gets broken 

    # Default arguments 
    def myfun(x,y=50): 
        print("x : " , x)
        print("y : ",  y)
    
    # Driver Code 
    myfun(10)

    # Ketwork Arguments 
    def student(firstname , lastname ): 
        print(firstname , lastname ) 
    
    # Keyowrd Arguments 
    student( firstname = 'atharva' , lastname = 'pingale ')
    student(lastname = 'pingale' , firstname = 'atharva')

    # Variable length arguments 
    # *args for variable number of arguments 

    def myfun(*args ): 
        for i in args: 
            print(i)
    
    # Driver Code 
    myfun(("atharva" , 'is' , 'awesome'))

    # kwargs 
    def myfun(**kwargs ): 
        for key, values in kwargs.items(): 
            print(" %s " %(key) , values )
    
    # Driver Code 
    myfun(first='atharva' , last = 'person ' , day = 'tuesday')

    # Anonymous function 
    # using lambda 
    def cube (x): return x**3
    
    cube_c = lambda x : x**3
    
    # Driver Code 
    print(cube(3))
    print(cube_c(3))


def f8():
    # class method and static method in python
    # class C(object ):
    #   @classmethod 
    #   def fun(cls , arg1,arg 2...): 
    #   ...
    # 
    # fun : function that needs to be converted into a class 
    # # method 
    # returns a class method for a function 

    # Static method 
    
    from datetime import date

    class Person : 
        def __init__( self, name , age ): 
            self.name = name 
            self.age = age 
        
        # A class method to create a Person object by birth year 
        @classmethod 
        def fromBirthYear(cls , name , year ): 
            return cls(name, date.today().year- year)
        
        # A static method to checl if a person if an adult or not 
        @staticmethod
        def isAdult (age ): 
            return age > 18
    
    Person1 = Person('athava ',20)
    Person2 = Person('aditya' , 13)

    print(Person1.age )
    print(Person2.age )
    # prints the result 
    print(Person.isAdult(22))

def f9() : 
    # Write and Empty function 
    # in python 
    def fun() : 
        pass 

    fun() 

    # Empty loop in python 
    var = True 
    while (var ==True) : 
        pass

    if ( var ==True ): 
        pass 
    else : 
        print('False ')

def f10():
    # Return multiple values 
    # in python 
    # using object 

    class test: 
        def __init__(self ): 
            self.str = 'atharva'
            self.x = 20 
    
    # This function returns an object of test 
    def fun() : 
        return test() 
    
    # Driver Code 
    t = fun() 
    print(t.str)
    print(t.x)

    # usig ttuple to return multiple values 
    def fun()  :
        str = 'atharva '
        age = 20
        return (str , age )
        # returns a tuple 
        # ( str,  age )
    
    # Driver Code 
    str , x = fun() 
    print(str , x )

    # Using lists to return multiple values 
    def fun()  :
        str = 'atharva'
        age = 20 
        return [str , age ]
        # returns a list 
        # of [str , age ]
    
    # Driver Code 
    str, x = fun() 
    print( str , x )
    # or 
    list = [] 
    list = fun() 
    print(list )

    # Using a dictionary to return multiple values 
    def fun(): 
        d = dict() 
        d['name '] = 'atharva'
        d['age'] = 20 
        return d 
        # returns a dictionary 
    
    # Driver Code 
    d = fun() # stores a dictionary 
    print(d)

    # Using data classes in python 
    # dataclass can be used to return 
    # a class with automatically 
    # added unique methods 

    from dataclasses import dataclass 

    @dataclass 
    class Book_list :  
        perunit_cost : float
        quantity_available: int =0 

        # fuction to calculate total cost 
        def total_cost(self) -> float : 
            return self.perunit_cost *self.quantity_available
        
    book  = Book_list(300 , 3)
    x = book.total_cost()
    book2 = Book_list(400,4)
    y = book2.total_cost()

    # print the total cst 
    # of the book 
    print("x : " , x)
    print("y : " , y) 

    # print the book details 
    print(book)
    print(book2)

    # 8100
    Book_list(perunit_cost = 900,quantity_available = 9)


def f11() : 
    # Partial functions in python 
    #partial functions allow us to fix a certain 
    # number of arguments of a functioun 
    # and generate a new function 

    from functools import partial

    # A normal function 
    def f(a,b,c,d): 
        print(a,b,c,d)
    
    # A partial fucntion that calls f with 
    # a = 1 , b =2 , c = 3 , d = 4 
    g = partial(f,1,2,3)

    # Calling g 
    print(g(4))

    import functools
    def add(a,b,c) : 
        return a+b+c
    
    # A partial function 
    h = partial(add, 1,2)

    # printing h 
    print(h(3))

def f12( ) :
    # First class function in python 

    def shout (text ): 
        return text.upper() 
    
    print(shout('atharva'))
    yell = shout 
    print(yell('aditya'))

    def add(a,b) :
        return a+b 
    
    print(add(2,3))
    sub = add
    print(sub(4,5))

    def shout( text): 
        return text.upper() 
    
    def whisper(text ): 
        return text.lower() 
    
    def greet(func) :
        # storing the function in an variable 
        greeting = func('''hi, I am created by a function 
                        passed as an arguemnt ''')
        print(greeting)
    greet(shout)
    greet(whisper)

    def addo(a,b): 
        return a+b
    def subt(a,b):
        return a-b
    def op(func): 
        operation = func(2,3)
        print(operation)
    
    op(addo)
    op(subt)

    # functions can return another function 
    def create_adder(x) :
        def adder(y ): 
            return x+y
        return adder
    
    add_15 = create_adder(12)
    print(add_15(3))
    

def f13(): 
    # Precision handling in python
    import math 

    a = math.pi
    print(math.trunc(a))
    print(math.ceil(a))
    print(math.floor(a))

    # setting precision 
    a = math.pi
    print(" %.4f " %(a))
    b = 123.12345
    print(" %2.3f"  %(b))
    print(" {0} " .format(b))
    print("round value : " , round(b,2))
    print("round value : " , round(b,3))

def f14() : 
    # args and kwargs in python

    def myfun(*args): 
        for i in args: 
            print(i)
    
    myfun('atharva' , 'pingale ' , 'person')

    # kwargs 
    def myfun2(**kwargs): 
        for key, value  in kwargs.items()  : 
            print("%s == %s " %(key , value))
    
    myfun2(first =  'atharva' , second = 'pingale' ,last = 'age')

    def myfun(num , *args ): 
        print("num : ",  num)
        for i in args : 
            print(i)
    
    myfun(12, 'atharva', 'person')

    # kwargs 2 
    def myfun(arg1 , **kwargs ): 
        print("arg1 : ",  arg1)
        for key,value in kwargs.items() : 
            print(" %s == %s " %(key,  value ))
    
    # Driver Code 
    myfun(12,atharva = 'pingale' , person = 'boy' )

    # args and kwargs to call a function 
    def person(a,b,c ): 
        print("a : " , a)
        print("b : " , b)
        print("c : " , c)
    args = ('atharva' , 'pingale ', 'awesome ')
    person(*args)
    print()
    kwargs = {'a' : 'atharva' , 'b': 'pingale ' , 'c' : 'stars '}
    person(**kwargs)

def f15() :
    # Nested functions in python 
    def outer_function(text): 
        text = text 
        def inner_function(): 
            print(text)
        inner_function() 
    
    outer_function("awesome")

    def outer_function(text): 
        text = text 
        def inner_function(): 
            text = 'dangerous'
            print(text)
        inner_function() 
        print(text)
    
    outer_function("awesome")

    # Python Closures 
    def outerfunction(text) :
        text = text
        def innerfunction(): 
            print(text)
        
        # Note we are returning function 
        # WITHOUT parenthesis 
        return innerfunction
    
    myfunction = outerfunction('awesomness overloaded ') 
    myfunction() 


def f16()  :
    # Function decorators 
    # uses of decorator 
    # 1. we ca define a function inside another function 
    # 2. a function can be passed as a parameter to anither 
    # function ( a function can also return another function )

    # Adds welcome message to the string 
    def messageWithWelcome(str) :
        # Nested function 
        def addWelcome() : 
            return "Welcome to "
        
        # Return concantenation of addWelcome() 
        # and str 
        return addWelcome() + str 
    
    # To get site name to which welcome is added 
    def site(site_name ) :
        return site_name 

    print(messageWithWelcome(site('geeksforgeeks')))

    # Example 2 
    def outer (string) :
        # Nested function 
        def inner() : 
            return 'atharva is '
        
        return inner() + string 
    
    # Driver code 
    def take_word(word): 
        return word 
    
    print(outer(site('awesome ')))

    # function decorator 
    # A function decorator is a fucntion that takes a function as its 
    # only parameter and returns a function 
    
    # adds a welcome message to the string 
    # returned by fun(),takes fun() as 
    # parameter and returns welcome () 

    def outer(message): 
        # Nested function 
        def addwelcome(var) :
            return "welcome to " + message(var)
        
        # Decorate returns a function 
        return addwelcome 
    
    @outer
    def word ( outside ) :
        return outside 
    
    # Driver Code 
    # This call is equivalent to call to 
    # outer() with function 
    # word('atharva') s parameter

    print(word('atharva is cool')) 

    # decorators can be useful to ttahc 
    # data 
    # A decorator function to attach 
    # data to func 

    def attach_data(fun): 
        fun.data = 3 
        fun.variable = 12 
        return fun
    
    @attach_data
    def add(x,y ): 
        return x+y 
    
    # Driver Code : 
    # This call is equivalent to attach_data() 
    # with add() as a parameter 
    print(add(2,3))
    print(add.data)
    print(add.variable)

    def concatenating( word ):
        # Nested function 
        def inner(variable ) :
            return 'welcome to ' + word(variable)
        
        return inner
    
    @concatenating
    def word1(variable ): 
        return variable
    
    @concatenating 
    def word2(variable ): 
        return variable 
    
    # Driver Code 
    print(word1('mumbai'))
    print(word2('paris'))

    # addition and sibtraction 
    # using decoorator functions 

    def result (message) :
        # Nested function 
        def inner(a,b ): 
            return message(a,b) 
        
        return inner 
    
    @result 
    def addition(a,b ): 
        return a+b 
    
    @result 
    def sub(a,b): 
        return a-b 
    
    # Driver Code 
    print(addition(2,3))
    print(sub(2,3))

    
def f17() :
    # decorators with parameters 
    # in python

    def decorators(*args , **kwargs ): 
        def inner(func) : 
            '''
            Do operations with func 
            '''
            return func 
        
        return inner # this is the fun_obj 
        # mestioned in the above content 
    
    @decorators()
    def func()  :
        '''
        function implementation
        '''

    




    














#f1()
#f2()
#f3()
#f4()
#f5()
#f6()
#f7()
#f8()
#f9()
#f10()
#f11()
#f12()
#f13()
#f14()
#f15()  
#f16()
f17()            