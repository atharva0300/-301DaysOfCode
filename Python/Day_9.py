

def f1() : 
    # Arrays 
    print("Arrays : ")
    import array as arr
    # creatig array 
    a = arr.array('i' , [1,2,3])

    # pritnting original array 
    print("Array : " , a)

    # pritning oroiginal array 
    for i in range(0,3): 
        print(a[i] , end=" ")
    
    print()
    print(a[0])
    # creating an array with float type 
    b = arr.array('d'  , [2.5,3.2,3.3])
    print("Array 2 : " , b)
    # printing original array 
    for i in range(0,3 ): 
        print(b[i] , end=" ")
    print()

    # adding elements to the array 
    # usng insert() 
    a.insert(1,4)
    # inserts 4 at 1st position ( index ) 
    print("Array after insertion : " , a)

    a.append(12)
    # adds 12 to the last 
    print("Array after ising append: " , a)

    # accessing elemnets from an array 
    print("element 0 : " , a[0])
    print("element 1 : " , a[1])
    print("element 2 : " , a[2])

    # removing elements from an array 
    # using remove () 
    print("Array before remove() operation : " , a)
    a.remove(4)
    # remves element 4 form the array 
    print("Array after removing element : " , a)
    # using pop()
    a.pop(2)
    # removes the 2nd element from the array
    print("Array after pop: " , a)

    # slicing an array 
    l = [1,2,3,4,5,6,7,8,9,10]
    a = arr.array('i' , l)
    print("Array : " , a)
    # slicing operaitons 
    sliced_array = a[3:8]
    print("Sliced_array : " , sliced_array)

    # searching element in an array 
    for i in a: 
        if i==3: 
            print("Element found")
            break
    print("Array : " , a)
    print(a.index(3))
    # updating elements in an array 
    for i in range(len(a)): 
        if a[i]==2:
            a[i]=0
            break
    print("Array after updation : " , a)

def f2() : 
    # maximum possible value of an integer 
    # large numbers in pytohn 
    x = 1000000000000000000000000000000000000000000000000
    x = x+1 
    print(x)
    print(type(x))

def f3():
    # global and local variables 
    def f () :
        print(s)
        # s is not inside the function f() 
        # but still it can access 
        # this is called global scope
    
    # global scope 
    s = 'atharvapingale '
    f() 
    def f(): 
        s = 'Me too'
        print(s)
        # prints 'Me too'
        # local variable precedence is higher than 
        # precedence of global variable 

    
    s = 'atharvapingale '
    f() 
    print(s) # prints 'atharvapingale' as 
            # s is in global scope 
    print("fourth : ")
    def f(): 
        global t
        t = 'Me too'
        print(t)
        # prints 'Me too'
        # local variable precedence is higher than 
        # precedence of global variable 

    # global scope 
    t = 'atharvapingale '
    f() 
    print(t)

    def f()  :
        print("Inside f() : " , a)
    
    # Variable 'a' is reduced as a local 
    a=1
    def g(): 
        a = 2
        print("Inside g() : " , a)
    
    print(a)
    g() 

def f4() : 
    # packing and unpacking arguments in python 
    def fun(a,b,c,d) :
        print(a,b,c,d)
    
    # Driver Code 
    my_list = [1,2,3,4]

    # this doesent work 
    #fun(my_list)
    
    # un[acking should be done 
    # # using '*' operator 

    fun(*my_list)

    # error when len(args)!=number of actual arguments 
    # required by the function
    print(range(3,6))
    args = range(3,6)
    print(*args) # unpacking args 
    
    # packing 
    def mysum(*args): 
        return sum(args)
    
    # driver code 
    print(mysum(1,2,3,4,5))
    print(mysum(10,20))

    # packing and in unpacking 
    def fun(a,b,c): 
        print(a,b,c)
    
    # A Call with unpacking of dictionary 
    d = {'a':2 , 'b':4, 'c':10}
    fun(**d)
    # unpacking dictionary 
    # should be done using 
    # ' ** ' operator 

    # packing dictionary 
    def fun(**kwargs) :
        # kwargs is a dict 
        print(type(kwargs))
        
        # printing kwargs 
        for key in kwargs: 
            print("%s = %s" %(key , kwargs[key]))
    
    # driver code 
    fun(name = 'atharva' , sname= 'pingale' , number=3)

def f5() : 
    # type conversion in python
    # implicit type conversion
    x = 10
    print("x is of type : " , type(x))
    y = 10.5
    print("y is of type : " , type(y))
    # explicit type conversion 
    # initializing string 
    s = '1000'
    # printing string conversion to int base 2 
    c = int(s)
    print(c)
    print("float :" , float(s))

    # ord() 
    # converts character to integer 
    s = '4'
    # converts the string character to integer 
    print("ord() : " , ord(s))

    # hex() 
    # converts the number to hexadecimal 
    # equivalent 
    print("hex() : " , hex(100))
    print("hex() : " , hex(int(s)))

    # oct() 
    # converts integer to octal 
    # euivalent 
    print("oct() : " , oct(int(s)))
    
    # tuple 
    # converts to tuple 
    s = '4'
    print(tuple(s))

    # set() 
    # converts to set 
    print(set(s))

    # list() 
    # converts to list 
    print(list(s))

    # dict() 
    # converts to dictionary 
    tup = ((1,'atharva') ,(2,'pingale'))
    print(tup)
    print(dict(tup))

    # complex( )
    # converts to a complex number 
    c = complex(1,2)
    print(c)

    # str()
    # converts to a string 
    print(str(42))

    # chr() 
    # converts number to its corresponding ASCII 
    # acharacter 
    print(chr(10))
    print(chr(76))
    print(chr(48))

def f6(): 
    # byte ojects vs string python 
    # initializing a string 
    a='atharvapingale'

    # initializing a byte object 
    c = b'atharvapingale'

    # using encode() to encode the string 
    # encoded version of a is stored in d 
    # using ASCII mapping 
    d = a.encode('ASCII')
    print("Printing values : " ,a)
    print(c,"\n" ,d)

    # checking if a is a converted to bytes or not 
    if( d==c) :
        print("Encoding Successful")
    else: 
        print("Encoding unsuccessful")
    
    # decoding 
    # using decode() 
    # convertss byte objet to string 

    e = d.decode('ASCII')
    print("e : " , e)
    f = c.decode('ASCII')
    print("f : " ,f)

def f7() :
    # equivalent codes in python 
    # procedure same output 
    # code 1 
    print(1)

    # code 2 
    print((1))

    # priting multiple values 
    # code 1 

def f8() :
    # private variables 
    # python code to illistrate how mangling works 

    class Map : 
        def __init__( self , iterate ): 
            self.list = []
            self.__geek(iterate )
        def geek(self , iterate ): 
            for item in iterate : 
                self.list.append(item)
        
        # private copy of original geek() method 
        __geek = geek
    class MapSubclass(Map) :
        # privides new signature for geek() but 
        # does not braek __init__() 
        def geek(self, keys, value ): 
            for i in zip(keys , value): 
                self.list.append(i)
    
    #python code to illustrate 
    # how single underscore works
    def _get_errors(self) :
        if self._errors is None : 
            self.full_clean() 
        return self._errors 

    errors = property(_get_errors) 
    print("errors :   " , errors)

    






#f1() 
#f2() 
#f3()
#f4()
#f5()
#f6()
#f7()
f8()   