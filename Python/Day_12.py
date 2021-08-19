


def f1() :
    # python bit_length 
    # int.bit_length() 
    a = 7 
    print(int.bit_length(a))
    b = -3 
    print(int.bit_length(b))

    # printing the bit_length in string 
    #print(str.bit_length(a))
    #print(str.bit_length(b))
    c = -7 
    print(int.bit_length(c))

    # int.to_bytes(length, byteorder , * , signed = False ) 
    print((1024).to_bytes(2,byteorder = 'big'))
    print((1024).to_bytes(2,byteorder = 'little'))

    # int.from_bytes(bytes , byteorder , * , signed = False)
    print(int.from_bytes(b'\x00\x10' , byteorder = 'big'))

def f2()  :
    # Classes 
    class MyClass : 
        # aassign the values to the MyClass attribtes 
        number = 0 
        name = 'noname'
    
    def main()  :
        # cteating an object to hte mYcLASS 
        # Here, 'me' is the object 
        me = MyClass() 

        # Accessing the attributes in the function that 
        # using the dot(.) operator 
        me.number = 1337
        me.name = 'atharva'

        # str is an built - in function that 
        # creates string 
        print(me.name + " "+ str(me.number))
    # telling pytohn that there is a main in the program 
    if __name__ =='__main__' :
        main() 
    
    # Methods 
    class MyName : 
        name = 'atharva'
        number = 213
        
        def set (self, name , number): 
            self.a = name 
            self.b = number 
    
    def printing(): 
        object = MyName( )
        # Passing values to the object variables 
        # by using ht edot operator 
        object.set('atharva' , 999)
        print("name : ",  str(object.name) + " Number : " + str(object.number))
    
    # Driver Code 
    # Calling printing () function 
    printing()

    # Inheritance 
    class printing2: 
        name = 'aditya'
        def out(name): 
            return name 
    
    def other_main()  :
        obj = printing2() 
        print(obj.out())
    
    other_main()

    class pet : 
        # __init__
        def __init__( self, name , age ): 
            self.name = name 
            self.age = age 
    
    # class cat inheriting from pet class 
    class cat ( pet ): 
        # __init__ 
        def __init__ ( self, name , age ): 
            # Calling the super - class function __init__
            # using the super() function 
            super().__init__(name , age)
    
    def main2()  :
        thepet = pet('tom' , 2) 
        thecat = cat('billi' , 3)

        # isinstance() function to check wheater a class is a 
        # inherited form another class 
        print("is thecat a cat? " + str(isinstance(thecat , cat)))
        print("is thecat a pet ? " + str(isinstance(thecat, pet)))
        print("is thepet a cat ? " + str(isinstance(thepet, cat)))
        print("is thepet a pet ? " + str(isinstance(thepet, pet)))
        print("name is the cat is " , thecat.name )
    
    # Driver Code 
    # calling the main2() function 
    main2()

    # iterators 
    class Reverse : 
        def __init__(self, string): 
            self.string = string 
            self.index = len(string)
        def __iter__(self): 
            return self
        def __next__(self): 
            if self.index==0: 
                raise StopIteration
            self.index = self.index -1 
            return self.string[self.index]

    def main3() : 
        reverse = Reverse('atharva')
        for char in reverse : 
            print(char)
    
    # Driver Code 
    # Calling main3() 
    main3() 

    # program to add 2 strings 
    # and then reversing the new string formed 
    class Reverse: 
        def __init__(self, string1, string2): 
            self.string1 = string1
            self.string2 = string2
            self.index = len(self.string1+self.string2)
        def adding(self): 
            return self.string1+self.string2
        def __iter__(self): 
            return self
        def __next__(self): 
            if self.index==0: 
                raise StopIteration 
            self.index = self.index -1 
            return (self.adding())[self.index]
    
    def main4() : 
        reverse = Reverse('atharva' , 'aditya')
        print("Combined string : " , reverse.adding())
        for char in reverse : 
            print(char , end=" ")
        print()
    
    # Driveer Code 
    # calling main4() 
    main4() 

    # Generators 
    def reverse (string): 
        for char in range(len(string)-1,-1,-1): 
            yield string[char]
    
    def main5() : 
        rev = reverse('pacific Rim')
        for char in rev : 
            print(char , end=" ")
        
        print()
        string = 'pokemon'
        print("Reverse : ")
        print(list(string[char]) for char in range(len(string)-1,-1,-1))

    # Driver Code 
    # Calling main5() function 
    main5() 

