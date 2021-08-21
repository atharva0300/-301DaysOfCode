#include<iostream>
#include<cstring>
#include<string>

using namespace std;


void using_getline();
void using_get();
void using_get_with_newline();
void cin_clear();
void string_class();
void string_class_2();
void string_operations();
void other_string();
void structures();
void unions();
void enumerations();
void pointers() ;

int main(){ 

    double constants = 1e7/9.0;
    cout<<"\nDOUBLE CONSTANTS  : "<<constants<<"\n";
    const int lbs_to_stone = 14;
    int lbs ;
    cout<<"\nEnter in lbs : ";
    cin>>lbs ;
    int stone = lbs /lbs_to_stone;
    int pounds = lbs%lbs_to_stone;
    cout<<"\nResult : "<<stone<<" stone and "<<" "<<pounds<<" pounds"<<"\n";
    short thirty = 30;
    long so_long = thirty;
    cout<<"\nSo_long : "<<so_long<<"\n";
    cout<<"\nSize of so_long : "<<sizeof(so_long)<<"\n";
    long number = 2111222333;
    float a =number ;
    cout<<"\na : "<<a<<"\n";

    // type conversion 
    cout.setf(ios_base::fixed , ios_base::floatfield);
    float tree=3;
    int guess = 3.9832;
    //int debt = 7.2e12;
    int debt = 4;
    cout<<"\ntree : "<<tree;
    cout<<"\nguess : "<<guess;
    cout<<"\ndebt : "<<debt<<"\n";

    short chickens = 20 ;
    short ducks = 35;
    short fowl = chickens + ducks ;
    cout<<"\nfowl : "<<fowl<<"\n";
    char c1 = 66;
    cout<<"\nchar c1 : "<<c1<<"\n";
    cout<<"\nint of q : "<<int('q')<<"\n";
    cout<<"\nlong of q : "<<long('q')<<"\n";

    cout<<"\nstatic_cast : "<<static_cast<long>('q')<<"\n";
    int auks , bats , coots;

    // the following statement adds the values as double 
    // then converts the result to int 
    auks= 19.99   + 11.99;

    // theses statements add values as int 
    bats = (int)19.99 + (int)11.99;
    coots = int(19.99) + int(11.99);
    cout<<"\nauks : "<<auks <<"\nbats : "<<bats;
    cout<<"\ncoots : "<<coots<<"\n";

    // auto declarations in C++ 
    auto n = 100; // n is int 
    auto x = 1.5; // x i double 
    auto y = 1.3e12L; // y is double long 

    cout<<"\nn: "<<n<<"\nx : "<<x<<"\ny : "<<y<<"\n";
    auto b = 0.0; // ok , x is double because 0.0 s double 
    double c = 0; // ok, 0 automatically converted to double 0.0
    auto d =0; // oops , z is int because 0 is int 
    cout<<"\nz : "<<d<<"\n";

    //compound types 
    // arrays
    short months[12];
    int yams[3];
    yams[0] = 7;
    yams[1] = 8;
    yams[2] = 6;
    int yamcosts[3] = {10,20,30};
    cout<<"\ntotal yams : "<<yams[0]+yams[1]+yams[2];
    cout<<"\nThe package with : "<<yams[1]<<" yams cost : "<<yamcosts[1];
    int total = yams[0]*yamcosts[0] + yams[1]*yamcosts[1] + yams[2]*yamcosts[2];
    cout<<"\ntotal costs : "<<total<<"\n";

    cout<<"\nSize of yams array : "<<sizeof(yams);
    cout<<"\nSize of one element : "<<sizeof(yams[0])<<"\n";
    short things[] = {1,5,6,7};
    int num_elements = sizeof(things)/sizeof(short);
    cout<<"\nnum_of_elements : "<<num_elements<<"\n";
    unsigned short e[2] = {} ;
    cout<<"e : "<<e[0]<<" e : "<<e[1]<<"\n";
    //long plifs[] = {25,92,3.0}; //not allowed 
    //cout<<"\nplifs : "<<plifs[0]<<"\n";

    char tlifs[4] = {'h' , 'i' , 112 , '\0'}; //allowed 
    cout<<"\ntlif[2] : "<<tlifs[2]<<"\n";

    char dog[8] = {'b' , 'e' ,'a' , 'u' ,'x' ,' ' ,'i' , 'i'}; // not a string 
    char cat[8] = {'f' , 'a' ,'t'  ,'e'  , 's' , 's', '\0'}; //a string  
    cout<<"\ndogs : "<<dog<<"\ncats : "<<cat<<"\n";
    //strings 
    char bird[11] = "Mr. Cheeps";
    char fish[] = "Bubbles";
    cout<<"\nbird  : "<<bird<<"\nfish : "<<fish<<"\n";

    //concatenating strings 
    cout<<"atharva is " " super cool";
    cout<<"\ni am "
    " super nice person\n";

    //strlen() 
    const int size = 15;
    char name[size]; //empty array 
    char name2[size ] = "C++owboy"; //initialized array 
    //NOTE : some implementations ma require the static keyword 
    // to initialize the array name2 

    cout<<"\nHowdy ! , I'm : "<<name2;
    cout<<"\n!What's your name ? ";
    cin>>name;
    cout<<"\nName is : "<<name;
    cout<<"\nstrlen() of name : "<<strlen(name);
    cout<<"\nsizeof name : "<<sizeof(name);
    cout<<"\nString concatenation : "<<name<<name2<<"\n";
    cout<<"\nname[0] : "<<name[18]<<"\n";

    const int ArSize =20 ;
    char name3[ArSize];
    char dessert[ArSize];

    cout<<"\nEnter your name : ";
    cin>>name3;
    cout<<"\nEnter your favourite desert  : ";
    cin>>dessert;
    cout<<"\nname : "<<name3;
    cout<<"\nDessert : "<<dessert<<"\n";

    // getline () and get() function
    cout<<"\nEnter name : ";
    char name4[ArSize];
    cin.getline(name4, ArSize);
    cout<<"\nYour full name : "<<name4<<"\n";
    //using_getline();
    // using get() 
    //using_get();
    //using_get_with_newline();
    //cin_clear();
    
    //mixing string and numeric input 
    cout <<"What year was your house buit : ";
    int year ;
    cin>>year;
    cout<<"\nWhat is its stret adress : ";
    char address[80];
    cin.getline(address , 80);
    cout<<"\nYear : "<<year;
    cout<<"\nAddress : "<<address;
    cout<<"\n";
    // the problem here is that 
    // adter the cin>>year 
    // it leaves a ewline generated by the enter 
    // this enter( newline ) is remained in the input queue
    // then when getline() is called 
    // the getline takes the Enter key from the input queue
    // and stores it 
    // when displaying , it displays the newline

    //solution for the problem
    // use cin.get() 
    // or cin.get(ch)
    // or con>>year.get()
    cout <<"What year was your house buit : ";
    int year2;
    (cin>>year2).get();
    cout<<"\nWhat is its stret adress : ";
    char address2[80];
    cin.getline(address2 , 80);
    cout<<"\nYear : "<<year2;
    cout<<"\nAddress : "<<address2;
    cout<<"\n";
    //string_class();
    //string_class_2();
    //string_operations();
    //other_string();
    //structures();
    //unions();
    //enumerations();
    pointers();

    return 0;
}

