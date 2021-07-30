

def func1() : 
    print("Inside func() : ")
    #Subroutines , Coroutinesand threads 
    def print_name( prefix ): 
        print("Searching prefix: {} " .format(prefix))
        while True : 
            name = (yield)
            print("Prefix :  " , prefix)
            print("Name : " , name)
            if prefix in name  :
                print(name )
    # Calling coroutine, nothing will happen
    corou = print_name("Dear")

    #Ths will start execution of coroutine and 
    # Prints first line "Searching prefix ..."
    #and advance execution to the first yield expression
    corou.__next__()

    #sending inputs 
    print("First : \n")
    corou.send("Atul")
    print("Second : \n")
    corou.send("Dear Atul")
    print("Third : \n")
    corou.send("Dear linkin")

    # Execution of Coroutine 
    # Closing a coroutine 
    print("\nClosing a Coroutine :\n ")
    def print_name( prefix ): 
        print("Searching prefix: {} " .format(prefix))
        try : 
            while True : 
                name = (yield)
                print("Prefix :  " , prefix)
                print("Name : " , name)
                if prefix in name  :
                    print(name )
        except GeneratorExit : 
            print("Closing croutine!")

    corou = print_name('Dear')
    corou.__next__()
    corou.send("Atul")
    corou.send("Dear Atul")
    corou.close()

    #Chainging coroutines for creating a pipeline 
    print("Chaining Coroutines : \n")
    # Producer function , Pattern_filter function , Sink function

    def producer(sentence , next_coroutine) :
        '''
        Producer which just split strings and 
        feed it to pattern_filter cotouine 
        '''
        tokens = sentence.split(",")
        for token in tokens: 
            next_coroutine.send(token)
        next_coroutine.close()
    
    def pattern_filter(pattern="ing" , next_coroutine=None) : 
        '''
        Search for pattern in received token
        and if pettern got matched, send it to
        print_token() coroutine ofr printing 
        '''
        print("Searching for {} " .format(pattern))
        try : 
            while True: 
                token = (yield)
                if pattern in token :
                    next_coroutine.send(token)
        except GeneratorExit: 
            print("Done with filtering!")
    def print_token() : 
        '''
        Act as a sink, simply print the 
        received tokens 
        '''
        print("I'm sink, I'll print tokens")
        try : 
            while True : 
                token = (yield)
                print(token)
        except GeneratorExit : 
            print("Done with printing!")
    
    pt = print_token() 
    pt.__next__()
    pf = pattern_filter(next_coroutine = pt)
    pf.__next__()
    sentence = "Bob is running behind a fast moving car"
    producer(sentence, pf)

def func2() : 
    print("Inside func2() : ")
    # int.bit_leangth() 
    num = 7
    print(num.bit_length())
    num = -7
    print(num.bit_length())
    #int.to_bytes(length , byteorder, * , signed=False)
    # returns byte representation of 1024
    # in a big endian machine
    print((1024).to_bytes(2 , byteorder="big"))
    print((1024).to_bytes(2 , byteorder="little"))
    # Returns integer value of '\x00\x10' in big endian machine
    print(int.from_bytes(b'\x00\x10' , byteorder="big"))
    print(int.from_bytes(b'\x00\x10' , byteorder="little"))

