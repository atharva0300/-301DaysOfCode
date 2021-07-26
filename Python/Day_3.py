from  __future__ import print_function
import operator 
import time 
import itertools

def func1():
    count=0
    while(count<3):
        count = count +1
        print(count)

def func2():
    count =0
    while (count<3):
        count = count +1
        print("abracadabatr")
    else:
        print("in else block")
    n=4
    for n in range(2,10):
        print(n)
    print("List iteration")
    l =['geeks' , 'for' , 'geeks']
    for i in l:
        print(i)
    print("\nTuple iterations")
    s = 'geeks'
    for i in s: 
        print(i)
    print("Dicionary iteration")
    d = dict()
    d['xyz'] = 123
    d['abc'] = 345
    for i in d:
        print(i)
    for i in d.items():
        print(i)
    for i in d:
        print(i)
    for i in d:
        print(i , ' : ' , d[i])
    for i in d:
        print("%s %d" %(i  ,d[i]))

def func3():
    list = ['geeks' , 'for' , 'geeks']
    for index in range(len(list)):
        print(list[index])
    
    print("Using else statement after for loop  :")
    for index in range(len(list)):
        print(list[index])
    else  :
        print("Inside else block")
    print("Nested loops : ")
    for i in range(1,5):
        for j in range(i):
            print(i , end=" ")
        print()
    for letter in 'geeksforgeeks':
        if letter =='e' or letter=='s':
            continue
        print("Current letter : " , letter)
        var =10
    s ='adam gilchrist'
    for letter in s: 
        if letter =='a' or letter=='g':
            continue 
        else : 
            print(letter)
    print()
    for letter in s : 
        if letter==' ':
            print("Space found")
    for letter in 'geeksforgeeks':
        if letter=='e' or letter =='s ':
            break
    print("Current letter :  " , letter )
    for i in range(1,5) :
        pass 
    print("Last number : " , i)
    fruits = ['guava' , 'mango' , 'apple']
    for i in fruits: 
        print(i)
    print("Using iterations iter() : ")
    iter_obj = iter(fruits)
    #indefinite while loop
    while True : 
        try : 
            #getting the next item
            fruit = next(iter_obj)
            print(fruit)
        except StopIteration  :
            # if StopIteration is raised 
            #break from the loop
            break


def func4():
    print("Inside function 4 : ")
    for key, value in enumerate(['the ' , 'big' , 'bang' , 'theory']):
        print(key , value)
    for key , value in enumerate (['geeks' ,'for' , 'geeks']):
        print(value , end=" ")
    questions = ['name ', 'color' , 'shape']
    answers = ['apple' , 'red' , 'circle']
    #using zip() to combine 2 containers 
    # and print values 
    for q , a in zip(questions , answers ) :
        print("What is your {0}? I am {1}." .format(q , a))
    d = {'geeks' : 'for' , 'only' : 'geeks' } 
    #using iteritems to print the dictionary key-value pair 
    print("The key value pair using items is : " )
    #using items to print the dictionary key-value pair 
    for i,j in d.items():
        print(i,j)
    king = {'akbar' : 'the great' ,'chandragupta' : 'maurya' , 'Modi' : 'The changer'}
    #using items to print the dictionary key-avalue pair 
    for key , value in king.items():
        print(key , value)

def func5():
    list = [1,3,5,6,2,1,3]
    #using sorted() to print the list in sorted order 
    print("The list is sorted order is : " )
    for i in sorted(list):
        print(i , end=" ")
    print("\r")
    #using sorted() and set() to print the list in sorted order 
    #use of set() removes duplicates.
    print("The list in sorted order ( without duplicates is : ")
    for i in sorted(set(list)):
        print(i , end=" ")
    print("\r")
    basket = ['guava' , 'orange' , 'bananan' , 'apple']
    #using sorted() and set() to print the list 
    # in sorted order 
    for fruit in sorted(set(basket)):
        print(fruit)
    print("In reverse Order : ")
    for fruit in sorted(set(basket) , reverse = True):
        print(fruit)
    print("In reverse order using reverse : ")
    for i in reversed(basket):
        print(i)
    print("List in rverse order using reverse : ")
    for i in reversed(list):
        print(i , end= ' ')
    print("Range in reversed : ")
    for i in reversed(range(1,10,2)):
        print(i , end=" ")

