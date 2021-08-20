


def f1() :
    print(6000+4523.5+134.12)
    print(+ 1000)
    principle = 1000
    rate = 0.05 
    numyears = 5 
    year =1 
    while year<=numyears :
        principle = principle * (1+rate) 
        print("year : " , year , " princple : " , principle)
        year = year +1 
    principle = 1000
    rate = 0.05 
    numyears = 5 
    year =1
    print()
    while year <=numyears : 
        principle = principle * ( 1+rate )
        print("year : %3d " %(year) , "principle : %0.2f" %(principle))
        print("year : {0:3d}" .format(year) , " principle : {0:.3f}" .format(principle))
        
        print()
        year = year + 1 

    age = input("Age : ")
    print("Age : " , age )
    # if and else statements 
    # comments 
    myName = input () 
    print("My name is : " , myName)
    print("Length of your name : " ,len(myName))
    print(len('i am ' + 'a person'))
    print('i am ' + str(23) + ' for a person')
    spam = int(input())
    print("spam : " , spam)
    print('you will be ' + str(spam+1) + ' years, the next year')

def f2()  :
    spam = True 
    print("spam value: " , spam)
    
    # comparison operators 
    print(12==12)
    print(12!=34)
    print(12/12==1)
    print(12/12!=1)
    print(12<11)
    print(12>11)
    print(12<=10)
    print("String comparison : ")
    print('atharva'=='atharva')
    print('apple' == 'banana')
    print('api' == 'sbi')
    print(len('api')==len('sbi'))
    print('a' + 'b'== 'b'+'a')
    print("Boolean values : ")
    print(True and True)
    print(True or True)
    print(True and False )
    print(False and False)
    print(not True)
    print(not False)
    print("Mixing boolean and comparator operators : ")
    print((4<5) and (5>4))
    print((4<5) and (5<4))
    print((1==2 ) or (2==2))

    name = 'Carol'
    age = 3000
    if name =='Alice': 
        print("Hi, Alice")
    elif name =='Carol':
        print('Hi, Carol')
    elif name =='atharva': 
        print("hi , atharva")
    elif age >200: 
        print('age > 200')
    else : 
        print("Inside the else clause ")

    if name =='Alice': 
        print("Hi, Alice")
    elif age >200: 
        print('age > 200')
    elif name =='Carol':
        print('Hi, Carol')
    elif name =='atharva': 
        print("hi , atharva")
    else : 
        print("Inside the else clause ")
    
    number = 0 
    while True : 
        print("Amazing tshirt")
        if number>4 :
            break
        number = number +1 
    print()
    number =0
    while True : 
        if number > 4 : 
            break
        elif number ==3 : 
            number = number +1 
            continue
        print("Amzing trouser ")
        number = number +1 
    
    numguests = int(input() )
    if numguests: # executes when numguests!=0
        print("Hello there")
    print()

def f3()  :
    # for loops and range() function
    print('my name is : ')
    for i in range(3): 
        print("atharva")
    print()
    print("2nd iteration : ")
    for i in range(3) :
        if i==2 : 
            continue
        print("aditya")
    print()

    total =0
    for i in range(101) :
        total = total + i 
    print(total)

    i=0
    while i< 4 : 
        print('atharva')
        i = i+1 
    
    import random 
    for i in range(5) :
        print(random.randint(1,10))
    print()

    # termiating the program before 
    # the intrepretor reaches the end 
    # usig sys module
    import sys 
    while True : 
        print("type to exit : ")
        response = input() 
        if response =='exit': 
            sys.exit()
        print('Response : ' , response)
        break

    print("After the loop")

def f4()  :
    # Guess the number 
    import random
    print("Guess a number between 1 and 10 : ")
    inp = int(input())
    if inp == random.randint(1,10): 
        print("Guessed te right number " , inp)
    

def f5()  :
    #Game of Rock Papers and Scissors 
    import random 

    comp_point=0
    your_point =0
    counter =0
    
    while counter<3: 
        comp = random.randint(1,3)
        print("Enter a number : ( 1-Rock : 2-Paper : 3-Scissors) ")
        guess = int(input())
        if guess==comp: 
            print('Tie')
        elif guess==1 and comp==2: 
            print("Rock defeated paper, comp point")
            comp_point = comp_point +1 
        elif guess==2 and comp==3 : 
            print("Scissors cuts paper , your point")
            your_point = your_point +1 
        elif guess==3 and comp==1: 
            print("paper covers rock, your point")
            comp_point = comp_point+1
        counter = counter +1 
    
    print("Score : ")
    print("your points : " , your_point)
    print("comp's points : " , comp_point)
    if your_point>comp_point: 
        print("You Won ! ")
    elif your_point<comp_point: 
        print("You loose :(")
    else : 
        print("It's a Tie")



    
    



    









#f1()
#f2() 
#f3()
#f4()
f5()  