void using_getline(){ 

    int ArSize = 20;
    char name[ArSize];
    cout<<"\nEnter name : ";
    cin.getline(name, ArSize);
    // if the impur string is longer than the array size 
    // then the getline( ) function, automatically 
    // stores the characters till the last index 
    // the characters after that are left in the input queue
    // this will give a failbit problem
    // so the next input will get blocked 

    cout<<"\nYour name is : "<<name<<"\n";
    cin.clear();
    //restores the input queue
    // solution for the failbit problem
    
}

void using_get(){ 
    int ArSize = 20 ;
    char name[ArSize];
    cout<<"\nEnter dessert : ";
    cin.get(name , ArSize).get(); // accepts newline 
    // just using cin.get() 
    // will craete a probem 
    // the 2nd word which you have enterd after the space 
    // will remain in the input queue
    // this meann that the next get() function 
    // when called will collect the data ( 2nd word )
    // from the input queue 
    // and you won't be able to enter the input 

    cout<<"\nDessert entered : "<<name<<"\n";
}

void using_get_with_newline(){ 
    int ArSize = 20 ;
    char name [ArSize];
    cout<<"\nEnter player name : ";
    cin.get(name , ArSize ).get();
    // if you enter the stirng , greater than the char array size 
    // then the get() stroes the characters until the last index 
    // the next characters are then left in the input queue
    // when the next input is called 
    // the next input variable stores the remaining characters of the input queue
    // this won't give rise to failbit 
    cout<<"\nplayer name : "<<name<<"\n";
    //clears the input queue 

}