def func6():
    print("Inside func6() ")
    n = int(input("Enter n : "))
    for i in range(0,n): 
        for j in range(0, i+1): 
            print("*" , end=" ")
        print("\r")
    print("\n")
    mylist = []
    for i in range(1 , n+1): 
        mylist.append("*"*i)
    print("\n".join(mylist))
    print("Star pattern : ")
    k = 2*n - 2
    for i in range(0,n): 
        for j in range(0,k): 
            print(end=" ")
        k = k-2 
        for j in range(0,i+1): 
            print("* " , end="")
        print("\n")
    print("Printing Triangle : " )
    k = n-1 
    for i in range(0,n): 
        for j in range(0,k): 
            print(end=" ")
        k = k-1
        for j in range(0,i+1):
            print("* " , end="")
        print("\n")
    print("Printing number pattern : ")
    for i in range(0,n): 
        for j in range(0,i+1): 
            print(j+1 , end=" ")
        print("\r")
    print("Printing numbers without reassigning : ")
    temp =0
    for i in range(0,n):
        for j in range(0,i+1):
            print(temp+1+j, end=" ")
        temp = temp+1+j
        print("\r")
    print("Character Pattern : ")
    num = 65 
    for i in range(0,n): 
        for j in range(0,i+1):
            ch = chr(num)
            print(ch , end=" ")
        num = num+1
        print("\r")
    print("Continuous Character Pattern : ")
    temp = 65
    for i in range(0,n): 
        for j in range(0,i+1):
            print(chr(temp+j) , end=" ")
        temp = temp+1+j
        print("\r")

def func7():
    print("Inside function 7 : ")
    x=5
    print(1<x<10)
    print(10<x<20)
    print(x<10 <x*10<100)
    print(10>x<=9)
    print(5==x>4)
    print("2nd example : ")
    a,b,c,d,e,f=0,5,12,0,15,15
    exp1 = a<=b <c > d is not e is f 
    exp2 = a is d>f is not c 
    print(exp1)
    print(exp2)

def func8() : 
    print("Inside func8() : ")
    for i in range(1,4): 
        print(i)
    else : #executed becasue no break in for 
        print( "No break")
    print("else block not executed here : ")
    for i in range(1,4): 
        print(i)
        break
    else : 
        #no executed as there is a break 
        print("No break")
    list = [1,9,8]
    for ele in list : 
        if ele%2==0: 
            print("list contains an even number")
            break
        # this else executes only if the break is NEVER 
        # reached and loop terminated after all iterations 
    else : 
        print("list does not contain an even number ")
    count =0 
    while ( count < 1): 
        count = count +1 
        print("count : " , count)
        break
    else : 
        print("No break")

def func9(argument): 
    print("Inside function 9 :  ")
    switcher = {0 :'zero' ,
                1 : 'one' , 
                2 : 'two', 
            }
    # get() method of dictionary data type returns 
    # value of passed argument if it is present 
    # in dictionary otherwise argument will 
    # be assigned as default of passed argument 
    return switcher.get(argument , "Nothing")