def f3()  :
    # Object Oriented programming in python
    class Test : 
        # A sample method 
        def fun(self ): 
            print("Hello")
    
    # Driver Code 
    obj = Test()
    obj.fun()

    # class person 
    class person : 
        # init method or constructor 
        def __init__(self , name): 
            self.name = name 
        
        # Sample method 
        def hi(self): 
            print(self.name)
    
    p = person('hi')
    p.hi()

    # class and instance variables ( or attributes )
    # self.name = instance varibles 
    # variables whose values are assigned inside a constructor 
    class student : 
        # class variable 
        stream = 'CSE'

        # the init method 
        def __init__(self , roll): 
            # instance varible 
            self.roll = roll
    
    # objects of studnet class 
    a = student(12)
    b = student(13)
    print(a.stream)
    print(b.stream)
    print(a.roll)
    print(b.roll)
    print(student.stream)

    # empty class 
    class Test : 
        pass 


def f4() : 
    # Data hiding and object printing 
    class myclass : 
        # hidden variable 
        _hvar = 12 
        def add( self, increment): 
            self._hvar  = self._hvar+ increment  
            print(self._hvar)
    
    # Driver Code 
    a = myclass()
    print(a.add(2))
    print(a.add(3))

    # accessig a hidden variable
    print("value of hvar : " , end=" ") 
    print(a._hvar)

    # pritig ojects 
    # using __str__ and __repr__ 

    class Test : 
        def __init__(self, a,b ): 
            self.a = a 
            self.b = b 
        def __repr__(self ): 
            return "Test a:%s b:%s " %(self.a , self.b)
        
        def __str__(self): 
            return "from str method of test : a is %s,"\
                    "b is %s " %(self.a , self.b)
    
    # Driver Code 
    t = Test(1234,5678)
    print(t) # this calls the __str__()
    print([t]) # this calls the __repr__()

    # if no __str__ is defined , then 
    # python uses __repr__

    # if no __repr__ is used 
    # then default is used 

def f5() :
    # Inheritance , exmaples of object 
    # issubclass and super 
    
    class person (object): 
        # constructor 
        def __init__(self , name ): 
            self.name = name 
        
        # to get name 
        def getname(self): 
            return self.name 
        
        # to check if this person is employee 
        def isemployee(self) :
            return False 
        
    # inherited or subclass (Note person in bracket )
    class employee(person): 
        # here we return true 
        def isemployee(self): 
            return True 
    
    # Driver Code 
    emp = person('batman') # an object of person 
    print(emp.getname() , emp.isemployee())

    emp = employee ('batwoman') # an object of employee 
    print(emp.getname() , emp.isemployee())

    # how to check if subclass or not 
    # issubclass() 
    class Base (object ) :
        pass 

    class derived(Base ):
        pass 

    a = Base() 
    b = derived() 
    print(issubclass(derived ,Base))
    print(issubclass(Base ,derived))

    print(isinstance(a,derived))
    print(isinstance(b,Base))

    # accessing parent members in subclass 

    class base(object): 
        # constructor 
        def __init__(self,x): 
            self.x = x 
    
    class derived(base): 
        # constructor 
        def __init__(self, x,y ): 
            base.x = x 
            self.x = x 
            self.y = y 
        
        def printxy(self): 
            # prints values 
            print(base.x , self.x + 5 , self.y)
    
    # Driver Code 
    d = derived(10,20)
    d.printxy()

    # using super() 
    class base(object ): 
        # constructor 
        def __init__(self,x): 
            self.x = 15
    
    class derived(base): 
        # constructor 
        def __init__(self , x,y ): 
            '''
            docstrings 
            '''
            super(derived,self).__init__(x)
            self.x = x 
            self.y = y 
        
        def printxy(self ): 
            # note that base.x won't work here 
            # because super() is used in constructor 
            print(self.x , self.y , self.x+2)
    
    # Driver Code 
    a = derived(11,11)
    a.printxy()

