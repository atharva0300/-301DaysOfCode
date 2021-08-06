from sys import stdin , stdout


def func1() : 
    # python program showing 
    # a use of input () 
    val = input()
    print(val)
    # input () automatcally identifies the data type of the input 
    # whereas war_input does not 
    # also raw_input() hasbeen renamed to input() in python 3 

def func2()  : 
    # taking input from a console 
    pass
def func3() :
    # using split() in pytonh 
    x,y = input("Enter 2 numbers :  ").split()
    print(x,y)
    # taking 2 inputs at a time 
    a,b = input("Enter a number : ").split()
    print("First number : {} and second number : {} " .format(a,b))

    #taking multiple inputs at a time 
    # and type casting them using the list() function
    x = list(map(int , input("Enter 2 numbers :  ").split()))
    print("List : " , x)

    # USING LIST COMPREHENSION
    # taking 2 inputs at a time 
    x, y = [int(x) for x in input("Enter 2 values number : ").split()]
    print("First numbner : " , x)
    print("Second number : " , y)

    # taking the three input ar a time 
    x,y,z = [int(x) for x in input("Enter 3 number : ").split()]
    print(x,y,z)

    # taking multiple inputs at a time 
    x = [int(x) for x in input("Enter multiple values : ").split()]
    print("list : " , x)

def func4() : 
    # input via readline method 
    n = stdin.readline() 
    print(n)
    print("After realdine")
    # array input similar method 
    arr=  [int(x) for x in stdin.readline().split()]

    #initialize summation
    sum = 0
    # calculate sum
    for x in arr: 
        sum +=x

    print(sum)

    def get_ints() :
        import sys
        return list(map(int,sys.stdin.readline().strip().split()))

    a= get_ints()
    print("list : " , a)

    # taking input string 
    def get_string() :
        import sys
        return sys.stdin.readline().strip()
    
    string = get_string()
    print(string)

    # getting individual words from the string 
    print("Words ")
    def get_words() :
        import sys
        return list(map(str ,sys.stdin.readline().strip().split()))
    
    words = get_words()
    print("words in the list : " , words)

    import atexit,io,sys
    # a stream manipulation using an in-memory bytes 
    # buffer. It inherits BufferedOBase
    

def func5(): 
    import random
    secret_number = random.randint(1,500)
    print("Pick a number : " )
    while True : 
        res = input("Guess a number : ")
        if ( res==secret_number): 
            print("You win!")
            break
        elif (res=='.'): 
            break
        else : 
            print("You lose")
            continue


    # function name as a parameter 
    secret_value = 500
    # function that returns the secret value 

def func6() : 
    import time 
    count_seconds = 3 
    for i in reversed(range(count_seconds+1)): 
        # reversed(range) = 3,2,1 ofr count_seconds strts with 3 

        if i>0: 
            print(i,end=">>>")
            time.sleep(1)
        else : 
            print('start')

    print("Before sleep of 2 sec ")
    time.sleep(2)
    print("After sleep of 2 secs ")

    import io
    # declare a dummy file 
    dummy_file = io.StringIO()

    # add a message to the dummy file 
    print("Hello! this is a dummy file" , file = dummy_file)

    # get the value from dummy file 
    dummy_file.getvalue()

def func7() : 
    pass 

def func8() : 
    pass 

def func9()  :
    # sep() parameter in python
    print('a' , 'b' , 'c', sep=",")
    # seperates eahc '<character' under '' by a 
    # comma 

    import antigravity 

def func10() : 
    # output formatting 

    # print integer and float value 
    print("Geeks : %2d ,Portal : %5.2f " %(1,5.333))
    # prints the intger till 1 decimal places 
    # so prints 1 
    # prints the portal till 5 decimal places 
    # and 2 places of decimals after the point 
    # so  , prints 5.33
    # similarly 

    print("Total students : %3d, Boys : %2d " %(240,120))

    # print the octal value 
    print("%7.3o " %(25))
    # here %7 is the spaces gap 
    # ie - the resutl will be printed after 7 spaces

    #prints exponential value 
    print("%.3E " %(239.12345))





    



    

#func1()
#func3()
#func4() 
#func5()
#func6()  
#func9()
func10()