/**
 * Зроблено:
 * ПІБ: Світличний Дмитро Євгенович
 * Група студента: 123
 * Lab 1.6
 */
#include <iostream>
int main(){
    //Завдання 1
    //Ініціювання змінних літералом
    const char CONST1 = '1';
    char Var1 = 'p';
    char Var2;
    Var2 = '№';
    //Ініціювання змінних кодом символа
    const char CONST2 = 0x7a; //"z"
    char Var3 = 0x3b; //";"
    char Var4;
    Var4 = 0x9; //"\t"
    //Завдання 2
    //Ініціювання змінних типів int, float, unsigned short
    int A = 3841;
    float B = 954.67;
    unsigned short C = 6429;
    //Опис змінних double, int, char
    double D;
    int E;
    char F;
    //За допомогою неявного приведення типів:
    D=A;
    E=B;
    F=C;
    //За допомогою явного приведення типів:
    D=(double)A;
    E=(int)B;
    F=(char)C;
    //За допомогою суворої типізації
    double * pD;
    void *pV;
    pV = &A;
    pD = (double*)pV;
    D=*pD;

    int * pE;
    pV = &B;
    pE = (int*)pV;
    E=*pE;
    
    char * pF;
    pV = &C;
    pF = (char*)pV;
    F=*pF;
}