void cin_clear(){ 
    int ArSize = 20 ;
    char name [ArSize];
    cout<<"\nEnter player2 name : ";
    cin.get(name , ArSize ).get();
    cout<<"\nplayer name : "<<name<<"\n";

}

void string_class(){
    // string class
    char charr1[20]; // creates an empty array 
    char charr2[20] ="jaguar"; // create an initialized array 
    string str1;    //create an empty string object 
    string str2="panther";    //create an initialized string 

    cout<<"\nEnter a kind of feline : ";
    cin>>charr1;
    cout<<"\nEnter another felines : ";
    cin>>str1;
    cout<<"\nHere are some felines : ";
    cout<<"\n"<<charr1<<" "<<charr2<<" "
        <<str1<<" "<<str2; // use count for output 
    
    cout<<"\nThe third letter in "<<charr2<<" is "
        <<charr2[2];
    cout<<"\nThe third letter in : "<<str2<<" is "
        <<str2[2]<<"\n";
}

void string_class_2(){

    string str1; // creates an empty object
    string str2="panther"; // ccreates an initialized string
    cout<<"\nEnter str1 : ";
    cin>>str1;

    //string initialization
    cout<<"\nCombined string : "<<str1+str2<<"\n";
    str1 = str1+str2;
    cout<<"\nAppended string : "<<str1<<"\n";

}

void string_operations(){
    char c1[20]; //empty character array 
    char c2[20] ="JAGUAR";
    string str1; //empty string object 
    string str2 = "PANTHER";

    //assignment for string objects and character arrays 
    str1 = str2 ; // copy str2 to str1 
    strcpy(c1 , c2); //copy c2 to c1

    //appending for string objects and character arrays 
    str1 = str1+str2 ;
    strcat(c1 ,c2);

    //finding the length of a string object and c-style string 
    int len1 = str1.size() ; //obtains length of str1
    int len2 = strlen(c1); //obtains length of c1 

    cout<<"\nThe string : "<<str1<<" contains "<<len1<<" characters ";
    cout<<"\nThe string "<<c1<<"\n contains "<<len2<<" characters ";
    
    char site[10] = "house";
    // strcat(site , "awesomeness"); //memory problem
    cout<<"\nsite : "<<site<<"\n";

    char c3[20];
    cout<<"\nLength of the char string before input : "<<strlen(c3)<<"\n";
    string str3;
    cout<<"\nLength of the string before input : "<<str3.size()<<"\n";
    cout<<"\nEnter char string : ";
    cin.getline(c3 , 20);
    cout<<"\nEnter string : ";
    getline(cin , str3);
    cout<<"\nYou entered : ";
    cout<<"\nChar : "<<c3<<"\nString : "<<str3;
    cout<<"\nchar length : "<<strlen(c3)<<"\nstring length : "<<str3.size()<<"\n";
}

void other_string(){
    wchar_t title[] = L"Chief astraunaut"; //w_char string 
    char16_t name[] = u"Felonia ripova"; // char16_t string 
    char32_t name2[] = U"Humber super sniper"; //char32_t string 
    // c++ uses the UTF 8 bit encoding prefix 
    // to indicate sring literals of that type 
    cout<<R"(Raw string here)"<<"\n";
    // this eleminates '(' and ')' 
}

