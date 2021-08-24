#include<iostream>
#include<cstring>
#include<vector>
#include<ctime>
//#include<array>
using namespace std;

void pointer();
void pointer2();
void pointer3();
void pointer4() ;
char* getname();
void vector_template();
void program1();
void test();
void program2();
void program3();
void Loops();
void factorial();
void Loops2();
void comparing_string();
void do_while();
void range_based();

union con4all
{
    int int_val;
    long long_val;
    double double_val;
};

struct Widget
{
    char brand[20]; //format depends on widget type
    int type ;
    union id
    {
        long id_num ;   // type 1 widgets
        char id_char[20];   //other widgets

    }id_val;
};

struct inflatable
{
    char name[20];
    float volume ;
    double price ;

};

struct antartica
{

    int year ;
};

struct info
{
    char fname[20];
    char lname[20];
    char grade;
    int age ;

};

struct CandyBar
{
    char brand[20];
    float weight;
    int calories ;
};

struct food
{
    int number ;
}pizza;
int main()
{
    cout<<"\nHey there ! \n";

    //unions
       con4all pail;
       pail.int_val = 14;
       pail.long_val = 12l;
       pail.double_val = 12.4321d;
       cout<<"\npail int_val : "<<pail.int_val;
       cout<<"\npail long_val : "<<pail.long_val;
       cout<<"\npail double double_val : "<<pail.double_val<<"\n";
       //struct
       Widget prize;
       if(prize.type==1)
       {
           prize.id_val.id_num = 20;
           cout<<"\nprize.id_val.id_num ; "<<prize.id_val.id_num;
       }
       else
       {
           prize.id_val.id_char[0] = 'r';
           cout<<"\nprize.id_val.id_char : "<<prize.id_val.id_char[0];
       }
    //enumerations
       enum spectrum {red , oraange , yellow , green , blue , violet , indigo , ultraviolet};

       spectrum band;   // band a variable of type spectrum
       band = blue ;    // valid , as blue is an enumerator
       //band =2000;  // invalid, 200 is not an enumerator
       int color = blue;
       //band =3 ;    // invalid, int is not converted to spectrum
       //band = 3+ red ;  // valid, red converted to int
       band = spectrum(3);  //type cast to type spectrum , valid
       //band = spectrum(1000); //invalid , because 1000 index does not exists in the spectrum

       //setting enumerator values
       enum bits{one =1, two=2 ,four=4 , eight =8};
       //the assigned values must be an integer
       enum bigstep {first , second = 2,  thousand = 1000,third };  //valid
      //creating more than one enumerator at the same time
      enum { zero , null=0 , one_2 , number=1};
      //Here both zero and null are = 0  and both one and number are 1
      bits myflag ;
      myflag = bits(6);     //valid , because 6 is in bits range

      cout<<"\nbits myflag : "<<myflag;
      cout<<"\n";

      //pointer
      int donuts = 6 ;
      double cups = 4.5;

      cout<<"\nDobuts valus : "<<donuts;
      cout<<"\nand donuts address  : "<<&donuts<<"\n";
      // note - you may need o use unsigned ( &donuts)
      // and unsigned ( &cups)
      cout<<"\ncups calus : "<<cups ;
      cout<<"\nand cups address : "<<&cups<<"\n";

      int updates = 6 ;     //declare a variable
      int *p ;      //declare an integer pointer
      p = &updates ;     //assign addreess of int to pointer
      //express values in 2 ways
      cout<<"\nvalus : "<<updates ;
      cout<<"\n*p_updates : "<<*p;

      //express address in 2 ways
      cout<<"\nAddress &updates : "<<&updates;
      cout<<"\np_updates address : "<<p;

      //use pointer to change values
      *p = *p +1;
      cout<<"\nNew value of the pointer : "<<*p<<"\n";

      //declaring and initializing pointers
      int *p_updates , p1=12;
      cout<<"\np1  : "<<p1;
      // here p_updats is  a pointer but p1 is not a pointer

      int higgens = 6 ;
      int *pt = &higgens ;
      cout<<"\npt : "<<*pt;
      cout<<"\nvalue if higgens : "<<higgens;
      cout<<"\nAddressf higgens : "<<&higgens;
      cout<<"\nAddress stored in pt pointer : "<<pt<<"\n";

      int *ptr ;
      //ptr  = 0xB8000000;        //type mismatch , the left side of the equation is an integer , but hte right side of the equation is 0xB8000000, it does not state wheather its an integer or an address
      // hence we use type conversion
      // so
      ptr = (int *) 0xB8000000;     //valied ,  as the 0xB8000000 is now an integer pointer , ie -a memory address
    cout<<"\nptr stored address  :"<<ptr<<"\n";

    // using new
    //int* pn =  new int ;
    //int higgens ;
    //int* pt = &higgens ;

    //code snippet
    int nights = 1001 ;
    int* pt_nights = new int ;
    *pt_nights = 1000 ;     //store a value there

    cout<<"\nnights value : "<<nights;
    cout<<"\nnights address : "<<&nights;
    cout<<"\npt pointer value : "<<*pt_nights ;
    cout<<"\npt pointer stored address  : "<<pt_nights<<"\n";
    //deleting a pointer
    delete pt_nights ;
    // this does not remove the pointer itself
    // but it frees up the memory that it stored
    int* ps = new int ;
    delete ps ;
    int jugs = 5 ;
    int* pt_jugs = &jugs ;
    delete pt_jugs ;
    int* ps_1 =new int ;
    int* pq = ps_1 ;         // set the second pointer to the same block
    delete pq ;     //delete the second pointer

    //dynamic array with new
    int* psome = new int[10];       //get a block of 10 ints
    delete [] psome ;       //frees up the dynamic memory
    int *pt_1 = new int;
    short* psamosa= new short[500];
    delete pt_1;
    // delete ps_1;     //invalid behaviour, can't do it
    delete [] psamosa;

    double* p3 = new double[3] ;
    p3[0] = 0.2 ;
    p3[1] = 0.5 ;
    p3[2] = 0.8 ;
    cout<<"\np3[1] : "<<p3[1];
    p3 = p3+1;      //increment the pointer
    cout<<"\np3 now : "<<p3[0];
    cout<<"\np3[1] : "<<p3[1];
    p3 = p3-1;
    delete [] p3 ;

    //pointers , arrays and pointer arithmetic
    double wages [3] = {1000,2000,3000};
    short stacks[3] = {3,2,1};

    // Here are 2 ways to get the address of an array
    double* pt_wages = wages ;
    short* pt_stacks = stacks ;

    // with array element
    cout<<"\npt_wages : "<<*pt_wages ;
    cout<<"\npt_wages address stored : "<<pt_wages ;
    cout<<"\nAdding one to the pointer : ";
    pt_wages = pt_wages + 1 ;
    cout<<"\npt wages : "<<*pt_wages ;
    cout<<"\npt_wages address stored : "<<pt_wages<<"\n" ;

    // similarly for pt_stacks
    cout<<"\npt_stacks : "<<*pt_stacks;
    cout<<"\npt_stacks address stored : "<<pt_stacks;
    cout<<"\nAdding one to the pointer of pt_stacks : ";
    pt_stacks = pt_stacks + 1;
    cout<<"\npt_stacks now  : "<<*pt_stacks ;
    cout<<"\npt_stacks address stored : "<<pt_stacks <<"\n";

    cout<<"\nwages[0]  : "<<wages[0];
    cout<<"\nwages[0] address stored  : "<<&wages[0];
    cout<<"\nstacks[0] : "<<stacks[0];
    cout<<"\nstacks[0] address stored  : "<<&stacks[0];

    cout<<"\nstacks : "<<*(stacks+1);
    cout<<"\nstacks : "<<*(stacks+2);
    cout<<"\nstakcs [0] value  : "<<stacks[0];

    cout<<"\nstacks whole address : "<<&stacks;
    //double* pn;       //pn can point to a double value
    // char* pc;        // pc can point to char value
    double* pn;
    double* pa;
    char* pc ;
    double bubble = 3.2 ;
    pn = &bubble;
    pc = new char ;
    pa = new double[30];        // aasign the address of the first element of the array of 30 double to pa

    // dereferencing the pointers
    cout<<*pn<<"\n";
    *pc = 's';      // place 's' into the emory location whose address  is pc
/*
    int tacos[3] ={1,2,3};
    int* pt_tacos = tacos ;
    pt_tacos = pt_tacos +1 ;
    cout<<"\npt_tacos address stored  : "<<pt_tacos;
    cout<<"\npt_tacos value : "<<*pt_tacos ;
    cout<<"\nsize of integer : "<<sizeof(int);
    pt_tacos = pt_tacos -1;
    delete pt_tacos;
   */
    pointer();

/*
    //pointer and strings
    char flower[10] = "rose";
    cout<<"\n"<<flower<<"s are red\n";
    // prints the entire string using the address of the character
    //ie- here flower is the address of the character
    // so, the program prints everyting from the start to the '\0' character of flower
    // hence, we get the entire string
*/

    //using strlen() and strspy()
    //pointer2();
    //pointer3() ;
    //pointer4() ;
    //vector_template();
    //program1();
    //test();
    //program2();
    //program3();
    //Loops();
    //factorial();
    //Loops2();
    //comparing_string();
    //do_while();
    range_based();


    return 0;

}

