


def f1() :
    # data structures 
    # assigning string to a variable 
    a= "this is a string"
    print(a)

    # lists in python
    # declaring a list 
    l = [1,'a',2,'b']
    print(l)
    l.append(6)
    print(l)
    l.remove(6)
    print(l)
    l.pop()
    print(l)
    print("index 2 : " ,l.index(2)) 
    print("list at index 2 :  " , l[2])
    l.clear()
    print("list : " , l)

    # tuple 
    tup = (1 , 'a' , 2, 'string ')
    print(tup)
    print(tup[1])
    # interation in python
    i=0
    while i<10: 
        print(i, end=" ")
        i=i+1
    print()
    s = 'hello world '
    for i in s : 
        print(i , end=" ") 
    print()
    l = [1,2,3,4,5]
    for i in l: 
        print(i , end=" ")
    print()
    for i in range(0,10): 
        print(i ,end=" ")
    print()

def f2()  :
    # string 
    string1 = 'welcome here '
    print(string1)
    # string with triple quotes 
    string2 = '''here i am '''
    print(string2)
    string2 = ''' this 
                    is 
                    a  milti line string'''
    print(string2)

    string1 = 'hello everyone '
    for i in string1:
        print(i , end=" ")
    
    print()
    print(string1[1])
    # string slicing 
    print("initial string 1 : ",string1)
    print("After slicing the string1 : " , string1[3:12])
    print("Slicing the string1 backwards : " , string1[3: -2])

    # deleting / updating from a string 
    del string1
    string1 = "i'm a \"geek\""
    # escaping double quotes 
    print(string1)
    string1 = 'i\'m a "geek"'
    # escaping single quotes
    print(string1)
    string1 = "c:\\python\\geeks\\"
    # escaping backlashes
    print(string1)
    
    # raw stinrg and an escape string 
    # using r and R 
    string1 = "this is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
    print("Printing in hex with use of escape sequence : ")
    print(string1)

    # using raw sting ot 
    # ignore escape sequences 
    string1 = r"this is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
    print("\nPrinting raw string in Hex format : ")
    print(string1)


    # formatting of strings 
    # default order 
    string1 = "{} {} {}" .format('geeks' , 'for' , 'life')
    print("Print string in default order : ")
    print(string1)

    # positional formatting 
    string2 = "{1} {0} {2} " .format('geeks' , 'for' , 'life')
    print(string2)

    # keyword formatting 
    string3 = "{l} {f} {g}" .format(g='geeks' , f='for' ,l='life')
    print(string3)
    
    # formatting of integers 
    string1 = "{0:b}" .format(16)
    print("\nBinary representation of 16 is : ")
    print(string1)

    # formatting of floats 
    string1 = "{0:e}" .format(165.6458)
    print("\nExponenet representation pf 165.6458  : ")
    print(string1)

    # rounding off integers 
    string1 = "{0:.2f}" .format(1/6)
    print("\none-sixth : ")
    print(string1)

    # string alignment 
    string1 = "|{:<10}|{:^10}|{:>10}|" .format('geeks' , 'for' , 'geeks')
    print("\nLeft, center and right alignment with formatting : ")
    print(string1)

    # To demonstrate aligning of spaces 
    string1 = "\n{0:^16} was founded in {1:<4}!" .format('geeksforgeeks' , 2009)
    print(string1)

    #python program for 
    # old style formatting 
    # of integers 
    integer1 = 12.3456789
    print("Formatting in 3.2f format : ")
    print("The value of Integer1 is %3.2f : " %integer1)
    print("\nFormatting in 3.4f format : ")
    print("The value of Integer1 is %3.4f " %integer1)
    
    print("\n\n")
    # more string examples 
    import string
    result = string.ascii_letters
    print(result)
    # prints all the ascii letters 
    # in both lower and upper case 
    result = string.ascii_lowercase
    # result = all lower case letters of the ascii letters 
    print(result)

    result = string.ascii_uppercase
    # result = all upper case letters of ascii
    print(result)
    string1 = 'ATHARVA'
    for i in string1 : 
        for j in result: 
            if i==j: 
                print(i , end=" ")
    
    print()
    num = string.digits
    # num = all digits fr0m 0-9
    print(num)
    import random
    generate_pass = ''.join([random.choice(string.ascii_lowercase + string.digits) for n in range(10)])
    print(generate_pass)

    generate_password = ''.join([random.choice(string.ascii_uppercase + string.digits) for n in range(10)])
    # combines string.ascii_uppercase and string.digits 
    # then creates a random password 
    # with size 10
    print(generate_password)

    #string.digits 
    print(string.digits)
    generate_password = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(10)])
    print(generate_password)            
    print()

    # string hex digits 
    print(string.hexdigits)
    # gets all the hexadecimal value s
    # checking hexadecimal values 
    value = "0123456789abcdef"
    print("INPUT : ")
    for i in  value : 
        if i not in string.hexdigits: 
            print("False")
            break
    else : 
        print("True")
    
    # generate_password of random hexdigits 
    generate_password = ''.join([random.choice(string.hexdigits) for i in range(10)])
    print(generate_password)

    # endswith () 
    text = 'geeksforgeeks'

    result = text.endswith('for geeks')
    print(result)
    result = text.endswith('forgeeks')
    print(result)
    result =text.startswith('geeksafter')
    print(result )
    result = text.startswith('geeks')
    print(result)

    # isdigit() 
    print("is digit: ")
    text = '123'
    result = text.isdigit()
    print(result)
    text='1a2d'
    print(text.isdigit())

    # errors and exceptions 
    count =0
    newstring=''
    # incrementig counter if a digit is found 
    # Finally printing the count an the new string 
    for a in range(53): 
        b = chr(a)
        if b.isdigit() ==True: 
            count +=1
            newstring +=b
    
    print("Toal digits in range : " , count )
    print("Digits : " , newstring)

    # containing numeric characters 
    print("Nmeric characters : ")
    s=  '12345'
    print(s.isdigit())

    s = '\u00B23455'
    # s = 'superscript(2)3455
    print(s.isdigit())
    # prints true as superscript(2) is als a digit
    # s = '1/2'
    # fraction is not a digit 
    s = '\u00BD'
    print(s.isdigit())

    # isdecimal() 
    print("isdecimal() : ")
    t = '123'
    print(t.isdecimal())
    t = 'a1b2'
    print(t.isalpha())
    t = 'abcd'
    print(t.isalpha())
    t = '12 34'
    print(t.isdecimal())

    # str.format() 
    print("str.format() : ")
    print("{} , A computer science portal for geeks" .format('geeksfrogeeks'))
    # using the format option available 
    string = 'atharva'
    print("\n{} is a cool guy" .format(string))
    # positional formatting 
    print("{1} {0} {2} are numbers " .format(1,2,3))
    
    # keywod formatting 
    print("{a} {b} " .format(a='atharva' , b='is cool'))

    # string index 
    ch = 'geeksforgeeks'
    # initializing argument string 
    ch1 = 'geeks'

    # using index() to find position of geeks 
    # starting from 2nd index 
    # print 8 
    pos = ch.index(ch1 , 2)
    print("The first position of geeks after 2nd index : " ,end=" ")
    print(pos)

    #index() 
    #initializing target string 
    ch = 'geeksforgeeks '
    # initializing hte argument string 
    ch1 = 'gfg'

    # using index() to find position of 'gfg'
    # raises error() 
    #pos = ch.index(ch1)
    print("The first position os gfg is : ")
    #print(pos)

    # whitespace() 
    print("Whitespaces : ")
    string = 'atharva'
    print(string.isspace())
    string = 'atharva is cool'
    print(string.isspace())
    string = 'atharva\nis\ncool'
    print(string.isspace())
    string = '\n \n \n'
    print(string.isspace())
    string ='\n'
    print(string.isspace())
    # space counter 
    print("Space counter program : ")
    string = 'My name is atharva'
    count =0
    for a in string : 
        if (a.isspace())==True: 
            count +=1
    print(count)

    string = 'My name is \n\n\n\natharva'
    count =0
    for a in string : 
        if (a.isspace())==True: 
            count +=1
    print(count)

    # swapcase program 
    # converts all lowercase to uppercase 
    # and converts all uppercase to lowercase 
    print("Swap case program : ")
    string = 'GeeksforGeeks'
    # prints after swapping all cases 
    print(string.swapcase())

    string ='supercool' 
    print(string.swapcase())

    # replace (old , new , count ) 
    print("Replace() program : ")
    string = 'atharva is atharva is cool'
    # prints the string by replacing all 
    # atharva by Boy
    print(string.replace('atharva' ,'Boy'))
    print(string.replace('a' , 'x'))
    print(string.replace('atharva' , 'Boy' , 1))
    # replaces only the 1st occurence of 'atharva' 
    # with 'Boy'
    print(string.replace('a','x',3))
    # replaces 3 occorunes of 'a'
    # with 'x'