def func10():
    # A-C-style way of accessiing lists elements 
    print("Inside func10() : ")
    cars = ['bmw' , 'ford' ,  'aston martin']
    i=0
    while ( i<len(cars)):
        print(cars[i])
        i += 1
    print("Python way of printing list elements : ")
    for i in cars : 
        print(i)
    for i in range(len(cars)): 
        print(cars[i])
    print("Enumerate : ")
    for i , x in enumerate(cars):
        print(x)
    print("Another solution using enumerate : ")
    for x in enumerate(cars): 
        print(x[0] , x[1])
    print("Another way ( single line way ) of enumerateing a list : ")
    print(enumerate(cars))

    #demonstrating the se of start in enumerate 
    print("Starting form 1 ")
    for x in enumerate(cars , start=1): 
        print(x[0] ,x[1])
    print("Starting form 4 ")
    for x in enumerate(cars , start=4): 
        print(x[0] ,x[1])
    # 2 seperate lists 
    cars = ['bmw' , 'aston martin ' , 'audi']
    accessories = ['gps kit ' , 'car repair-tool kit']

    # single dictionary holds prices of cars nad 
    # its accessories 
    # first 3 items store prices of cars 
    # and next 2 items store prices of accessories 
    prices = {1:"570000$", 2:"68000$", 3:"450000$",
            4:"8900$", 5:"4500$"}
    # printing prices for cars 
    for index , c in enumerate( cars , start =1): 
        print("Car : %s Price %s " %(c , prices[index]))
    basket = ['moblile' , 'food' , 'mat']
    ran = ['a' , 'b' , 'c' , 'd']
    prices_2 = {1 : '120' , 2 : '230' , 3 : '340' , 4 : '450' , 
            5 : '560' , 6 : '670' , 7 : '780'}
    for j , x in enumerate(basket , start =1 ):
        print("Item : %s : Price : %s " %(x , prices_2[j])) 
    # printing for the ran lsit 
    for i,x in enumerate(ran , start = 1):
        print("Ran : %s : Price : %s "  %(x , prices_2[j+i]))
        # or 
        # print("Ran : %s : Price : %s "  %(x , prices_2[len(basket)+i]))
        # will give the same output 
    print("Simple zipping code : ")
    list_1 = ['me' , 'you']
    list_2 = [12,34]
    for i,j in zip(list_1 , list_2): 
        print(i , j)
    print("Zipping example 2 : ")
    cars = ["Aston", "Audi", "McLaren"]
    accessories = ["GPS", "Car Repair Kit", 
            "Dolby sound kit"]
    for i,j in  zip(cars , accessories): 
        print("Cars %s : Accessories required : %s " %(i , j))
    # using ( reverse of zip ) with *zip function 

    l1 , l2 =  zip( *[( 'Aston' , 'Gps') , ('Audi' , 'Car repair') , ('Mslaren' , 'Dolby sound kit ') ])
    # printing unzipped lists 
    print( l1) 
    print(l2) 
    list_1 = [1,2,3,4]
    list_2 = ['apr' , 'rt' , 'ty' , 'op']
    zipped = zip(list_1, list_2)
    zip_2 , zip_3 = zip(*zipped)
    print(zip(*zipped))
    print(zip_2, " : " , zip_3)

def func11() : 
    print("Inside function11  : ")
    # defining lists 
    l1 = [1,2,3]
    l2 = [2,3,4]
    # starting time before map 
    # function
    t1 = time.time()
    # calculating result 
    a,b,c = map(operator.mul , l1 , l2 )
    # ending time after map 
    # function
    t2 = time.time()
    # time taken by the map function 
    print("Result : " , a,b,c)
    print("Time taken by the map function is : %.12f " %(t2-t1))

    #calcullating time taken by the naive method 
    t3 = time.time() 
    print("Result : ")
    for i in range(3): 
        print(l1[i]*l2[i] , end=" ")
    t4 = time.time()
    print("\nTime taken by using the naive method : %.12f " %(t4-t3))