void pointer()
{
    int tacos2[3] = {1,2,3};
    int* pe_tacos = tacos2;
    pe_tacos = pe_tacos +1 ;
    cout<<"\npe_tacos value : "<<*pe_tacos;
    cout<<"\npe_tacos addresss : "<<pe_tacos;
    pe_tacos = pe_tacos + 1 ;
    cout<<"\npe_tacos value updated : "<<*pe_tacos ;
    pe_tacos = pe_tacos -2;
    cout<<"\ntacos2 value using address : "<<*tacos2;
    cout<<"\ntacos2 next value using address : "<<*(tacos2+1);    cout<<"\npe_tacos value : "<<*pe_tacos;
    delete pe_tacos ;
}
void pointer2()
{
    char animal[20] = "bear";
    const char* pt_bird = "wren";
    char *ps ;

    cout<<"\n"<<animal;
    cout<<"\n"<<pt_bird;

    ps = animal ;
    cout<<"\nanimal momery address : "<<(int * ) animal;
    cout<<"\nps value : "<<ps;
    cout<<"\nvalue of ps before stirng copy : "<<ps ;

    char* pt;
    pt= new char[strlen(animal) +1];       //get a new storage
    strcpy(pt, animal);        //copy string to new storage
    cout<<"\nAfter using strcpy() : ";
    cout<<"\nAnimal at : "<<(int * )animal<<" is "<<animal;
    cout<<"\npt at "<<(int * )pt <<" is "<<pt;
    delete [] ps ;
    delete [] pt ;

    //here "wren" actually holds the address of the string
    cout<<"\nA concerned " <<pt_bird <<"\n";
    char* pt_animal = animal;
    cout<<"\npt_animal : "<<pt_animal;
    cout<<"\npt_animal address where the string is found : "<<(int * )pt_animal;

    delete pt_animal;
    delete pt_bird ;

}