def f3() : 
    # Lists 
    # creating a list 
    list = []
    print("Blank list : ")
    print(list)
    list = [1,2,2,4]
    print(list)
    # creating a list of strings and accessing 
    # using index 
    list = ['atharva' , 'is' , 'cool']
    print("\nList items : ")
    for i in list : 
        print(i)
    
    # creating a multidimensional list 
    # by nesting a list insidea list 
    list = [['atharva' , 'cool'] , 'is ']
    print("Multi-dimensional list : " , list)

    # creating a lsit with multiple distant or duplicate elements 
    list = [1,2,4,4,3,3,3,6,5]
    print("\nList with the use of Numbers : ")
    print(list)

    # creating a list with 
    # mixed type of values 
    # ( Hsving numbers and string) 
    list = [1,2,'atarva' ,4,'is' , 5,'cool']
    print(list)
    # knowing the size of the list
    print(len(list))
    # appending 
    print("Appending a list : ")
    list.clear() 
    print(list)
    for i in range(3): 
        list.append(i)
    print(list)

    # using tuple to append 
    list.append((8,9))
    print(list)
    for i in list : 
        print(i , end=",")
    print() 
    print(list[3][0])
    print(list[3][1])
    list2 = ['atharva']
    list.append(list2)
    print(list)

    # insert operation in a list 
    list.insert(0,12)
    print(list)
    #insert(position , element)
    # extend() 
    print("Using extend : ")
    # addition of elements in a list 
    # creating a list 
    list = [1,2,3,4]
    print(list)

    # addition of multiple elements 
    # to the list at the end 
    # ( using the exted method)
    list.extend([8,'geeks','always'])
    print("\nList after using extend : ", list)

    # accessing elements from the list
    list=['geeks' , 'for' ,'geeks']
    print(list[0])
    print(list[1])

    # creating a new multi-dimensional list 
    list = [['geeks' , 'for'] , ['geeks']]

    # accessing an element from the 
    # multi-dimensional list using 
    # # index number 
    print("Accessing a element from a multi-dimensional list : ")
    print(list[0][1])
    print(list[1][0])

    #REMIVING ELEMENTS FORM THE LIST 
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(list)
    print("Removing elements from the list : ")
    list.remove(5)
    list.remove(6)
    print("\nList after removal of 2 elements : ")
    print(list)
    # removing elements frmo an iterator 
    for i in range(1,5): 
        list.remove(i)
    print("\nList after Removing a range of elements : " , list)

    # poppig in list
    print("uSING POP() IN list : ")
    print(list)
    print(list.pop()) 
    print(list)
    print(list.pop(3)) 
    # pop's the 3rd element 
    print(list)

    # list comprehesion
    print("List comprehension : ")
    odd_square = [x**2 for x in range(1,11) if x%2==1]
    print(odd_square)
    even_square = [x**2 for x in range(1,11) if x%2==0]
    print(even_square)
    print("Sorted list in ascending order : " , list.sort(reverse=False))
    result = sorted(list)
    print("Sorted list in ascending order : " , result)
    print("Sorted list in reversed order : " , sorted(list , reverse = True))
    print("list in reverse order using reverse : " , reversed(list))
    result = []
    result  = reversed(list)
    print("Reverse list : " , result)
    print("Reversed list : ")
    for i in result : 
        print(i,end=",")

