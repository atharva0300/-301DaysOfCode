from __future__ import print_function

def f1() : 
    # There is no main() function in python
    # the interpreter, starts at level 0
    # indentation is to be executed
    # before doung that, it will craete some special variables 
    # such as __name__.
    # if the source file is executed as the main program, the itrepreter 
    # sets the __name__ module to have a value 
    # __main__. 
    # if ther file is being imported form another modfule,
    # __name__ will be sret to the module's name 

    print("Atharva here ")
    if __name__ =="__main__" :
        print("File1 is being run directly")
    else : 
        print("File1 is being imported")
    
    import file2 as f

    f.func() 
    if __name__ =="__main__" :
        print("File1 is being run directly")
    else : 
        print("File1 is being imported")

def f2() : 
    # Basic Operators in Python
    # Examples of Arithmatic Operators 
    a=9
    b=4
    print("Summation : " ,a+b )
    print("Subtraction : " , a-b)
    print("Division :  " , a/b)
    print("Mutiplication : " , a*b)
    print("Floor division : " , a//b)
    print("Power : " , a**b)
    print("Modulo : " ,  a%b)

    # Relational Operators 
    print("Greater than : " , a>b)
    print("Less than : " , a<b)
    print("Equal to : "  , a==b)
    print("Not equal to : " , a!=b)
    print("Greater than or equal to : " , a>=b)
    print("Less than or equal to : " , a<=b)

    # Logical Operators 
    print("And : " , a and b )
    print("Or : " , a or b)
    print("Not b :  " , not b )
    print("Not a : " , not a )

    a = True 
    b = False 
    print("And : " , a and b )
    print("Or : " , a or b)
    print("Not b :  " , not b )
    print("Not a : " , not a )

    # Bitwise Operators 
    a =  10
    b = 4 
    print("Bitwise operators \n\n")
    print("Binary of a : ",  bin(a))
    print("Binary of b : " , bin(b))
    print("a and b  :" , a &b)
    print("a or b : " , a | b) 
    print("not a : " , ~a , "and its binary : " , bin(~a))
    print("Not b : " , ~b)
    print("a XOR b : " , a ^ b )
    print("Bitwise right shift : "  , a>>2)
    print("Bitwise left shift : " ,a<<2)

    # Assignment Operators 
    # Special Operators 
    a1 = 3
    b1 = 3
    a2 = 'GeeksforGeeks'
    b2 = 'atharva'
    a3 = [1,2,3]
    b3 = [1,2,3]
    print("a1 is not b1 : " , a1 is not b1 )
    print("a2 is b2 : ",  a2 is b2)
    print(a3 is b3) # Output is false 
    # Since lists are mutable 
    a3 = (1,2,3)
    b3 = (1,2,3)
    print(a3 is b3) # Output is True 
    # Since sets are immutable 

    # Membership Operators 
    # Examples of Membership Operators 
    x = 'GeeksforGeeks'
    y = {3:'a' , 4:'b'}
    print("Membership Operatos : ")
    print('G' in x )
    print('geeks' not in x )
    print("Geeks" not in x)
    print(3 in y )
    print('b' in y)
    print('b' in y[4])

    # Precedence and Associativity of Operators 
    print("Operator precendence : ")
    expr = 10+20*30
    print(expr)

    # Precedence of 'or' & 'and'
    name = "Atharva"
    age = 12

    if name=="Atharva" or name=="Pingale" and age>=2: 
        print("Hello welcome ")
    else :
        print("Goodbye! ") 

    # Operators Associativity 
    print("Operator Associativity : ")
    # left-right associatiity 
    # 100/10 *10 is calclated as 
    # (100/10) *10 and not 
    # as 100/(10*10)
    print(100/10*10)

    # Left -right associativity 
    # 5-2 + 3 is calculated as
    # (5-2) + 3 and not 
    # as 5 - (2+3)
    print(5-2+3)

    # right - left associativity 
    # 2**3**2 is calcualted as 
    # 2** (3**2) and not 
    # as (2**3)**2
    print(2**3**2)

def f3(): 
    # Ternary Operators 
    print("Ternary Operators: ")
    a,b = 10,20

    # Copy value of a in min if a<b else copy b 
    min = a if a<b else b
    print(min)

    a,b = 10,20

    # Use tuple for selecting an item 
    # ( if_test_false , if_test_true)[test]
    print((b,a)[a<b])

    # Use dictionary to select items
    # if [a<b] is true then value of True key will print 
    # elif [a<b] is false then value of False key will print
    print({True: a , False: b} [a<b])
    print({True: a , False: b} [a>b])

    # Lambda expressions
    print((lambda:b , lambda:a) [a<b] ())
    print((lambda:b , lambda:a) [a>b] ())

    # Ternary Operator wirten as nested if-else 
    a,b = 10,20
    print("Both a and b are equal " if a==b else "a is greater than b" 
        if a>b else "b is greater than a")

    a,b = 10,20
    if a!=b: 
        if a>b: 
            print("a is greater then b ")
        else :
            print("b is greater than a")
    else : 
        print("Both a and b are equal")
    
    # Conditional Operator 
    a,b = 10,20

    # If a is less than b, then a is assigned 
    # else b is assgned ( note : it dosen't
    #  work if a is 0 )
    print(a or b)
    min = a<b and a or b
    print(min)
    min = a>b and a or b
    print(min)


def f4() : 
    # Division Operator in Python
    print(5//2)
    print(-5//2)
    print(-5.0/2)
    print(-5.0/2)
    print(5.0//2)
    print(-5.0//2)

def f5(): 
    # Operator Overloading in Python
    # Operator overloading means giving extended 
    # meaning beyond their predefined 
    # Operaional meaning 

    print(1+2)
    print("atharva" + " pingale")
    print("atharva "*3)

    class A: 
        def __init__(self , a): 
            self.a = a
        # adding 2 objects 
        def __add__(self, o): 
            return self.a + o.a
    
    ob1 = A(1)
    ob2 = A(2)
    ob3= A('atharva')
    ob4 = A(' pingale')
    print(ob1 + ob2)
    print(ob3 + ob4)

    # Peform addition of 2 complex 
    # numers using binary 
    # + operator overloading 

    class Complex : 
        def __init__(self , a,b): 
            self.a = a
            self.b = b
        # Adding 2 objects 
        def __add__(self, other) :
            return self.a + other.a, self.b + other.b
    
    ob1 = Complex(1,2)
    ob2 = Complex(2,3)
    ob3 = ob1+ob2
    print(ob3)

    # cOMPARISON oPERATORS 
    class A: 
        def __init__(self, a ): 
            self.a = a 
        def __gt__( self, other ): 
            if (self.a>other.a) :
                return True 
            else : 
                return False
    
    ob1 = A(12)
    ob2 = A(13)
    print(ob1>ob2)
    print(ob1<ob2)

    # Overloading Equality and less than operators 

    class B: 
        def __init__(self,  a): 
            self.a =a 
        def __lt__(self, other): 
            if (self.a<other.a): 
                return "ob1 is less than ob2"
            else :
                return "ob1 is greater than ob2"
        
        def __eq__(self, other ): 
            if ( self.a==other.a ): 
                return "Both are equal"
            else : 
                return "Not Equal"
    
    ob1 = B(2)
    ob2 = B(3)
    print(ob1<ob2)

    ob3 = B(4)
    ob4 = B(4)
    print(ob1==ob2)

def f6() :
    # Any All in python

    # Since all are false, false is returned 
    print(any([False,False ,False , False]))

    # Here the method will short-circuit at the 
    # second item (True) and will return True 
    print(any([False , True , False , False ]))

    # Here the method will short-corsuit at the 
    # first item (True ) and will return True 
    print(any([True, False , False , False]))

    # All 
    print(all([False,False , False ]))
    print(all([False , True , False]))
    print(all([True , True , True ]))

    # Practical exmaples 
    list1 = []
    list2 = []
    # index ranges from 1 to 10 to multiply 
    for i in range(1,11): 
        list1.append(4*i)
    
    # index to access the list2 if from 0 to 9 
    for i in range(0,10): 
        list2.append(list1[i]%5==0)
    
    print("See wheather at least one number is divisible by 5 in list1 : ")
    print(any(list2))

    # To find odd numbers
    list1 = []
    for i in range(1,11): 
        list1.append(4*i)
    
    for i in range(0,10):
        list2.append(list1[i]%2!=0)
    
    print("Odd numbers : " , any([list2]))

def f7() :
    # Immutable Targets 
    import operator 
    # initializing valeus 
    x = 5 
    y = 6
    a = 5
    b = 6
    # using add() to add the arguments passed 
    z=  operator.add(a,b)

    # using iadd9() to add the arguments passed 
    p = operator.iadd(x,y)

    # printing the modified value 
    print("Value after adding using normal operator : " , end=" ")
    print(z)

    print("Value after adding using Inplace operator : " , p)
    print("Value of x : " , x)
    print("Value of x : " , a)

    # Mutable Targets 
    a = [1,2,4,5]
    #using add9) to add the arguments passed 
    z = operator.add(a,[1,2,3])
    # adds [1,2,3] tpo the list 
    print("z : " , z)
    print("Value of a : " , a) # stays the same 
    # using iadd() 
    p = operator.iadd(a,[1,2,3])
    print("p : " , p)
    print("Value of a : " , a) # gets changed 

def f8() : 
    # Operator Functions in python
    # add() , sub() ,  mul() 

    # importing operator module 
    import operator 

    a = 4
    b=3

    # using add9) ot add 2 numbers 
    print("Addition : " , operator.add(a,b))

    # using iadd() to add 2 numebers 
    print("Addition 2 : " , operator.iadd(a,b))
    print("Multiply : " , operator.mul(a,b))
    print("Subtraction : " , operator.sub(a,b))
    # truediv(a,b)
    print("True division : " , operator.truediv(a,b))
    # floordiv() 
    print("Flooe division : " , operator.floordiv(a,b))
    # pow() 
    print("Power : " , operator.pow(a,b))
    # mod() 
    print("Module : " , operator.mod(a,b))
    #lt() 
    # to check if a is less than b or not 
    print("lt : " , operator.lt(a,b))
    #le()
    print("le : " , operator.le(a,b))
    # eq() 
    print("eq : ",  operator.eq(a,b))
    # gt() 
    # greater than 
    print("gt : " , operator.gt(a,b))
    # ge()
    print("ge : " , operator.ge(a,b))
    # ne()
    print("ne : ",  operator.ne(a,b))

def f9(): 
    # Inplace operators()
    import operator 
    #iadd() and iconcat() 
    x = operator.iadd(2,3)

    #print the modified value 
    print("The value after adding and assigning : ",  end=" ")
    print(x)

    #initializing values 
    y = 'geeks'
    z = 'forgeeks'

    #using iconcat() to concat the sequences 
    y = operator.iconcat(y,z)
    #using iconcat() to concat sequences 
    print("The string after concatenation is : ",  y)
    # similarly 
    # isub() 
    # imul() 
    # itruediv() 
    # imod() 

def f10() : 
    # Logic Gates in Python
    # and gate 
    def AND ( a,b): 
        if a==1 and b==1: 
            return True 
        else : 
            return False 
    
    # Driver Code 
    if __name__ =='__main__': 
        print(AND(1,1))
        print("+--------------+--------------+")
        print(AND(False , False ))
        print(AND(True , False ))
        print(AND(False , True ))
        print(AND(True , True ))
    
    #NAND gate 
    def NAND(a,b): 
        if a==1 and b==1 : 
            return False 
        else: 
            return True 
    print("NAND Gate : ")
    # Driver Code 
    if __name__=='__main__': 
        print(NAND(1,0))
        print(NAND(False , False))
        print(NAND(True , False))
        print(NAND(False , True ))
        print(NAND(True , True))
    
    # OR gate 
    def OR(a,b): 
        if a==0 and b==0 : 
            return False
        else : 
            return True
    print("OR gate : ")
    # Driver Code 
    if __name__ =='__main__': 
        print(OR(1,0))
        print(OR(False ,  False))
        print(OR(True  ,  False))
        print(OR(False ,  True))
        print(OR(True ,  True))
    
    # XOR gate 
    def XOR(a,b): 
        if a!=b: 
            return True 
        else: 
            return False 
    print("XOR gate : ")
    # Driver Code 
    if __name__ =='__main__': 
        print(XOR(1,0))
        print(XOR(False,  False ))
        print(XOR(True,  False ))
        print(XOR(False,  True))
        print(XOR(True,  True))
    
    # NOT gate 
    def NOT(a,b): 
        return not a 
    print("NOT gate : ")
    # Driver Code 
    if __name__ =='__main__': 
        print(NOT(1,0))
        print(NOT(False , False))
        print(NOT(True , False))
        print(NOT(False ,True))
        print(NOT(True, True))
    
    # NOR gate 
    def NOR(a,b): 
        if a==0 and b==0: 
            return True 
        else : 
            return False 
    
    # Driver Code 
    print("NOR gate : ")
    if __name__ =='__main__': 
        print(NOR(1,0))
        print(NOR(False , False))
        print(NOR(True, False))
        print(NOR(False , True))
        print(NOR(True , True))
    
    # XNOR gate 
    def XNOR(a,b):
        if a==b :
            return True 
        else : 
            return False 
    
    # Driver Code 
    print("XNOR gate : ")
    if __name__ =='__main__': 
        print(XNOR(1,0))
        print(XNOR(False,False))
        print(XNOR(True,False)) 
        print(XNOR(False,True))
        print(XNOR(True,True))
        
def f11() : 
    # Python a+=b is not always 
    # a=a+b
    list1 = [5,4,3,2,1]
    list2 = list1
    list1 += [1,2,3,4]
    print(list1)
    print(list2)
    # Even lust 2 gets appended 
    # step 1 : list1 is initialized 
    # step 2 : list2 is equal to list1 , which means that 
    # the contents of list1 gets shared with list2
    # step 3 : list1 gets appended
    # step 4 : list2 also gets appended

    # Example 2 
    list1 = [5,4,3,2,1]
    list2 = list1
    list1 = list1 + [1,2,3,4]
    print(list1)
    print(list2)
    # list2 does not get appended

def f12()  :
    # Differencce in '==' and 
    # 'is' operator 
    list1 = []
    list2 = []
    list3 = list1
    if(list1==list2): 
        print("True")
    else : 
        print("False ")
    
    if (list1 is list2):
        print("True")
    else:
        print("False")
    if (list1 is list3):
        print("True")
    else:   
        print("False")
    list3 = list3 + list2
    if (list1 is list3):
        print("True")
    else:   
        print("False")
    
    print(id(list1))
    print(id(list2))


def f13(): 
    # Membership and Identity 
    # Membership operators 
    # in operator 
    list1 = [1,2,3,4]
    if 3 in list1: 
        print("YES")
    else : 
        print("NO")
    
    # overlapping without using operator 
    def overlapping(list1, list2) : 
        c=0
        d=0
        for i in list1: 
            c+=1
        for i in list2: 
            d+=1 
        for i in range(0,c): 
            for j in range(0,d): 
                if(list1[i]==list2[j]): 
                    return 1
        return 0
    
    list1 =[1,2,3,4,5]
    list2 = [6,7,8,9]
    if(overlapping(list1,list2)): 
        print("overlapping")
    else : 
        print("not overlapping")
    
    # 'not in' operator 
    x = 24
    y=20
    list = [10,20,30,40,50]

    if(x not in list ): 
        print("x is not present in given list")
    else : 
        print("x is present in the given list ")
    
    if(y in list) :
        print("y is present ion the list ")
    else : 
        print("y is not in the given list ")
    
    #identity opeators 
    # 'is' operator 
    x=5 
    if ( type(x) is int ): 
        print("True ")
    else: 
        print("False")

    # 'is not' operator 
    x = 5.2
    if ( type(x) is not int ): 
        print("true")
    else : 
        print("false")

def f14() :
    # Loops in python
    # while loop
    count =0
    while (count<3): 
        print(count)
        count=count+1
    
    print("While with else ")
    #using else statements in while loop
    count =0
    while (count<3): 
        count = count +1 
        print(count)
    else : 
        print("In the else block")

    # for loop
    for i in range(0,4): 
        print(i , end=" ")
    print("\n")
    # list iteration
    l = ['atharva' , 'pingale' , 'boy']
    for i in l: 
        print(i)
    
    # tuple iteration
    tup = ('atharva' , 'pingale ' , 'boy')
    for i in tup: 
        print(i)
    
    # string iteration
    s = 'atharva pingale '
    for i in s : 
        print(i)
    
    # dictionary iteration
    dict = {1:'atharva' , 2:'pingale' , 3:'boy'}
    for i in dict : 
        print(i)
    
    # printing dictionary items 
    for i in dict : 
        print(dict[i])
    
    for i in dict.items(): 
        print(i)
    
    for i in dict.values()  :
        print(i)
    
    for i in dict.keys() : 
        print(i)
    
    # iterating by index of sequences 
    print("Iterrating by index of sequences : ")
    list = ['atharva' , 'pingale' , 'boy']
    for index in range(len(list)): 
        print(list[index])
    
    # using else statements with loops 
    lsit = ['atharva' , 'pingale ' , 'boy']
    for index in range(len(list)): 
        print(list[index])
    else : 
        print("Inside the else block")
    
    # Nested loops 
    for i in range(1,5) :
        for j in range(i): 
            print(i , end=" ")
        print()
    
    # loop control statements 
    for letters in 'atharva pingale' : 
        if letters=='g' or letters =='s': 
            continue 
        print("Current letter : ",  letters)
    
    # Break statement 
    for letters in 'atharvapingale ': 
        # brea loop as soon as it sees 'g'
        # or 's'
        if letters =='g' or letters =='s': 
            break
        print("Current letter : " , letters )
    
    # Pass statement 
    for letter in 'atharva': 
        pass
    print("Last letter : " , letter)

    # lists 
    fruits = ['apple' , 'orange' , 'kiwi']
    for fruit in fruits : 
        print(fruit)
    
    print("Using iter_obj : ")
    fruits = ['apple' , 'banana' , 'orange']
    iter_obj = iter(fruits)
    while True : 
        try : 
            # getting the next item
            fruit = next(iter_obj)
            print(fruit)
        except : 
            # if StopIteration 
            # is raised , it breaks 
            break

def f15() : 
    #Looping technique in Python 
    # Using Enumerate () 
    for  key, value in enumerate(['atharva' , 'pingale ' , 'boy']): 
        print(key ,  value )


    # Using zip() 
    # Zip() is used to combine 2 similar 
    # containers 
    # list-list and dict-dict 
    questions = ['name ' , 'colour ' , 'shape']
    answers = ['apple' , 'red ' , 'circle']
    # using zip()
    for a, b in zip(questions , answers ): 
        print(a,b)

    # using iteritems() 
    d = {'atharva' : 'boy' , 'Julia' : 'girl'}
    # using iteritems to print the dictionary
    
    # using items to print the dictionary key-value 
    # pair 
    print("The key value pair using items is : " )
    for i,j in d.items(): 
        print(i,j)
    
    for i in d.items () : 
        print(i)
    
    # using sorted () 
    list = [1,3,5,6,2,1,3]
    # using sorted 90 to print the list in sorted order 
    print("The list in sorted order : ")
    for i in sorted(list): 
        print(i , end=" ")
    print()
    # sorted list , without duplicates 
    print("Sorted list without duplicates : ")
    for i in sorted(set(list)): 
        print(i)
    
    # Exmample 
    basket = ['guave' , 'orange' , 'apple' , 'pear'
                , 'guave' , 'banana' , 'grape']
    # using sorted() and set() to print the list 
    # in sorted order 
    for i in sorted(set(basket)): 
        print(i)
    
    # Using reversed () 
    list = [1,5,2,3,9,2]
    for i in reversed(list): 
        print(i)

def f16() : 
    # Programs ofr printing 
    # Pyramid patterns in Python
    def p1(n): 
        for i in range(0,n) :
            for j in range(0,i+1): 
                print("*" , end=" ")
            print()
    p1(5)

    # Another Approach 
    def p2(n) : 
        mylist = []
        for i in range(1,n+1): 
            mylist.append("* "*i)
        print("\n".join(mylist))
    p2(5)

    # After 180 degree rotation
    def p3(n) :
        # number of spaces 
        k = 2*n-2
        for i in range(0,n): 
            for j in range(0,k): 
                print(" " , end="")
            k = k-2
            # printing stars 
            for j in range(0,i+1): 
                print("* " , end="")
            print()
    p3(5)

    # Printing Trangle 
    print("\n")
    def p4(n):
        k = n-1
        for i in range(0,n): 
            # Printing spaces 
            for j in range(0,k) :
                print(" " , end="")
            # Printing stars 
            k=k-1
            for j in range(0,i+1): 
                print("* ",end="")
            print()

    p4(5)

    # Number Pattern
    def p5(n) :
        for i in range(0,n): 
            for j in range(0,i+1): 
                print(j+1,end=" ")
            print()
    p5(5)

    # Numbers without reassigning 
    def p6(n) :
        count =1
        for i in range(0,n):
            for j in range(0,i+1):
                print(count,end=" ")
                count =count +1 
            print()
                            
    p6(5)

    # Character pattern 
    def p7(n) :
        count =65
        for i in range(0,n): 
            for j in range(0,i+1): 
                print(chr(count) , end=" ")
            count = count +1 
            print()
    p7(5)

    # Continuous character Pattern
    def p8(n): 
        count =65
        for i in range(0,n): 
            for j in range(0,i+1): 
                print(chr(count),end=" ")
                count = count +1 
            print()
    p8(5)

def f17() :
    # Chaining Comparison in Python 
    x =5 
    print(1<x<6)
    print(10<x<20)
    print(x<10<x*10<100)
    print(10>x<=9)
    print(5==x>4)

    # Example 
    print("Exmaple 2 : ")
    a,b,c,d,e,f = 0,5,12,0,15,15
    exp1 = a<=b <c>d is not e is f 
    exp2 = a is d>f is not c 
    print(exp1)
    print(exp2)

def f18() :
    # Here else block is exeucted 
    for i in range(1,4): 
        print(i)
    else : # Executed because no break in for 
        print("No break")
    
    # Here else block is not executed 
    for i in range(1,4): 
        print(i)
        break
    else : # Not execured as there is a break
        print("No break")
    
    def contains_even_number(list): 
        for element in list: 
            if element%2==0: 
                print("List contains an even number")
                break
        else : 
            print("List contains odd numbers")
    contains_even_number([1,9,8])
    contains_even_number([2,4,6])
    contains_even_number([1,3,7])

def f19() : 
    # Switch function in python 
    ## python does not have 
    # switch casing 
    # to get around this fact 
    # we use dictionry mapping 
    def numbers_to_strings(argument): 
        switcher = {0 :'zero' , 1:'one' , 2:'two'}

        # get() method of dictionary data type returns 
        # value of passed argument if it is present 
        # in dictionatry otherwise second argment will
        # be assigned as defualt value of passed argument 
        return switcher.get(argument, 'nothing')
    
    # Driver Code 
    if __name__ == '__main__': 
        argument = 0
        print(numbers_to_strings(argument))
        argument = 12
        print(numbers_to_strings(argument))

def f20() : 
    # Using iterations in python effectively 
    cars = ['aston' , 'audi' , 'mclaren']
    i=0
    while i<len(cars): 
        print(cars[i])
        i = i+1
    # for in style 
    for i in cars: 
        print(i)
    
    # indexing using range() functions 
    for i in range(len(cars )): 
        print(cars[i])
    
    # using enumerate 
    print("Using enumerate (): ")
    for key,value  in enumerate(cars ): 
        print(key, value )
    print("Enumerate alternative example : ")
    # Alternative solution
    for i in enumerate(cars ): 
        print(i[0] , i[1])
    
    # Starting the enumerate from 1 
    for i in enumerate( cars , start =1): 
        print(i[0] , i[1])
    
    # Looping extensions 
    cars = ["Aston", "Audi", "McLaren"]
    accessories = ["GPS kit", "Car repair-tool kit"]
    prices = {1:"570000$", 2:"68000$", 3:"450000$",
        4:"8900$", 5:"4500$"}
    # Printing the prices of the cars 
    for index , c in enumerate(cars , start =1 ): 
        print("Cars : %s  , Price : %s " %(c,prices[index]))
    
    # Pricing hte accessesories 
    for index,  a in enumerate(accessories,start=1): 
        print("%s , Price : %s " %(a , prices[index+len(cars)]))

    # Zip function 
    cars = ["Aston", "Audi", "McLaren"]
    accessories = ["GPS", "Car Repair Kit", 
                "Dolby sound kit"]
    # Combinign the lists and printing 
    for c,a in zip(cars , accessories): 
        print("{0}  , {1} " .format(c,a))

    # Unzipping and then printing 
    l1,l2 = zip(*[('Aston', 'GPS'), 
            ('Audi', 'Car Repair'), 
            ('McLaren', 'Dolby sound kit') 
            ])
    print(l1)
    print(l2)

def f21() :
    # Python itertools 
    import operator 
    import time 

    # Defining lists 
    l1=  [1,2,3]
    l2 = [2,3,4]

    # Starting time before map 
    # function 
    t1 = time.time() 

    # Calculating the result 
    a,b,c = map(operator.mul ,l1,l2)
    # Ending time after map 
    t2 = time.time() 
    time_taken = t2-t1
    print("Result : " , a,b,c)
    print("Time taken : " , time_taken)

    # 3 types of iterators 
    # 1. Infinite iterators 
    # 2. Combinatoric iterators 
    # 3. Terminating iterators 
    import itertools

    for i in itertools.count(5,5) : 
        if i==35: 
            break
        else : 
            print(i , end=" ")
    print() 
    #cycle 
    count =0
    for i in itertools.cycle('A'): 
        if count>7: 
            break
        else : 
            print(i , end=" ")
            count =count +1 
    print() 

    # using hte next function 
    l = ['atharva' , 'pingale ' , 'person']
    # defining iterator 
    iterators = itertools.cycle(l)
    for i in range(5) :
        print(next(iterators),end=" ")
        print() 
    
    # repeat(val , num)
    print("Priting a 2 times : " , list(itertools.repeat('A',2)))

    # Combinatoric iterators 




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
#f17()
#f18()
#f19()
#f20()
f21()      