def func12() : 
    print("Inside func12() : ")
    print("Indefinite iterator : ")
    # for in loop
    for i in itertools.count(5,5): 
        if i==35: 
            break
        else : 
            print(i , end=" ")
    print("\r")
    print("Cyclic iterator : ")
    count =0
    for i in itertools.cycle('AB'): 
        if count > 7: 
            break
        else : 
            print(i , end=" ")
            count += 1
    print("\r")
    count =0
    for i in itertools.cycle('AB'): 
        if count > 7: 
            break
        else : 
            print(i , end=".")
            count += 1
    print("\r")
    print("Using next function : ")
    l = ['geeks' , 'for' , 'geeks']
    iterators = itertools.cycle(l)
    # for in loop
    for i in range(6): 
        # using next function
        print(next(iterators) , end=" ")
    print("\r")
    for i in range(5): 
        # using next function
        print(next(iterators) , end=" ")
    print("\r")
    print("Combinatorics iterators : ")
    # using repeat(val , num ) 
    #  using repeat() to repeatedly print number 
    print("Printing the numbers repeatedly : ")
    print(list(itertools.repeat(24,4)))
    # repeats 24,4 times 
    print("Using product() in combinatorics iterators : ")
    # product() 
    print("The cartesian product using repeat : ")
    print("Without using repeat : ")
    print(list(itertools.product([1,2])))
    print("Using repeat = 2 : ")
    print(list(itertools.product([1,2], repeat = 2)))
    print()
    print("Using repeat = 3 : ")
    print(list(itertools.product([1,2], repeat = 3)))

    print("The cartesian product of the containers : ")
    print(list(itertools.product(['geeks' , 'for' , 'geeks'] , '2')))
    print()
    
    print("The cartesian product of the containers : ")
    print(list(itertools.product('AB' , [3,4])))
    print()
    print("Permutations : ")
    # permutations () 
    print("All permutations of the given list is : ")
    print(list(itertools.permutations([1 , 'geeks'] , 2)))
    print()

    print("All permutations of the given string : ")
    print(list(itertools.permutations('AB')))
    print()

    print("All permutations of the given container is : ")
    print(list(itertools.permutations(range(3) , 2)))
    print()

    print("Combinations : ")
    # combinations () 
    print("All combinations of list in sorted order ( without replacement )  : ")
    print(list(itertools.combinations(['A' , 2] , 2)))
    print()
    print("All permutations of list : ")
    print(list(itertools.permutations(['A' , 2] , 2)))
    print()

    print("All the combinations of the string in sorted order ( without replacement ) : ")
    print(list(itertools.combinations('AB' ,2)))
    print()
    print("All combinations of list in sorted order ( without replacement ) : ")
    print(list(itertools.combinations(range(2) , 1)))

    print("Combinations with replacements : ")
    # combinations_with_replacements()
    print("All the combinations with replacement of a string in sorted order : ")
    print(list(itertools.combinations_with_replacement('AB' , 2)))
    print()

    print("All combinations of a list in sorted order ( with replacements) :  ")
    print(list(itertools.combinations_with_replacement([1,2] , 2)))
    print()

    print("All combinations of container in sorted order ( with replacement ) : ")
    print(list(itertools.combinations_with_replacement(range(2) ,1)))
    print()

    print("Terminating iterators : ")
    # terminating iterators using accumulate( iter , func) 
    li1 = [1,4,5,7]
    # using accumulate () 
    # prints the successive summation of elements 
    print("The sum after rach iteration : " , end=" ")
    print(list(itertools.accumulate(li1)))
    # 1 
    # 1+4 = 5
    # 5 + 5 = 10 
    # 10 + 7 = 17

    # using accumulate()
    #prints the successive multiplication elements 
    print("The sum after each iteration : " , end=" ")
    print(list(itertools.accumulate(li1 , operator.mul)))
    # 1 
    # 1 * 4 = 4 
    # 4 * 5 = 20 
    # 20 * 7 = 140
    print("Chain : ")
    # chain (iter1 , iter2...)
    li1 = [1,4,5,7]
    li2 = [1,6,5,9]
    li3 = [8,10,5,4]
    #using chain() to print al elements of the lists 
    print("All values in mentioned chain are : " , end=" ")
    print(list(itertools.chain(li1 , li2 , li3)))
    print("Chain.from_terable() : ")
    li1 = [1,4,5,7]
    li2 = [1,6,5,9]
    li3 = [8,10,5,4]
    li4 = [li1 , li2 , li3 ]
    print("All values in mentioned chain are : " , end=" ")
    print(list(itertools.chain.from_iterable(li4)))
    print()
    print("Compress(iter , selector ) : ")
    # compress( iter , selector )
    #using compress() ot selectively print data values 
    print("The compressed values in string are : " , end=" ")
    print(list(itertools.compress('GEEKSFORGEEKS' , [1,0,0,0,0,1,0,0,1,0,0,0,0])))
    print()
    li5 = [1,2,3,4,5,6,7,8,9,10]
    print(list(itertools.compress(li5 , [1,0,0,1,0,0,1,0,0,1])))
    print()
    print("Dropwhile(func , seq) : ")
    li = [2,4,5,7,8]
    #using dropwhile() to start displaying after condiiton is false 
    print("The values after condition returns false : " , end=" ")
    print(list(itertools.dropwhile(lambda x: x%2==0 , li)))
    # 2 % 2 ==0 ... True ... Won't print anything
    # 4 % 2 ==0 ... True ... Won;t print anything
    # 5 % 2 !=0 ... False ... Prints 5 
    # ... Here after all elements are printed even when the condition satisfies ( ie. x %2==0 .. Will still print x hereafter)
    #prints x element from li , when the condition is false 
    print("Filterfalse ( func , seq) : ")
    li = [2,4,5,7,8]
    # using filter false() to print values 
    print("The values that return false to function : " , end=" ")
    print(list(itertools.filterfalse(lambda x : x%2==0 , li)))
    print()

    print("islice : ")
    # isslice(iterable , start , stop , step)
    li = [2,4,5,7,8,10,20]
    # using isslice() to slice the list according to need 
    # starts printing from 2nd index till 6th skipping 2 
    print("The sliced list values : " , end=" ")
    print(list(itertools.islice(li , 1 , 6 , 2)))
    # prints 1st element : 1 
    # prints 3rd element : 7 
    #prints 5th element : 10 
    # after this iterator stops as , stop=6 
    print()
    print("Starmap(func , tuple list) : ")
    li = [(1,10,5) , (8,4,1) , (5,4,9) , (11,10,1)]
    # using starmap()for selection value according to function
    # selects min of all tuple values 
    print("The values according to function are : " , end=" ")
    print(list(itertools.starmap(min , li)))
    # prints the minimum from every part of tuple 
    # (1,10,5) -> minimum = 1 
    # (8,4,1) -> Minimum  1 
    #...
    print()
    print("The values according to function are : " , end=" ")
    print(list(itertools.starmap(max , li)))
    # prints maximum element from each part of the tuple 
    print()

    print("Takewhile function : ")
    # takewhile(func , iterable)
    li = [2,4,6,7,8,10,20]
    # using takehwhile() to print the values till condition is false 
    print("The list alues till 1st false values are : "  , end=" ")
    print(list(itertools.takewhile(lambda x: x%2==0 , li)))
    # This iterator is opposite of 'Dropwhile' 
    # It prints the values till the 1st false condition
    # 2%2=0 ... True ... Prints 
    # 4%2==0 ... True ... Prints 
    # 6%2==0 ... True ... Prints 
    # 7%2==0 ...False ... Does not print 
    # Hereafter it won't print even when the condition is satisfied 
    print()

    print("zip_longest(iterable1 , iterable2 , fillval) : ")
    # using the zip_longest() to combine 2 iterables 
    print("The combined values of iterables is : ")
    print(*(itertools.zip_longest('GosoGes' , 'ekfrek' , fillvalue='_')))
    # prints 
    # G from 1st string , e from 2nd string 
    # o from 1st string , k from 2nd string 
    # s from 1st string , f from 2nd string 
    # ... so on
    # but for s in 1st string , there is not element at the same position in 
    # string 2 , so , it prints the fillvalue instead 
    print()


