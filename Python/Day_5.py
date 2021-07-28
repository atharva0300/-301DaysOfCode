from functools import partial 
from functools import *
import math 
import numpy as np

def func1()  :
    print("Inside fun1() : ")
    # a normal fucntion 
    def f(a,b,c,x): 
        return 1000*a + 100*b + 10*c + x 
    # A partial functin that calls f with 
    # a as 3 , b as 1 and c as 4 
    g = partial(f,3,1,4)

    # Calling g() 
    print(g(5))
    # a normal function
    def add( a,b,c): 
        return 100*a + 10*b + c
    # A partial function with
    # A partial function with b = 1 and c = 2 
    add_part = partial(add, c = 2 , b = 1)
    # cCalling the partial function
    print(add_part(3))
    # can be treated as objects 
    def shout(text): 
        return text.upper()
    
    print(shout("Hello"))
    yell = shout 
    print(yell("Hello to you "))

    # Can be passed as arguments to other functions 
    def shout(text): 
        return text.upper() 
    def whisper(text): 
        return text.lower() 
    def greet(func): 
        # storing the funtion in a variable 
        greeting = func("""Hi, I am created by a function passed as an argument""" )
        print(greeting)

    greet(shout)
    greet(whisper)

    # Functions can return another functions 
    def create_adder(x) :
        def adder(y) :
            return x+y
        return adder 
    add_15 = create_adder(15)
    print(add_15(10))

    # Precision Handling in python 
    # initializing value 
    a = 3.4567

    # using trunc() to print integer after truncating 
    print("The integral value of number is : " , end=" ")
    print(math.trunc(a))
    # Using the ceil() to print hte number after ceiling 
    print("The smallest integer greater than number is : " , end=" ")
    print(math.ceil(a))
    # Using hte floor() to print hte number after flooring 
    print("The greatest integer smaller than number is : " , end=" ")
    print(math.floor(a))

    # Setting Precision in python 
    # using round() 
    a = 3.45677
    # Using hte '%' to print value till 2 decimal places 
    print("The value of number till 2 decimal place( using % ) is : " ,end= " ")
    print(' %.2f ' %a)

    #using the format9) to print hte vlaue til 2 decimal places 
    print("The value of number till 2 decimal place ( using format() ) is :  " , end=" ")
    print(' {0:.2f} ' .format(a))

    #using the round() to print alue till 2 decimal places 
    print("The value of number till 2 decimal places using the round() is : " , end=" ")
    print(round(a,2))

def func2() : 
    print("Inside func2() : ")
    # Using *args for variable number of arguments 
    def myFun(*argv): 
        for arg in argv :
            print(arg)
    myFun('Hello' , 'this' , 'is' , 'cool')

    # *args with first extra argument 
    def myFun(arg1 , *argv): 
        print("First argument : " , arg1)
        for arg in argv  :
            print("Next argument through *argv : " , arg)
    myFun('Hello' , 'this' , 'is' , 'cool')

    #  Using kwargs 
    def myFun(**kwargs ): 
        for key , value in kwargs.items()  :
            print("%s == %s " %(key , value ))
        
    myFun(first='hello' , second = 'this' , third='is cool')
    def myFun( args , **kwargs ): 
        print("Printing an arg : " , args)
        for key , value in kwargs.items() : 
            print("%s == %s" %(key , value))
    
    #driver code 
    myFun('hi' , first = 'this' , second ='is cool')
    # Using args nad kwargs to call a function 
    def myFun( arg1 , arg2 , arg3): 
        print( "arg 1 : "  , arg1)
        print( "arg 2 : "  , arg2)
        print( "arg 3 : "  , arg3)
    # Now we can use *args or **kwargs to 
    # pass the arguments to this function
    args = ('this'  ,'is ' , 'legit')
    myFun(*args)

    print("Passing **kwargs")
    kwargs = {'arg1' : 'this' , 'arg2' : 'is' , 'arg3' : 'legit'}
    myFun(**kwargs)

    print("Kwargs anothe example : ")
    def myFun( a,b,c) :
        print(a ,b, c )
    kwargs = {'a' : '1' , 'b' : '2' , 'c' : '3'}
    myFun(**kwargs)

    def myFun(*args , **kwargs ): 
        print(" args : " , args)
        print("Kwargs : " , kwargs )
    
    # Passing arguments for args and kwargs 
    myFun('this ' , 'is ', 'legit ' , a ='1' , b = '2' , c='3' ) 