void pointer3()
{
    char animal[10] = "tiger";
    char* ps_new ;
    ps_new = animal;    //
    ps_new=  new char[strlen(animal)+1];    //increases the size of ps_new
    cout<<"\nps_new : "<<ps_new; // won;t display anything , because the new memory contains nothing
    char* pt_new ;
    pt_new = new char[strlen(animal) +1 ];  // allocates a new memory of that size  , and points towards it
    strcpy(pt_new , animal);    // copies the contents of animal to pt_new
    cout<<"\npt_new : "<<pt_new;    //diaplys animal string
    // ie - tiger

    char food[20] = "carrots ";
    strcpy(food , "spinach");
    cout<<"\nfood value : "<<food;
    //when the food array is smaller than the string , then
    //strcpy(food , "this is an oversized string , lets see what will happen");
   // cout<<"\nfood value now : "<<food;
    // will cause the program to close midway

    // so , instead of strcpy() use strncpy()
    strncpy(food, "this is an oversized sting , lets see what will happen",20);
    cout<<"\nfood value now : "<<food<<"\n";
}

void pointer4()
{
    // Using pointer to create dynamic structures
    inflatable* ps = new inflatable ;
    // use the '.' operator with structure name
    // use the '->' operator with pointer-to -structure
    cout<<"\nEnter name of inflatble item  ";
    cin.get(ps->name ,20 ); // method 1 for member access
    cout<<"nEnter volume in cubic feet  : ";
    cin>>(*ps).volume;      // method 2 for member access
    cout<<"\nEnter price : ";
    cin>>ps->price ;        // method 3 for member access
    cout<<"\nName : "<<(*ps).name;
    cout<<"\nvolume : "<<ps->volume;
    cout<<"\nprice  : "<<ps->price;
    delete ps ;

    // an example of using new and delete
    char* name ;        //create a pointer but no storage
    name = getname();       // assign address os string to name
    cout<<"\n"<<name<<" at "<<(int *) name;
    delete [] name ;        //freed memory

    name = getname() ;       // reused the freed memory
    cout<<"\n"<<name<<" at "<<(int * )name;
    delete [] name;         // freed memory

    // automatic storage, static storage and dynamic storage
    antartica s01, s02,s03 ;
    s01.year = 1998;
    antartica* pa = &s02;
    pa->year = 1999;
    antartica trio[3];      //array of  3 structures
    trio[0].year = 2000;
    cout<<"\ntrio year : "<<trio->year;
    const antartica* arp[3] = {&s01,&s02,&s03};
    cout<<"\narp[1]->year : "<<arp[1]->year;
    const antartica** pp = arp;
    const antartica** ppb = arp;
    cout<<"\nppa year : "<<(*pp)->year;
    cout<<"\nppb year : "<<(*(ppb+1))->year;

}