def func13(): 
    print("Inside func13() : ")
    listA = ['a' , 'e' , 'i' , 'o' , 'u']
    iter_listA  = iter(listA)
    try : 
        print(next(iter_listA))
        print(next(iter_listA))
        print(next(iter_listA))
        print(next(iter_listA))
        print(next(iter_listA))
        print(next(iter_listA))
        # StopIterationError
    except : 
        print("Throwing StopIterationError , inside except block")

    print("Exmaple -2 : ")
    lst = [11,22,33,44,55]
    iter_lst = iter(lst)
    while True : 
        try : 
            print(iter_lst.__next__())
        except : 
            break
    
    print("Example 3 : ")
    listB = ['cat ', 'bat' , 'sat' , 'mat']
    iter_listB = listB.__iter__()
    try : 
        print(iter_listB.__next__())
        print(iter_listB.__next__())
        print(iter_listB.__next__())
        print(iter_listB.__next__())
        #StopIterationError
    except : 
        print("Throwing StopIteratorError , inside Except block")

    print("For user-defined functions : ")
    class Counter : 
        def __init__(self , start , end): 
            self.num = start 
            self.end = end 
        def __iter__ ( self): 
            return self 
        def __next__(self):
            if self.num> self.end: 
                raise StopIteration
            else : 
                self.num +=1 
                return self.num-1
                






func1()
func2()
func3()
func4()
func5()
func6()
func7()
func8()
argument = 0
print(func9(argument))
argument = 11
print(func9(argument)) 
func10()
func11() 
func12()
func13()