def func3() : 
    print("Inside func3() : ")
    # Classes 
    class MyClass : 
        # assign the vlaues to the MyClass attributes 
        number =0
        name = "noname"
    def Main()  :
        # Creating n object  of hte MyClass.
        # Here , 'me' is the object 
        me = MyClass()

        #Accessing the attributes of MyClass 
        #using the dot(.) operator 
        me.number = 1337
        me.name = "Harshh"

        # str is an build-in function that
        # creates an string 
        print(me.name + " " + str(me.number))
    # telling python that there is main in the program
    if __name__ == '__main__' : 
        Main() 

    # Methods 
    class Vector2D: 
        x = 0.0
        y = 0.0

        #Creating a method named set 
        def Set(self, x , y): 
            self.x = x
            self.y = y
    def Main() : 
        #vec is an object of class Vector2D
        vec = Vector2D() 

        #Passing values to the funnction set 
        # by using dot(.) operator 
        vec.Set(5,6)
        print("X : " + str(vec.x) + " , Y : " + str(vec.y))
    if __name__ =='__main__': 
        Main() 

    # Inheritance 
    class Pet : 
        #__init__ is an contructor working of inheritance 
        def __init__(self , name , age ): 
            self.name = name 
            self.age = age 
    # Class Cat inheriting from the Class Pet 
    class Cat(Pet) : 
        def __init__(self , name , age): 
            # Calling the super-class function __init__ 
            # Using the super () function 
            super().__init__(name , age)
    def iMain() : 
        thePet = Pet("Pet" , 1)
        jess = Cat("Jess" ,3)

        #isinstance() function to check wheaater a class is 
        # inherited form another class 
        print("Is Jess a cat? " +str(isinstance(jess,Cat)))
        print("Is Jess a pet? " +str(isinstance(jess,Pet)))
        print("Is the Pet a cat? " +str(isinstance(thePet,Cat)))
        print("Is the Pet a pet? " +str(isinstance(thePet,Pet)))
        print(jess.name)


    if __name__ =='__main__': 
        iMain() 

    # iterators 
    class Reverse : 
        def __init__(self ,data): 
            self.data = data
            self.index = len(data)
        def __iter__(self) :
            return self 
        def __next__(self) :
            if self.index==0: 
                raise StopIteration
            self.index -= 1
            return self.data[self.index]
    
    def Main() : 
        rev = Reverse('Drapsicle')
        for char in rev: 
            print(char)
    
    if __name__ =='__main__' :
        Main()

def func4(): 
    # Generators 
    print("Generators :\n")
    def Reverse (data): 
        # This is like counting from 100 to 1 by taking one(-1)
        # step backward 
        for index in range(len(data)-1,-1,-1) : 
            yield data[index]
    def Main(): 
        rev = Reverse("Harshh")
        for char in rev : 
            print(char)
        data = "Harshh"
        print(list(data[i] for i in range(len(data)-1,-1,-1)))

    Main()
    # A simple example class 
    class Test : 
        # A sample Method 
        def fun(self) : 
            print("Hello")
    
    # Driver code 
    obj = Test() 
    obj.fun()

    # A Sample class with init method 
    class Person : 
        # init method or contructor 
        def __init__ (self , name): 
            self.name = name
        
        # Sample Method 
        def say_hi(self): 
            print("Hello , my name is " , self.name)
    p = Person("Atharva")
    p.say_hi()

    # Class and Variable instance 
    class CSStudent: 
        # Class Variable 
        stream = 'cse'

        # The init methd or constructor
        def __init__(self,roll) :
            # Instance Variable 
            self.roll = roll
    # Objects of CSStudent class 
    a = CSStudent(101)
    b = CSStudent(102)

    print(a.stream) # prints 'cse'
    print(b.stream) # prints 'cse'
    print(a.roll) # prints 101
    #Class variables can be accessed using Class 
    # name also
    print(CSStudent.stream) #pritns 'cse'

    # Creating an empty class 
    class Test: 
        pass 
    
    # Data Hinding 
    class MyClass : 
        # Hidden member of MyClass 
        __hiddenvariable = 0

        # A member method that changes 
        # _hiddenvariable 
        def add(self , increment ): 
            self.__hiddenvariable += increment 
            print(self.__hiddenvariable)
    
    # Driver Code 
    myObject = MyClass()
    myObject.add(2)
    myObject.add(5)

    #This line casuses error
    # print(myObject.__hiddenvariable)

    # Members can be accessed outside a class 
    class MyClass : 
        # Hidden member of MyClass
        __hiddenvariable = 10
    
    # Driver Code 
    myObject = MyClass() 
    # Accessing hideen variables 
    print(myObject._MyClass__hiddenvariable)

    # Printing Objects 
    class Test : 
        def __init__(self , a,b): 
            self.a = a
            self.b = b
        def __repr__(self) :
            return "Test a : %s b: %s " %(self.a,self.b)
        
        def __str__(self): 
            return "From str method of Test: a is %s," \
                "b is %s " %(self.a , self.b)
        
    # Driver Code 
    t = Test(1234,5678)
    print(t) # This calls __str__()
    print([t]) # This calls __repr__()

    # If no __str__ method is defined, print t(or print str(t))
    # uses __repr__ 

    class Test : 
        def __init__(self , a,b): 
            self.a = a
            self.b = b
        def __repr__ (self): 
            return "Test a : %s b: %s " %(self.a,self.b)
    # Driver Code 
    t = Test(1234,5678)
    print(t)


    # If no __repr__ method is used, then the default is used 
    class Test : 
        def __init__(self ,a,b): 
            self.a = a
            self.b = b
    # Driver Code 
    t = Test(1234,5678)
    print(t)


