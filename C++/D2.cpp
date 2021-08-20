#include<iostream>
#include<cmath>
#include<climits>

#define ZERO 0

using namespace std;
void simon(int);
int stonetolb(int);
int age_to_months(int);

int main(){ 
    int a;
    cout<<"This is atharva\n";
    cin>>a;
    cout<<"\nThe number you entered is : "<<a<<"\n";
    int carrots = 25;
    cout<<"\nI have "<<carrots<<" carrots \n";
    int banana;
    banana = carrots = 25;
    cout<<"\nBanana's left : "<<banana<<"\n";
    cout<<"\nBanana's left ( in strings ) : %s"<<"25"<<"\n";
    cout<<"\nbanana's left ( in int ) : %d"<<25<<"\n";
    cout<<"\nEnter area : ";
    float area;
    cin>>area;
    double side;
    side = sqrt(area);
    cout<<"Side length : "<<side<<"\n";
    double result = pow(2,3);
    cout<<"power (2,3) : "<<result<<"\n";
    cout<<"\nRandom integer : "<<rand()<<"\n";
    simon(12);
    cout<<"stone to lb : "<<stonetolb(14)<<"\n";
    int aunts = stonetolb(10);
    cout<<"10 stones to lb : "<<aunts<<"\n";
    float furlongs;
    cout<<"\nEnter value in furlongs : ";
    cin>>furlongs;
    cout<<"\nConverted value : "<<furlongs*220<<" yards \n";
    cout<<"age 14 in months : "<<age_to_months(14)<<"\n";
    cout<<"\nSize of int : "<<sizeof(int);
    cout<<"\nSize of long : "<<sizeof(long);
    cout<<"\nSize of long long : "<<sizeof(long long );
    cout<<"\nSize of short : "<<sizeof(short)<<"\n";
    int n_int = INT_MAX; // initializes _int to MAX_INT value 
    short n_short = SHRT_MAX;
    long n_long = LONG_MAX;
    long long n_llong = LLONG_MAX ;

    //sizeof operator yields the size of data type 
    // in bytes 
    cout<<"\nSize of INT_MAX : "<<sizeof(n_int)<<" bytes";
    cout<<"\nSize of SHORT_MAX : "<<sizeof(n_short)<<" bytes ";
    cout<<"\nSize of LONG_MAX : "<<sizeof(n_long)<<" bytes ";
    cout<<"\nSize of LONG LONG _MAX : "<<sizeof(n_llong)<<" bytes\n";

    //printing the maximum values 
    cout<<"\nMax value of int : "<<n_int;
    cout<<"\nMax size of short : "<<n_short;
    cout<<"\nMax value of long : "<<n_long;
    cout<<"\nMax value of long long : "<<n_llong<<"\n";

    cout<<"\nMinimum int value : "<<INT_MIN;
    cout<<"\nBits per byte : "<<CHAR_BIT;
    cout<<"\nMaximum sizeof a char : "<<sizeof(char);
    cout<<"\nMaximum unsigned long long value : "<<ULLONG_MAX;
    short plane ;
    cout<<"\nValue of plane : "<<plane;
    unsigned short nn_short = SHRT_MAX;
    cout<<"\nMaximum value of unsigned short : "<<nn_short;
    cout<<"\nAdding 1 to nn_short : "<<nn_short +1;
    cout<<"\nAdding -1 to nn_short : "<<nn_short-1;
    short sam = SHRT_MAX ;
    unsigned short sue = sam ;
    cout<<"\nadding 1 to sue : "<<sue+1;
    cout<<"\nAdding -1 to sue : "<<sue-1;

    int  chest =42;
    int  waist = 0x42; //hexadecimal iteger literal
    int insem = 042; //octal integer literal
    
    cout<<"\nchest : "<<chest <<"(42 i decimal )";
    cout<<"\nWaist : "<<waist<<" (42 in hexadecimal ) ";
    cout<<"\ninsem : "<<insem<<" (42 in octal ) ";
    int bin = 012 ;
    cout<<"\nbinary : "<<bin<<"\n";

    //desplaying integers in decimal , hexadecimal , octal literals 
    int b = 42;

    cout<<"\nChest : "<<b<<" in deciaml";
    cout<<hex;
    cout<<"\nWaist : "<<b <<" in hexadecimal ";
    cout<<oct;
    cout<<"\ninsem : "<<b<<" in octal\n ";
    cout<<dec;
    cout<<"\nInteger 120 : "<<120<<"\n";
    cout<<"\nSending long integer : "<<120L;
    cout<<"\nSending unsigned long integer : "<<120UL;
    cout<<"\nSending short integer : "<<120U;
    cout<<"\nSize of long : "<<sizeof(120L);
    cout<<"\nSize of unsigned long : "<<sizeof(120UL);
    cout<<"\nSize of long : "<<sizeof(long);
    cout<<"\nSize of int : "<<sizeof(int);

    // ASCII values 
    char ch ;
    cout<<"\nEnter a character : ";
    cin>>ch;
    cout<<"\nCharacter entered : "<<ch;
    cout<<"\ninteger character : "<<int(ch)<<"\n";

    //using put() 
    char c = 'M';
    int i = c;
    c = c+1;
    i = c;
    cout<<"\nASCII character for 'A' : "<<int('A');
    cout<<"\nUpdated character : "<<c;
    cout<<"\nASCII value of the character : "<<i<<"\n";
    cout<<"\nPrinting using putch() : ";
    cout.put(c);
    char alarm = '\a';
    //cout<<"\ncharacter alarm : "<<alarm<<"\n";
    cout<<"\ncharcter alarm : \a"<<"\n";
    cout<<"\n Octal number : "<<"\012"<<"\n";

    //using backspace character 
    cout<<"\nenter your code : ______\b\b\b\b\b\b";
    long code;
    cin>>code;
    cout<<"\nYou entered the code : "<<code;
    cout<<"\nbits in character set : "<<CHAR_BIT<<"\n";

    //wchar_t
    wchar_t bob = L'P';
    wcout<<L"tall";
    cout<<"\nSize of bob  :"<<sizeof(bob)<<"\n";

    // char16_t and char32_t 
    char16_t ch1 = u'q';  //basic character in 16bit form 
    char32_t ch2 = U'\U0000222B'; // universal character name in 32-bit form
    cout<<"\nch1 : "<<ch1;
    cout<<"\nch2 : "<<ch2<<"\n";

    //bool values 
    bool is_ready = true ;
    cout<<"\nis-ready : "<<is_ready;
    int ass = true ;
    int ass2 = false ;
    cout<<"\nass : "<<ass <<"ass2 : "<<" "<<ass2<<"\n";

    //const qualifier 
    float mass = 9.11e-31;
    cout<<"\nMass of electron : "<<mass<<"\n";

    cout<<"\nSize of float : "<<sizeof(float)<<" bytes ";
    cout<<"\nSize of double  : "<<sizeof(double)<<" bytes ";
    cout<<"\nSize of long double : "<<sizeof(long double)<<" bytes "<<"\n";

    float tub= 10.0/3.0;
    double mint = 10.0 / 3.0;
    const float million = 1.0e6;

    cout<<"\nTub : "<<tub;
    cout<<"\nmint : "<<mint;
    cout<<"\nMillion : "<<million;
    cout<<"\nten million tubs : "<<million * tub * 10<<"\n";

    cout<<"\nfloat constant : "<<1.32f;
    cout<<"\nloong double constant : "<<2.2L<<"\n";
    cout<<"\nSize of loing double constant : "<<sizeof(2.2L);
    cout<<"\nSize of float constant : "<<sizeof(1.32f)<<"\n";

    // problems with float 
    float a_float = 2.34e+22f;
    float b_float = a_float + 0.1f;

    cout<<"\na : "<<a_float;
    cout<<"\nb : "<<b_float;
    cout<<"\nSubtraction of both : "<<a_float-b_float<<"\n";

    //modulous operator works only for int data type 
    // example 
    float bat = 2;
    float hat = 3;
    //cout<<"\nModulous of bat and hat : "<<bat%hat<<"\n";
    // gives error
    cout<<"\nDivision of bat and hat : "<<bat/hat;
    cout<<"\nInteger output of division of bat and hat : "<<int(bat/hat)<<"\n";

    return 0;

}

void simon(int n){ 
    cout<<"Inside simon function : "<<n<<"\n";
}

int stonetolb(int stone ){
    return 14*stone;
}

int age_to_months(int n){
    return n*12;
}