def func3():
    print("Inside func3() : ")
    # Nested function in python 
    def outerFunction(text) :
        def innerFunction(): 
            print(text )
        
        innerFunction()
    if __name__ == "__main__" :
        outerFunction('Hello there ! ')

    def pop(list):
        def pop_number( my_list): 
            return my_list[len(my_list) -1]
        
        list.remove(pop_number(list))
        return list
    
    # callng function
    list = [1,2,3,4,5]
    print(pop(list))
    print(pop(list))
    print(pop(list))

    #Python Closures 
    def outerFunction(text) :
        def innerFunction(): 
            print(text)
        
        # Return the function without the parenthesis 
        return  innerFunction
        # returns a function 

    a = outerFunction('hello there ! ')
    # Storing the returned function inside the variable 'a'
    print(a())
    # Closures is a function object that remembers the value in the 
    # enclosing scope , even if they are not present in the memory

    # Say we delete the outer function , then
    del outerFunction
    # outerFunction("hello") # this will give an error 
    # since we have deleted the outer function , so we cannot call
    # the function

    # now let's call the inner function
    ## which is the python closure
    # now before deleting outerFunction , we have created a variable 'a'
    # which stores the function innerFunction
    # So , on calling a() 
    print(a())
    # it  executes innerFunction() even when the outerFunction 
    # is deleated 

    # Exmaple 2 
    def nth_power(exponent): 
        def pow_of(base): 
            return pow(base , exponent)
        
        return pow_of
    
    b = nth_power(2)
    # the 2 gets assigned to exponent
    print(b(12))
    # the 12 gets assigned to base 
    # returns the pow() 

    #deleting nth_power() 
    del nth_power
    # calling and printing b() 
    print(b(13))
    # now b variable here has the function pow_of() 
    # where exponent is already assigned = 2 
    # on passing 13 as an argument in b() 
    # 13 gets assigned to base 
    # returns the output

def func4() : 
    print("Inside function4() :  ")
    # Python Decorators 
    # Bakground 
    def messagewithWelcome(str) :
        # nested function
        def addWelcome() :
            return "Welcome to "
        
        # Return concantenation of addWelcome () 
        # and str 
        return addWelcome()  + str 
    
    # To get site name to switch welcome is added 
    def site ( site_name ): 
        return site_name
    
    print(messagewithWelcome(site("Disneyland")))

    def decorate_message(fun):

        # Nested Function
        def addWelcome(site_name ): 
            return "Welcome to " + fun(site_name)
        
        #Decorator returns a function
        return addWelcome
    
    @decorate_message
    def site(site_name): 
        return site_name
    
    #Driver code 
    # This call is equivalent to call to 
    # decorate_message () with function
    # site("India") as parameter 
    print(site("India"))

    #Exmaple 2 
    # A decorator function to attach data to function
    def attach_data(func) : 
        func.data = 3
        return func

    @attach_data
    def add(x,y) : 
        return x + y
    
    @attach_data
    def f() : 
        pass 
    
    # Driver Code 
    # This call is equivalent to attach_data() 
    # with add() as parameter 
    print(add(2,3))
    print(add.data)
    print(f.data)