void structures(){
    struct inflatable // structure definition
    { 
        char name[20];
        float volume;
        double price; 

    };
    inflatable hat; // hat variable of data type - inflatable struct 
    
    inflatable guest { 
        "awesomeness", //name vlaue 
        1.88, // volume value 
        29.99 // price value 
    }; //guest is a structure variable of type inflatable 

    inflatable pal{ 
        "overeating", //name value 
        12.99, // volume value 
        0.34 // price value 
    }; // pal is a second struct variable of struct inflatable 

    cout<<"\nExpand you  guest list with : "<<guest.name;
    cout<<" and "<<pal.name<<"\n";

    // pal.name is the name number of hte pal variable 
    cout<<"\nYou can have both for money ";
    cout<<guest.price + pal.price<<"\n";

    //can a structuer use a string class member 
    struct info { //struct definition
        string name;
        float volume ;
        double price ;
    };

    info bouquet { 
        "sunflowers",
        0.20,
        12.49
    };
    
    info choice ;
    cout<<"\nbouquet : "<<bouquet.name;
    cout<<"\nvolume : "<<bouquet.volume;
    cout<<"\nPrice : "<<bouquet.price;

    struct perks { 
        int key_number=10 ;
        int code=20;
    }key1 , key2; // structure variables 
    cout<<"\nkey1 key_number : "<<key1.key_number;
    cout<<"\nkey1 code : "<<key1.code<<"\n";

    //structure with no tag name 
    struct { 
        int x =1;
        int y =2;
    }position; // a structure variable 
    cout<<"\nposition x : "<<position.x;
    cout<<"\nposition y : "<<position.y<<"\n";

    // arrays of structures 
    perks person[2]{ 
        30,100,
        900,40
    };
    cout<<"\nperson0.key_number : "<<person[0].key_number;
    cout<<"\nperson1.code : "<<person[0].code;
    cout<<"\nperson2.ley_number : "<<person[1].code;
    cout<<"\nperson2.code : "<<person[1].code<<"\n";

    // bits field in structures 
    struct toggle{ 
        unsigned int SN =4; // 4 bits for SN value 
        unsigned int : 4; // 4 bits unused 
        bool goodIn = 1; // valid input ( 1 bit )
        bool goodTrogle = 1 ; // successful toggling 
    };

    toggle rim{ 14,true ,false};
    if (rim.goodIn){
        cout<<"\nTrue statement\n";
    }
}

void unions(){ 
    // union can ohl difference data types 
    // one type at a a time 
    union one { 
        int int_val;
        long long_val;
        double double_val;
    };
    one pail;
    pail.int_val = 1;
    cout<<"\nint_value : "<<pail.int_val;
    pail.long_val = 2;
    cout<<"\nlong value : "<<pail.long_val<<"\n";

    //anonymous union
    struct widget{ 
        char brand[20];
        int type;
        union { //anonymous union
            long id_num;
            char id_char[12];
        };      
    };

    widget price ;
    if(price.type==1){ 
        cout<<"\nEnter price.id_num : ";
        cin>>price.id_num;
    }
    else { 
        cout<<"\nEnter price.id_char : ";
        cin>>price.id_char;
    }

}

void enumerations(){
    enum spectrum {v,i,b,g,y,o,r};
    spectrum band; //badn , a variable of type spectrum
    band = b ; // valid, b is an enumerator
    //band = 2000; //invalid , 2000 not an enumerator 

    band = o; //valid 
    //++band; // not valid ++ discused in chapter 5 
    //band = o + r;  // not valid ,a little tricky 
    int color = b; // valid, epctrum type promoted to int 
    //band = 3; // invalid, int not converted to spectrum 
    color = 3 + r; // valid, red converted to int 
    //band = o + r ; // not valid, but a little tricky 

    // type casting 
    band = spectrum(3); // typecast 3 to type spectrum
    //band = spectrum(1200); //typecast 1200 unefined 

    //setting enumerator values 
    //enum bits{one = 1 , two =2,four =4,eight=8};
    enum bigstep{first, second=2, third};
    //enum { zero, null=0 ,one , num_uno=1};
    //bits person;
    //person = bits(6); //valid , because 6 is int bits range 
}