def func5() : 
    class Person ( object): 
        # Constructor 
        def __init__(self,name): 
            self.name = name 

        # To get name 
        def getName(self): 
            return self.name 
    
        # To check if this person is employee
        def isEmployee(self): 
            return False
    # Inherited or sub class ( Note Person in bracket ) 
    class Employee( Person): 
        # Here we return true 
        def isEmployee(self) :
            return True 
    # Driver Code 
    emp = Person("Geek1") # An Object of Person 
    print(emp.getName() , emp.isEmployee())

    emp = Employee("Geeks2") # An Object of Employee 
    print(emp.getName() , emp.isEmployee())

    # subclass of another 
    class Base(object): 
        pass # Empty class 
    class Derived( Base ): 
        pass # Empty Class 

    # Driver Code 
    print(issubclass(Derived,Base))
    print(issubclass(Base , Derived))

    d = Derived() 
    b = Base() 

    # b is not an instancce of Derived 
    print(isinstance( b , Derived))

    # But d is an instance of Base 
    print(isinstance(d , Base))

    # Object Class
    # Inheritance 
    class Base1(object ): 
        def __init__(self): 
            self.str1 = "Geek1"
            print("Base1")
    class Base2(object ): 
        def __init__(self): 
            self.str2 = "Geek2"
            print("Base2")
    
    class Derived(Base1 , Base2): 
        def __init__(self) :

            # Calling constructors of Base1
            # and Base2 classes 
            Base1.__init__(self)
            Base2.__init__(self)
            print("Derived")
        def printstrs(self) : 
            print(self.str1 , self.str2)
        
    ob = Derived() 
    ob.printstrs()

    # Accessing parent members in a subclass 
    # Class members can be acessed 
    # in derived class using base class name 
    class Base(object ): 
        # Constructor
        def __int__(self  , x): 
            self.x = x
    class Derived( Base): 
        # Constructor
        def __init__(self , x , y):
            Base.x = x
            self.y = y
        def printXY(self): 
            # Print(self.x , self.y) will also work
            print(Base.x , self.y)

    # Driver Code 
    d = Derived(10,20)
    d.printXY()

    # Using super() 
    # Accessing parent class using super() 
    class Base (object ): 
        # Constructor 
        def __init__(self,x): 
            self.x = x
            print("Inside Base")
    
    class Derived(Base) :
        # Constructor 
        def __init__(self , x, y): 
            '''
            In Python 3.x , super().__init__(name)
            also works 
            '''
            super(Derived,self).__init__(x)
            print("After super() :\n")
            self.y = y
        def printXY(self): 
            # Note that Base.x won't work here 
            # Because super() is used in constructor 
            print(self.x , self.y)
    
    # Driver Code 
    d = Derived(10,20)
    d.printXY()

    # Exmple : 
    class Base(object): 
        def __init__(self ,a): 
            self.num = a
        def double(self):
            self.num = self.num*2
    class Derived(Base) :
        def __init__(self ,a) :
            Base.__init__(self,a)
        def triple(self) : 
            self.num = self.num*3
    
    # Driver Code 
    d = Derived(4)
    print(d.num)
    d.double()
    print(d.num)
    d.triple()
    print(d.num)

    class Person(object ): 
        def __init__(self , name): 
            self.name = name 
        def getName(self): 
            return self.name 
        def isEmployee(self ): 
            return False
    class Employee(Person) :
        def __init__(self , name,id):
            '''
            Inheriting class Person'''
            Person.__init__(self,name )
            self.empID=id
        def isEmployee(self): 
            return True 
        def getID(self ): 
            return self.empID
    
    # Driver Code 
    emp = Employee("atharva" , "123")
    print(emp.getName() , emp.isEmployee() , emp.getID())