def func5() : 
    print("Inside func5() :  ")
    # Decorators with syntax in python 
    def decorators ( *args , **kwargs ) :
        def inner(func): 
            '''
                do operations eith func
            '''
            return func 
        
        return inner # this is the function_object 
    
    @decorators()
    def func(): 
        '''
            function implementation
        '''

    def decorators_fun(func): 
        print("Inside Decorator")

        def inner(*args , **kwargs ): 
            print("Inside inner function")
            print("Decorated the function")
            # Do opeartions with func

            func() #Calls the func_to() function
                # Removing func() won't execute func_to() 
        return inner

    @decorators_fun
    def func_to(): 
        print("Inside the actual function")

    func_to() 

    # Another way 
    # Decorators with parameters in python
    print("Another way :\n")
    decorators_fun(func_to)() 

    # Example 3 
    print("\nAnother way_2 : \n")
    def decorator(*args, **kwargs ): 
        print("iside decorator ") 

        def inner (func) :
            # code functionaliy here 
            print("Inside the inner function")
            print("I like" , kwargs['like'])

            func() 
        # returning inner function
        return inner 
    
    @decorator(like = 'pineapple')
    def my_func() :
        print("Inside the actual function")

    print("\nAnother way_3 :\n")
    def decorator_func(x,y) :
        def inner(func): 
            def wrapper(*args  , **kwargs ):
                print("I like pineapples ")
                print("Summation of values : {}  " .format(x+y))
                
                func(*args , **kwargs )
            return wrapper 
        return inner
    
    # Not using decorator 
    def my_func(*args) : 
        for ele in args :
            print(ele)

    # Another way of using decorators 
    decorator_func(12,15)(my_func)('this ' , 'is ' , 'cool')

    print("\nExmaple :\n")

    def decorator(dataType , message1 , message2): 
        def decorator(fun): 
            print(message1)
            def wrapper(*args , **kwargs ):
                print(message2)
                if all([type(arg) == dataType for arg in args]) : 
                    return fun(*args , **kwargs)
                return "Invalid Input "
            return wrapper 
        return decorator
    
    @decorator(str , "Decorator for stringjon" , "StringJoin started ... ")
    def stringJoin(*args ): 
        st = '.'
        for i in args : 
            st += i
        return st 

    @decorator(int , "Decorator for summation\n" , "Summation Started ... " )
    def summation(*args ): 
        summ = 0
        for arg in args : 
            summ += arg
        return summ
    
    print(stringJoin("I" , "like" , "PineApple"))
    print() 
    print(summation(19,2,8,533,67,981,119))

def func6() :
    print("Inside func6()  : ")
    # Memoizatoin using decorators 
    def facto(num) :
        if num==1 : 
            return 1 
        else : 
            return num*facto(num-1)
    
    print(facto(5))
    print("\nUsing Decorators in the above code : ")
    #  A decorator function for function 'f' is passed 
    # as a parameter 
    def memoize_factorial(f) : 
        memory = {} 

        # This inner function has access to memory 
        # and 'f'
        def inner (num) : 
            if num not in memory : 
                memory[num] = f(num)
            return memory[num]
        return inner 
    
    @memoize_factorial
    def facto(num) :
        if num == 1 : 
            return 1 
        else : 
            return num * facto(num-1)
    
    print(facto(5))

def func7()  :
    print("Inside the func7() : ")
    help(print)
    # Dispplays the suer defned functions and cxlasses. The Docstring 
    # ( Documentation string ) is used ofr documentation.  

    class Helper : 
        def __init__(self):
            ''' The helper class is initialized '''
        def print_help( self ) : 
            ''' Returns the help description '''
            print("Helper description")
    
    help(Helper)
    help(Helper.print_help)

def func8() : 
    print("Inside func8() :\n")
    # Example 1 
    # IMporitng Numpy module
    a = np.array([1,2,3]) 

    # prints the type 
    print(type(a))
    # Prints the dataType of 'a'
    # DataType of a = class numpy.ndarray

    #Example 2 
    comp = complex

    arr = np.array

def func9(): 
    print("Inside func9() : ")
    # this creates a list of 0 to 5 
    # integers 
    demo= range(6)

    # print the demo
    print(demo)

    #it will gnerate error
    # print(next(demo))
    # Hence , python range () is not an iterator 
    demo = iter(range(6))
    print(demo)
    
    # use next 
    print(next(demo))
    # creates a deo range 
    demo = range(1,31,2)
    # print the range 
    print(demo)

    # print the start of range 
    print(demo.start)

    # print the step of range 
    print(demo.step)

    # print the index of element 23 
    print(demo.index(23))

    # since 30 is not present it will give error 
    #print(demo.index(30))





func1() 
func2() 
func3() 
func4() 
func5() 
func6() 
func7()
func8() 
func9()  