void pointers() { 
    int donuts = 6 ;
    double cups =4.5;
    cout<<"\nDonuts value : "<<donuts;
    cout<<"\nDonuts address : "<<(&donuts)<<"\n";
    cout<<"\nCups value : "<<cups ;
    cout<<"\ncups address : "<<(&cups)<<"\n";
    cout<<"\nSize of doube : "<<sizeof(double)<<"\n";
    int donuts2=2;
    cout<<"\nAddress of donuts 2 : "<<(&donuts2)<<"\n";

    //pointers 
    int updates=6;
    int *p_updates; // declare pointer to an int 
    p_updates = &updates ; //assign address of int to a pointer 
    
    //express values two ways 
    cout<<"\nValue :updates :  "<<updates;
    cout<<"\np_updates : "<<*p_updates<<"\n";

    //express address two ways
    cout<<"\nAdresses : &updates : "<<&updates;
    cout<<"\np_updates : "<<p_updates<<"\n";

    //use pointer to change value 
    *p_updates = *p_updates + 1;
    cout<<"\nNow updates : "<<updates<<"\n";

    //assignment , other way 
    int *p1 , p2;
    //here p1 - is a pointer 
    // p2 - is an integer and not a pointer 
    int higgens = 5 ;
    int *ptr = &higgens;
    cout<<"\nValue of higgens : "<<higgens;
    cout<<"\nValue pf higgens poitner : "<<ptr<<"\n";

    //int *fellow;
    //*fellow = 123; //invalid 
    // the pointer does not know where to point to 

    //pointers and numbers 
    int *pt;
    pt = (int*) 0xB8000000; //types now match 
    //this means that the 
    //pointer now points to the memory address 
    //0xB8000000
    cout<<"\npt : "<<pt;
    //cout<<"\nValue of pt : "<<*pt<<"\n"; // will give an 
    // error

    //allocating memory with 'new'
    int *pn = new int;
    // this means that the, compiler now 
    // finds a space in the memory 
    // to store an integer, so it 
    // finds a free space of 4 bytes 
    // and the pointer pn, points to that memory address 

    int nights = 1001;
    int *night = new int; // allocates space ofr an int 
    *night = 1001; // stores the vlaue 1001 

    cout<<"\nnights value : "<<nights;
    cout<<"\nnight pointer value : "<<*night;
    cout<<"\nnight pointer address, it holds  : "<<night;
    cout<<"\nAddress of pointer night : "<<&night;
    cout<<"\nSize of pointer night : "<<sizeof(night);
    cout<<"\nSize of int : "<<sizeof(int);
    cout<<"\nSize of night value : "<<sizeof(*night)<<"\n";

    delete night;
    /*
    //freeing memory with delete 
    int *ps = new int ; //allocates memory with new 
    delete ps ; // free memory with delete when done 
    */
    int *pm = new int ; 
    delete pm;
    int judge =5 ;
    int *j = new int;
    delete j;

    int *pi= new int ; //allocates memory 
    delete pi;
    //int *pq = pi; // set second pointer to same block 
    //delete pi;
    //delete pq; // delete with second pointer
    //cout<<"\nAddress of pi : "<<&pi<<"\n";    //gives error

    //creating a dynaic array with new 
    int *psome = new int[10]; // get a block of 10 ints 
    delete [] psome; // frees the dynamic memory

    double *p3 = new double[3]; //space for 3 doubles 
    p3[0] = 0.2 ; // treat p3 like an array name 
    p3[1] = 0.3; 
    p3[2] = 0.4; 
    cout<<"\np[0] : "<<p3[0]<<"\np3[1] : "<<p3[1]<<"\np3[2] : "<<p3[2]<<"\n";
    p3 = p3+1 ; // givs the address of the next element 
    cout<<"\np3 value : "<<*p3;
    cout<<"\np3 address : "<<p3;
    p3= p3+1;
    cout<<"\np3 value : "<<*p3;
    cout<<"\np3 address : "<<p3;
    *p3 = *p3+1;
    cout<<"\np3 value : "<<*p3;
    p3= p3-2;
    // remember, after you are done incrementing the address 
    // of the address of the element the pointer holds 
    // before deleating the entire pointer array 
    // make sure, that the pointer, points to 
    // the first element, ie- pointer[0]
    //So, do this by decrementing, the same steps 
    // you applied while incrementing the pointer address 
    cout<<"\n";
    delete []p3;

    //pointers , array and pointer arithmatic
    double wages[3] = {1000.0 , 2000.0 ,3000.0};
    short stacks[3] = {3,2,1};

    //here are 2 ways to get the address of an array 
    double *wage = wages ; // name of an array = address 
    short *stack = &stacks[0]; //or use the address operator 

    // with array element 
    cout<<"\nwage pointer value  : "<<*wage;
    wage = wage +1 ;
    cout<<"\nWage pointer value : "<<*wage;
    wage =wage +1 ;
    cout<<"\nWage pointer value : "<<*wage<<"\n";

    // address operator pointer 
    cout<<"\nstack pointer value : "<<*stack;
    stack = stack +1 ;
    cout<<"\nstack pointer value : "<<*stack;
    stack = stack +1 ;
    cout<<"\nstack pointer value : "<<*stack<<"\n";

    int plane = 3 ;
    int *planes = &plane;
    cout<<"\nplanes value : "<<*planes;
    cout<<"\nplanes address : "<<planes<<"\n";
    //hence array operator 
    // ie - array name = address 
    // works only for arrays and not for non-array elements 
    

    








}