def f6() : 
    # polymorphim in python 
    print(len('atharva'))

    print(len(range(5)))
    def add(x,y,z=1): 
        return x , y+z 
    
    # Driver Code 
    print(add(2,3))
    print(add(1,2))
    print(add(1,2,3))

    # polymorphism

    class india(): 
        def capital (self ): 
            print("New Delhi")
        
        def language (self ): 
            print("hindi")
        
        def type(self ): 
            print("developing ")
    
    class usa (): 
        def capital(self ): 
            print("washington DC ")
        def language(self): 
            print("English")
        def type(self): 
            print("developed")
    
    a=  india()
    b = usa() 
    for country in (a,b): 
        print(country.capital() , country.language() , country.type())
        print()

    # polymorphism with inheritance 
    class bird: 
        def intro(self): 
            print("there are many types of birds ")
        
        def flight(self): 
            print("most birds can fly but some cannot ")
        
    class sparrow(bird):
        def flight(self): 
            print("sparrows can fly")
    
    class ostrich(bird): 
        def flight(self): 
            print("ostrich can't fly")
    
    # Driver Code 
    a = bird() 
    b = sparrow()
    c = ostrich()

    a.intro()
    a.flight()
    b.flight()
    c.flight()
    b.intro()
    c.intro()

def f7() : 
    # class or static varialbes in python 
    class student : 
        stream = 'CSE '

        def __init__(self , name , roll ): 
            self.name = name 
            self.roll = roll 
        
    # objects of student 
    a = student('atharva' , 1)
    b = student('aditya' , 2)
    print(a.name)
    print(a.roll)
    print(b.name)
    print(b.roll)

    # class variables can be accessed during class 
    # name also
    print(student.stream) 

    # Now if we change the stream for just a it won't be changed 
    a.stream = 'ece'
    print(a.stream)
    print(b.stream)

    student.stream = 'mechanical'
    print(a.stream)
    print(b.stream)

def f8() :
    # changing class members in python

    class student :
        stream = 'CSE'
        def __init__(self, name , roll): 
            self.name = name 
            self.roll = roll 
    
    # Driver program to tets the functionality 
    # creating objects of students class 
    a = student('atharva', 1)
    b = student('aditya' , 2)

    print("Initially ")
    print("a.stream = " , a.stream)
    print("b.stream : " , b.stream )

    # this thing dosne't change class(static) variable 
    # instead creates instance variable for the object 
    # 'a' that shadows class member 

    a.stream = 'ece'

    print("After changing a.stream : ")
    print("a.stream : " , a.stream)
    print("b.stream : ",  b.stream)

def f9() :
    # constuctors in python 

    class geeksforgeeks : 
        # default constuctor 
        def __init__(self): 
            self.geek = 'geeksforgeeks'
        
        # a method for printing data memebers 
        def print_geek(self): 
            print(self.geek)
    
    # creating object of the class 
    obj = geeksforgeeks() 

    # calling the instance method using the object ob j
    obj.print_geek()

    class addition : 
        first =0 
        second =0 
        third =0 

        # parameterized constuctors 
        def __init__(self, f,s ): 
            self.first = f 
            self.second = s 
        def display(self) :
            print("first number : " + str(self.first) )
            print("second numer : " +str(self.second))
            print("addition of two numbers :  " + str(self.answer))
        
        def calculate(self): 
            self.answer = self.first + self.second 
    
    # creating object of the class 
    a = addition(100 , 200)

    # perform addition 
    a.calculate()

    # display 
    a.display()


    class number2 : 
        def __init__(self, number ): 
            self.number = number 
        
        def add(self): 
            print("adds 5 : " , self.number+5 )
    
    # Driver Code 
    b = number2(3)
    b.add()

    
def f10() :
    # destructors in python 
    # using __del__() 

    class person : 
        # initializing 
        def __init__(self ): 
            print("person created ")
        
        # deleating ( calling destructor )
        def __del__(self ): 
            print("Calling destructor ")
    
    def create_object () :
        print("making oejct : ")
        a = person()
        print("function end ")
        return a 
    
    print("calling create_object () function : ")
    b = create_object() 
    print("program ends ")
    class A : 
        def __init__(self , bb): 
            self.b = bb 
        
    class B : 
        def __init__(self): 
            self.a = A(self)
        
        def __del__(self ): 
            print("die")
    
    def fun(): 
        b = B() 
    
    fun()



def f11() :
    # first class functions 

    def shout(text): 
        return text.upper() 
    
    print(shout('atharva'))

    yell = shout
    print(yell('aditya'))

    def shout(string) : 
        return string.upper() 

    def whisper(string): 
        return string.lower() 
    
    def greet(func): 
        #storing the function in a variable 
        greeting = func("""Hi, I am created by a function
                    passed as an argument.""")
        print(greeting)
    
    greet(shout)
    greet(whisper)

    def create_adder(x): 
        def adder(y) :
            return x+y 
        
        return adder 
    
    add_15 = create_adder(15)
    print(add_15(10))