def func6() : 
    print("Inside func6() : ")
    # Ploymorphism
    # Same function name , but different signatures ( arguments )

    # Morphic Functions 
    # len() being used for a string 
    print(len("atharva"))
    
    # len() used ofr a list 
    print(len([1,2,3]))

    # Polymorphism
    def add(x,y,z=0): 
        return x+y+z
    
    # Driver Code 
    print(add(2,3)) # Executes the in-built function by python
    print(add(1,2,3)) # Executes the function made by me 

    # Polymorphism with class methods 
    class India() : 
        def capital(self) :
            print("Delhi")
        def language(self): 
            print("Hindi")
        def type(self): 
            print("Developing ")
    class USA (): 
        def capital(self): 
            print("Washington DC")
        def language(self) :
            print("English")
        def type(self): 
            print("Developed")
    
    obj_ind = India() 
    obj_USA = USA()
    for country in (obj_ind , obj_USA): 
        country.capital() 
        country.language()
        country.type()

    # Polymorphism with Inheritance 
    # Where the Derived class method has the same name as the 
    # Base class method
    class Bird: 
        def intro(self):
            print("There are many types of birds ")
        def flight(self ): 
            print("Most of the bords can fly but some cannot ")
    class Sparrow(Bird) : 
        def flight(self) :
            print("Sparrows can fly")
    
    class Ostrich(Bird) :
        def flight(self): 
            print("Ostrich cannot fly")
        
    obj_bird = Bird() 
    obj_sparrow = Sparrow()
    obj_ostrich = Ostrich() 
    obj_bird.intro() 
    obj_bird.flight()

    obj_sparrow.intro() 
    obj_sparrow.flight()

    obj_ostrich.intro() 
    obj_ostrich.flight()

    # Polymorphism with a Function and objects 
    def func(obj): 
        obj.capital() 
        obj.language()
        obj.type() 
    obj_ind = India() 
    obj_USA = USA()

    func(obj_ind)
    func(obj_USA)

    # Implementing polymorphosm with a function

def func7() :
    print("Inside func7() : ")
    # Python program to show that the variables with a value 
    # assigned in class decleration, are class variables 
    # Class for Computer Science Student 
    class CSStudent: 
        stream = 'cse'
        def __init__(self, name , rollno) :
            self.name = name 
            self.rollno = rollno
    
    # Objects of CSStudent class 
    a = CSStudent('atharva' , 1)
    b = CSStudent('brother' , 2)
    print(a.stream) # prints cse 
    print(b.stream) # prints cse 
    print(a.name) # prints 'atharva'
    print(b.name) # prints 'brother'
    print(a.rollno) # prints 1
    print(b.rollno) # prints 2 

    # Class variables can be accessed using Class 
    # name also 
    print(CSStudent.stream) # prints 'cse'

    # Now if we change the stream for just a it
    # won't be changed for b 
    a.stream = 'ece'
    print(a.stream) # prints 'ece'
    print(b.stream) # prints 'cse'

    # To change the stream for all instances of hte class we 
    # can change it 
    # directly from  the class 
    CSStudent.stream ='mech'

    print(a.stream) # prints mech 
    print(b.stream) # prints mech

    # Constructors 
    class Name: 
        # Default Constructor
        def __init__(self) : 
            self.geek = 'atharva'
        
        # A method for printing data members 
        def print_geek(self ) : 
            print(self.geek)
    
    # Creating an object of the class 
    obj = Name() 
    obj.print_geek()

    # Example of Parameterised Contructor
    class Addition : 
        first,second,answer=0,0,0
        # Parameterized Constructor 
        def __init__(self , f,  s): 
            self.first = f
            self.second = s 

        def display(self): 
            print("First number :  "  + str(self.first))
            print("Second number :  "  + str(self.second))
            print("Addition :  " + str(self.answer))
        def Calculate ( self ): 
            self.answer= self.first + self.second
    
    # Creating object of the class 
    # This will invoke parameterized Constructor 
    obj = Addition(2,3)
    #perform addition
    obj.Calculate() 
    # Display Result 
    obj.display()

    # Destructors 
    # Python program for destructor
    class Persona: 
        #Initializing 
        def __init__(self): 
            print("Employee Created")
        
        # Deleting ( Calling destructor)
        def __del__(self) :
            print("Destructor called , Employee deleted")
        
    obj = Persona()
    del obj

    # Python program to illustrate destructor 
    class Employee: 
        # Initalizing 
        def __init__(self) :
            print("Employee Created")
        def __del__(self): 
            print("Destructor called")
    
    def Create_obj() : 
        print("Marking obj...")
        obj = Employee()
        print("function end...")
        return obj
    
    print("Calling create_obj() function ...")
    obj = Create_obj() 
    print("Program end ...")

    # Python porgram fto illustrate destructor 
    class A : 
        def __init__(self,bb): 
            self.b = bb
        
        def __del__(self ): 
            print("class A destructor called")
    
    class B: 
        def __init__(self): 
            self.a = A(self)
        def __del__(self ): 
            print("class B destructor Called ")
    
    def fun() :
        b = B() 
    
    fun() 
    



func1()
func2() 
func3() 
func4()
func5() 
func6() 
func7()