char* getname()
{

    char temp[80];      //temporary storage
    cout<<"\nEnter last name : ";
    cin>>temp;
    char* pn = new char[strlen(temp) + 1];
    strcpy(pn , temp);      // copy string into smaller space
    return pn;
}
/*
void vector_template()
{

    vector<int> v1 ;        //creates a zero-size array of int
    int n ;
    cin>>n;
    vector<double>v2(n);        // create an array of n double

    //an array object of 5 units
    // including array header file
    array<int , 5>a1;       // create an array object of 5 units
    array<double,4>ad = {1.2,2.3,4.5,5.6};
}*/

void program1()
{
    info* pointer = new info;
    cout<<"\nEnter first name : ";
    cin.get(pointer->fname,20).get();
    cout<<"\nEnter last name : ";
    cin.get(pointer->lname ,20).get();
    cout<<"\nEnter grade : ";
    cin.get(pointer->grade).get();
    cout<<"\nEnter age : ";
    cin>>pointer->age;
    cout<<"\nName : "<<pointer->lname<<" , "<<pointer->fname;
    cout<<"\nGrade : "<<char(pointer->grade+1);
    cout<<"\nAge : "<<pointer->age;
    delete pointer ;

}

void test()
{
    char name[20];
    cout<<"\nEnter name  : ";
    cin.get(name , 20 ).get();
    cout<<"\nName : "<<name;
    char fname[20];
    cout<<"\nEnter a string : ";
    cin.get(fname , 20 );
    cout<<"\nString : "<<fname;

}

