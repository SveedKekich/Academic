/**
 * Done by:
 * Student Name: Svitlichnyi Dmitro
 * Student Group: 123
 * Practical 1.1
 */
#include <iostream>
using std::cin, std::cout;
int factorial(int num){
    if(num==0 || num==1){
    return 1;
    }
    else{
        int res=1;
        for(int i=num;i>0;i--){
            res*=i;
        }
        return res;
    }
}
void Task1(){
float A,B;
cin>>A>>B;
cout<<(A+B)/2<<'\n';
}
void Task2(){
int A,B,C;
cin>>A>>B;
C=A;
A=B;
B=C;
cout<<A<<'\n'<<B<<'\n';
}
void Task3(){
    float A,B;
    cout<<A-B<<'\n';
    cout<<A/B<<'\n';  
}
void Task4(){
    int A;
    cin>>A;
    cout<<!A<<'\n';
}
void Task5(){
    int A,B,C;
    cin>>A>>B>>C;
    cout<<C*(A+B)<<'\n';
}
void Task6(){
    int a1, d, n=1,sum=0;
    cin>>a1>>d;
    for(int i=0;i<5;i++){
        int an=a1+d*(n-1);
        cout<<an<<" ";
        n++;
        sum+=an;
    }
    cout<<'\n'<<sum;
}
void Task7(){
    float res = 0;
    for(int i=1;i<=5;i++){
        res+=factorial(i);
    }
    cout<<res/5;
}
int main(){
Task1();
Task2();
Task3();
Task4();
Task5();
Task6();
Task7();
}