def f4() :
    # tuples 
    # creating a tuple 
    tuple1 = ()
    print("Tuples : ")
    print(tuple1)
    tuple1 = ('atharva' , 'is' ,'cool')
    print(tuple1)
    # creating a tuple1 with 
    # use of list 
    list = [1,2,3,4,5,6]
    print("Tuple of the list : " , tuple(list))
    tuple2 = tuple('atharva')
    # created a tuple2 
    # of every character /letter 
    # present in the word 'atharva'
    print(tuple2)

    # creating a tuple with mixed data types 
    print("Creating a tuple with mixed data types : ")
    tuple1 = (5,'atharva' , 7)
    print(tuple1)

    # creating a tuple with nested tuples 
    tuple1= (0,1,2,3)
    tuple2 = ('atharva' , 'pingale')
    tuple3 = (tuple1,tuple2)
    print("tuple3 :  " , tuple3)

    # creating a tple with repeatition 
    tuple1 = tuple('atharva')*3
    print("tuple1 with repeatition : " , tuple1)
    # prints the characters 
    # from the word 'atharva' 
    # 3 times 

    # creating tuple using loops 
    print("Tuple created using loops: ")
    tuple1 = 'geeks'
    for i in range(5): 
        tuple1 = (tuple1,)
        print(tuple1)
    print()

    # Accessing of tuples 
    # with indexing 
    tuple1 = tuple('geeks')
    print(tuple1)   
    #tuple unpacking 
    tuple1 = ('geeks' , 'for' , 'geeks')
    # this line unpack 
    # # values of tuple1
    a,b,c = tuple1 
    print("Elements of tuple : {} {} {} " .format(a,b,c))

    # formatting a tuple 
    tuple1 = (0,1,2,3)
    tuple2 = ('geeks' , 'for', 'geeks')
    tuple3 = tuple1+ tuple2
    # printing the 1t tuple , rhen 2nd , then final 
    print(tuple1 , "\n" , tuple2 , "\n" , tuple3)

    # slicing a tuple 
    tuple1 = tuple('atharva')
    # removing first element
    print("removing st elemnt : " , tuple1[1:])
    # reversing hte tuple 
    print("Reversing the tuple : " , tuple1[::-1])

    # printing elements of a range 
    print("\nPrinting elemnts between rane 4-9 : " , tuple1[4:9])

    # deletating a tuple 
    print("Deleating a tuple : ")
    del tuple1 
    # error : print(tuple1)