void program2()
{
    cin.get();
    char fname[20];
    char lname[20];
    cout<<"\nEnter first name : ";
    cin.get(fname, 20 ).get();
    cout<<"\nEnter last name : ";
    cin.get(lname, 20).get();
    strcpy(fname , strcat(fname , " , "));
    cout<<"\nFinal name : "<<strcat(fname, lname);
}

void program3()
{

    CandyBar snack ;
    cout<<"\nEnter Brand : ";
    cin.get(snack.brand , 20).get();
    cout<<"\nEnter weight : ";
    cin>>snack.weight;
    cout<<"\nEnter calories : ";
    cin>>snack.calories;
    cout<<"\nBrand Name : "<<snack.brand;
    cout<<"\nWeight : "<<snack.weight;
    cout<<"\nCalories : "<<snack.calories;
    pizza.number = 12;
    cout<<"\nPizza number : "<<pizza.number;
    food* pointer = new food ;
    cout<<"\nEnter food  number : ";
    cin>>pointer->number;
    cout<<"\nFood number : "<<pointer->number;
    delete pointer;

}

void Loops()
{
    int i;      //create a counter ;
    // initialize the counter ;
    for (i=0;i<5;i++)
    {
        cout<<"\nInside a loop, prints 5 times";
    }
    // a reverse loop
    cout<<"\n";
    int limit;
    cout<<"\nLimit : ";
    cin>>limit;
    for(i=limit;i;i--)  //quits when i ==0
    {
        cout<<"\nLimits "<<i;
    }
    int x;
    cout<<"\nNow the expression has the value : ";
    cout<<(x=100);
    cout<<"\nNow x : "<<x;
    cout<<"\nThe expression x<3 has the value : ";
    cout<<(x<3);
    cout<<"\nThe expression x>3 has the value : ";
    cout<<(x>3);
    cout.setf(ios_base::boolalpha);    // a newer , C++ feature
    cout<<"\nThe expression x<3 has the value : ";
    cout<<(x<3);
    cout<<"\nThe expression x>3 has the value : ";
    cout<<(x>3);

}

void factorial()
{

    const int number = 16;
    long long factorials[number];
    factorials[1]=factorials[0]=1LL;
    for(int i=2;i<number;i++)
    {
        factorials[i] =i*factorials[i-1];
    }
    cout<<"\nDisplaying factorials ";
    for ( int i=0;i<number;i++)
    {
        cout<<"\n"<<i<<"! : "<<factorials[i];
    }
}

void Loops2()
{
    int number ;
    cout<<"\nEnter a number : ";
    cin>>number ;
    for(int i=0;i<100;i = i+number )
    {
        cout<<"\n"<<i;
    }
    string word ;
    cout<<"\nEnter a word : ";
    cin>>word;
    for(int i=word.size()-1 ; i>=0;i--)
    {
        cout<<"\n"<<word[i];
    }

    // ++p operator and p++ operator
    int a = 20 ;
    int b = 20 ;
    cout<<"\na : "<<a<<"\nb : "<<b;
    cout<<"\na++ : "<<a++<<"\n++b : "<<++b;
    cout<<"\na : "<<a<<"\nb : "<<b;

    int z =5;
    int y = ++z ;
    cout<<"\ny : "<<y ;
    cout<<"\nz : "<<z;
    int x = 5 ;
    int j = x++;
    cout<<"\nj : "<<j;
    cout<<"\nx : "<<x;

    //increment and decrement operators and pointers
    double arr[5] = {21.1 , 32.8 , 45.2 ,37.8};
    double* pt = arr ;
    cout<<"\npt : "<<*pt;
    ++pt ;
    cout<<"\npt  : "<<*pt;
    ++*pt;
    cout<<"\npt : "<<*pt;
    *++pt ;
    cout<<"\npt : "<<*pt;

    //function for average
    int limit ;
    cout<<"\nEnter entries : ";
    cin>>limit;
    float sum ;
    for(int i=0;i<limit;i++)
    {
        int get ;
         cout<<"\nEnter number : ";
         cin>>get;
         sum = sum + get ;
    }
    float avg = sum / limit ;
    cout<<"\nAverage : "<<avg;

    //reversing a string
    string letters;
    cout<<"\nEnter a word : ";
    cin>>letters ;
    char temp;
    int i,k ;
    for (k=0,i=letters.size()-1; k<i; i-- ,k++)
    {
        temp = letters[i];
        letters[i] = letters[k];
        letters[k] = temp;
    }
    cout<<"\nReversed word : "<<letters;
    //printing ASCII characters
    char ch;
    for(ch='a' ; ch<='z' ; ch++)
    {
        cout<<"\n"<<ch;
    }

    char word2[5] = "?ate";
    for (char ch ='a' ; strcmp(word2 ,"mate") ; ch++)
    {
        cout<<"\n"<<word2;
        word2[0] = ch;
    }
    cout<<"\nLoop ends here, because word == mate ";
    char word3[5] = "mate";
    cout<<"\nchecking : "<<(strcmp(word3 , "mate"));
    // prints false
    // the reason is that no 2 strings are the same

}

