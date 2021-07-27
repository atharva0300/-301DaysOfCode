import itertools
from datetime import date 
from dataclasses import dataclass

def func1(): 
    for city in ["Berlin " , "Vienna" , "Zurich"]: 
        print(city)
print("\n")
for city in ("Python" , "Perl" , "Ruby"): 
    print(city)
print("\n")
for ch in "Iteration is easy":
    print(ch , end=" ")
print("\n")
cities = ["Berlin" , "Vienna" , "Zurich"]
# initializing hte object 
iterator_obj = iter(cities)
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))

element = [34,[4,5] , (4,5) , {"a":4} , "dfsdf" , 4.5]
for i in element :
    try : 
        iter(i)
        print(i , " is iterable : True ")
    except TypeError :
        print(i , "is iterable : False ")

def func2(): 
    #a generator function that yields 1 for first time 
    # 2 second time and 3rd  time 
    def simpleGeneratorFun():
        yield 1 
        yield 2 
        yield 3 
    
    #Driver code to check above generator 
    for value in simpleGeneratorFun():
        print(value)

    # using __next__() 
    print("\nUsing next : " )
    x = simpleGeneratorFun()
    # iterating over the generator object using next 
    
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())

    # A simole generator for Fibonacci numbers 
    print("\nSimple Fibonacci number generator : ")
    def fib(limit): 
        a,b = 0,1
        # One by one yield next Fibonacci Numebr 
        while a < limit : 
            yield a 
            a,b = b , a+b
    x = fib(5)
    for i in range(5): 
        print(x.__next__())
    
def func3() :
    # yield() and next() 
    def generator () :
        t=1 
        print("First result is : " , t )
        yield t 

        t += 1
        print("Second result is : " , t )
        yield t 

        t += 1
        print("Third result is : " , t)
        yield t 

        t += 1
        print("Fourth result is : " , t)
        yield t
    
    call = generator() 
    call.__next__()
    call.__next__()
    call.__next__()
    string = 'geek'
    li = list(string[i] for i in range(len(string)-1,-1,-1))
    print(li)
    
def func4():
    " This is a Docstring, under func4() " 
    def evenodd(x) :  
        if ( x%2==0) :
            print("Even number : ")
        else : 
            print("Odd number ")
    evenodd(5)
    evenodd(4)
    def square_value(num) :
        """ This is a function that returns sqaures number  """
        return num**2
    print(square_value(5))
    print(square_value.__doc__)
    def myfunc(x): 
        x[0] = 20

    # driver code ( not that 1st is modified )
    # after function call
    lst = [10,11,12,13,14,15]
    myfunc(lst)
    print(lst)

    def myfunc2(x) : 
        x = [20,30,40]
    
    lst = [10,11,12,13,14,15]
    myfunc2(lst)
    print(lst)
    def myfunc5(x) : 
        x = 20 
    
    x = 10
    myfunc5(x) 
    print(x)

    def swap(x,y) :
        temp = x 
        x=  y
        y = temp
    # driver code 
    x = 2
    y = 3
    swap(x , y)
    print(x)
    print(y)
    def myfunc3(x, y=50): 
        print(" x : " , x)
        print("y : " , y)
    # driver code ( we call myfunc() with only )
    # argument 
    myfunc3(23)
    def student(firstname , lastname): 
        print("first name : " , firstname )
        print("Last name : " , lastname)
    
    #keyword arguments 
    student(firstname = "john" , lastname = "Elton")
    student(firstname = "sonu" , lastname = "nigam")
    # *args for variable number of arguments 
    def myfunc4(*argv) :
        for arg in argv : 
            print(arg)
    
    myfunc4('Hello' , 'This ' , 'is ' , 'a ' ,'human')
    def myfunc6(**kwargs) :
        for key , value in kwargs.items() : 
            print("Key : %s " %(key) )
            print("Value : %s" %(value))

    myfunc6(john = '12', elton='23' , person ='45')
    print("Calling the function the second time : ")
    myfunc6(john = 12, elton=23 , person =45)
    def cube(x): 
        return x**3
    cube_2 = lambda x :x*x*x
    print(cube(7))
    print(cube_2(7))

def func5() : 
    print("Inside func4() : ")
    # Class method 
    class Person : 
        def __init__(self , name , age ): 
            self.name = name 
            self.age = age 
        
        # a class method to create a Person object by birth year 
        def fromBirthYear(cls , name , year ): 
            return cls( name , date.today().year - year)
        
        # A static method to check if a person is adult or not 
        def isAdult(age): 
            return age> 18
        
    person1 = Person('john' , 21)
    person2 = Person.fromBirthYear( Person ,'John' , 1996)
    print(person1.age)
    print(person2.age)

    # print the result 
    print(Person.isAdult(40))

def func6() :
    def empty() : 
        pass 
    empty() 

    def empty_2() : 
        animal = True 
        while ( animal==True ) : 
            pass 
            # Infonite loop
    #empty_2()

    def empty_3() : 
        animal = True
        if ( animal == True ): 
            pass 
        else :
            print("False")
    empty_3()

def func7(): 
    def simpleGenerator() : 
        yield 1 
        yield 2
        yield 3
    # Driver Code to check abive generatro function 
    for value in simpleGenerator() : 
        print(value)

    def nextSquare() : 
        i = 1 
        # An infinite loop to generate squares 
        while True :
            if i==10: 
                break
            yield i*i
            i += 1
            # next execution resumes 
            # from this point 
    # Driver code 
    # Infinite code 
    for num in nextSquare() :
        print(num) 
    # values from a method using class 
    class Test : 
        def __init__(self):
            self.str = 'JohnEltonisthebest'
            self.x = 20 
    # This function returns an object of test 
    def fun() :
        return Test() 
        
    # Driver Code 
    t = fun() 
    print(t.str)
    print(t.x)

    # This is a function returns a tuple 
    def fun() : 
        str = 'LinkinParkistheBest'
        x = 44
        return (str , x)
        # Returns a tuple 
    #Driveer code to test above method 
    str , x = fun() 
    # Assign returned tuple 
    print(str)
    print(x)
    # This gunction reutrns a list 
    def fun() : 
        str = 'AlanWalkeristheBest'
        age = 25
        return [str , age]
    
    # Driver code 
    list = fun() 
    print(list)

    #This function returns a dictionary 
    def fun() : 
        d = dict() 
        d['str'] = 'EdsheeranistheBest'
        d['age'] = 40 
        return d  
    
    # Driver Code 
    dope = fun()
    print(dope)

    # Using Data class in python 
    @dataclass
    class Book_list :
        perunit_cost : float 
        quantity_available : int =0 

        # a constructor to fill arguments in Dataclass() 
        # and access it form there 
        def __init__(self ,name : str , perunit_cost: float , quantity_available : int=0): 
            self.perunit_cost = perunit_cost
            self.quantity_available = quantity_available


        # function to calculate the total cost 
        def total_cost(self) -> float : 
            return self.perunit_cost*self.quantity_available
    
    book = Book_list("Introduction to Python Programming " , 200 , 4)
    x = book.total_cost()
    # returns a float value
    print(x)
    print(book) # Prints all the variables of the class 
    
    



func1()
func2() 
func3() 
func4() 
print(func4.__doc__)
func5() 
func6() 
func7() 