def f5() : 
    # sets 
    print("Sets : ")
    set1 = set() 
    print(set1)

    # use of string 
    set1 = set('atharva')
    print(set1)
    # does not print duplicate characters 

    # use of a list 
    set1=set([1,2,1,4,2])
    print(set1)

    # adding elements to a set 
    print("Adding elements to a set : ")
    set1 = set() 
    print("Initial blank set : ")
    print(set1)

    # Adding elemnt and tuple to the set 
    set1.add(8)
    set1.add(9)
    set1.add(10)
    print("\nSet after addition of 3 elemnts : ")
    print(set1)

    # using iterator to add elements 
    set2 = set() 
    for i in range(5): 
        set2.add(i)
    print("Final set after iteration : ", set2)

    # using update() 
    set2.update([6,7])
    print(set2)
    set2.discard(2)
    print(set2)
    print(set2.pop())
    # pop's the 0th element  
    print(set2)
    set2.clear() 
    print(set2)

def f6():
    # dictionary 
    dict = {1:'atharva' , 2:'pingale'}
    print(dict) 

    # creating a dictionary 
    # with mixed names 
    dict = {'name': 'atharva' ,1:[1,2,3,4,5]}
    print(dict)
    dict={}
    # creating an empty dicitonary 
    dict3={}
    dict3 ={(1,'atharva') ,( 2,'pingale')}
    print(dict3)






#f1()
#f2() 
#f3()
# f4()
#f5()
f6()    