def f12(): 
    # metaprogramming with metaclasse sin python 
    num =13 
    print("type of number : "  , type(num))
    list = [1,2,3]
    print("tpype of list : " , type(list))

    name = 'athava'
    print("type of string : " , type(name))

    # eert type n python defined by class 
    class student : 
        pass 
    a= student() 
    print(type(a))

    class studnet : 
        pass 

    # prints type of studnet class 
    print("type of studnet class is : " , type(studnet ))

    class test : pass 

    # defining method varialbes 
    test.x = 45 
    test.foo = lambda self : print("hello")

    # creating object 
    c = test() 
    print(c.x)
    c.foo()
    
    # creating metaclasses 
    # using __new__ () 
    # and __init__() 

    def test_method(self): 
        print("this is test class method")
    
    # creating a base class 
    class base : 
        def myfun(self): 
            print("this is inherited method ! ")
        
    # creaitng test class dynamically using 
    # type() methid directly 
    test = type('test' , (base,), dict(x='atharva' , my_method=test_method))

    # print tpe of test 
    print("type of test class : " , type(test))

    # creating instance of test class 
    test_obj = test() 
    print("type of test obj : " , type(test_obj))
    # calling inherited method
    test_obj.myfun()
 
    # calling Test class method
    test_obj.my_method()
 
    # printing variable
    print(test_obj.x)


def f13(): 
    # python exceptional handling 
    amount = 1000
    # check that you are eligiblie to 
    # purchase ..
    if (amount>2999): 
        print("yes")

    a = [1,2,3]
    try : 
        print("second elemnet : %d " %(a[1]))
        # throws error since three are only elements of the list 
        print("fourth element : %d " %(a[3]))
    except : 
        print("an error occured")

    #catching specific exception 
    def fin(a): 
        if a<4: 
            # throws ZeroDIVISIONError for a=3 
            b = a/(a-3)
        
        # throws NameError if a>=4
        print("Value of b : " , b)
    
    try : 
        fin(3)
        fin(5)
    
    # note that braces() are necessary here 
    except ZeroDivisionError: 
        print("ZeroDivision Error")
    except NameError:
        print("Name Error")

    # commeting line fin(3)
    # will give Name Error

    # try with else cause 
    print("experimenting try-else : ")
    def abc(a,b): 
        try : 
            c = ((a+b)/(a-b))
        except ZeroDivisionError :
            print("a/b result in 0")
        else : 
            print(c)
    
    # Driver program to test above function 
    abc(2.0 , 3.0)
    abc(3.0 , 3.0)

    # finally keyword in python
    print("\nTesting finally keyword : ")
    try : 
        k = 5//0 # raises ZeroDivisionError
    
    except ZeroDivisionError: 
        print("Cannot divide by zero")
    
    finally : 
        # this block is always executed 
        # regardless of exception generation 
        print("this is always executed")


    # raising exception 
    '''
    print("\nTesting raising exception : ")
    try : 
        raise NameError('hi there') # raise error 
    except NameError: 
        print("an exception")
        raise  # to determine wheather the exception was raised nr not 
    '''

def f14() : 
    # Usere - defined exceptions in python 
    class myerror(Exception): 
        # constructor or initializer 
        def __init__(self , value ): 
            self.value = value 

        # __str__ is to print() the value 
        def __str__(self ): 
            return(repr(self.value))
    
    try : 
        raise (myerror(3*2))
    
    # value of exception is stored in error
    except myerror as error : 
        print("a new exception occured : ", error.value)

    # knowing all exception class 
    #help(Exception)

    # deriving error from super class exception 

    # class erorr is derived from super class exception
    class error(Exception):  # BASE CLASS 
        pass 
    

    class derived(error): 
        # raised when an operation attempts a state 
        # transition that's not allowed 
        def __init__(self, a , b , msg ): 
            self.a = a 
            self.bb = b
            self.msg = msg 
    try : 
        raise (derived(2,3*2,'not allowed'))
    except derived as d: 
        print("Exception occured : " , d.msg)
    
    # exceptions as a base class 
    # runtime error 

    class networkingerror(RuntimeError): 
        def __init__(self, arg): 
            self.args = arg 
    
    try : 
        raise networkingerror('error')
    except networkingerror as network :
        print("Exception :  " , network.args)

    

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