void comparing_string()
{

    string word4 = "?ate";
    for ( char ch='a' ; word4!="mate" ; ch++)
    {
        cout<<"\n"<<word4;
        word4[0] = ch;
    }
    cout<<"\nAfter this the loop ends : ";

    //while loop
    const int number = 20 ;
    char name[number];
    cout<<"\nEnter your name : ";
    cin>>name;
    int i=0;
    while(name[i]!='\0')
    {
        cout<<"\n"<<name[i]<<" : "<<int(name[i]);
        i++;
    }
    cout<<"\nEnd of the loop : ";

    // clock time program
    cout<<"\nEnter the delay time , in seconds : ";
    float secs;
    cin>>secs;
    clock_t delay = secs*CLOCKS_PER_SEC;     //convert to clock ticks
    cout<<"\nStarting : ";
    clock_t start = clock();
    while(clock() - start < delay )     //wait until the time elapses               // note the esemicolon
    ;
    cout<<"Done ";

}

void do_while()
{
    int n;
    cout<<"\nEnter numbers in the range 1-10 to find my favorite number :  ";
    do
    {
        cin>>n; //execute the body
    }while(n!=7);       // then test
    cout<<"\nYes, 7 i s my favourite number ";
}

void range_based()
{
    int prices[5] = {11,22,33,44,55};
    int x=0;
    for ( x : prices )
    {
        cout<<"\n"<<x;
    }

    char ch;
    int count=0;
    cout<<"\nEnter characters, enter # to quit : ";
    cin>>ch;
    while ( ch!='#')
    {
        cout<<ch;
        count ++ ;
        cin>>ch;
    }
    cout<<"\n"<<count<<" characters printed ";
    // this however does not count 'spaces' character

    // to solve this problem, use cin.get(char)
    cout<<"\nUpdated program : ";
    char chr ;
    count =0;
    cout<<"\nEnter characters, enter # to quit : ";
    cin.get(chr);   // take the first character
    while (chr!='#')
    {
        cout<<chr;      //echo the character
        count ++;   // incrementing operation
        cin.get(chr);     // take the next input
    }
    cout<<"\n"<<count<<" character printed : ";
    count =0;
    char chr1;
    cout<<"\nEnter something and type '#' to stop  : ";
    cin.get(chr1);
    while (cin.eof()==false)
    {
        cout<<chr1;
        count++;
        cin.get(chr1);
        if(chr1=='#')
        {
            break;
        }
    }
    cout<<"\n"<<count<<" characters printing";
    char chr2 ;
    cout<<"\nEnter a character : ";
    chr2  = cin.get();
    cout.put(chr2);

}

