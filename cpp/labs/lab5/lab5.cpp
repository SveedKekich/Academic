/**
 * Зроблено:
 * ПІБ: Світличний Дмитро Євгенович
 * Група студента: 123
 * Lab 1.5
 */
#include <iostream>
int main(){
    //Завдання 1
    float a1=5.8,b1=39.1,c1=70,d1=42; //Опис та ініціалізація змінних 1 виразу
    bool ARez = (!(a1=b1)^(-(c1<d1))); //Побудування 1 виразу
    float a2=85,b2=85,c2=6.4,d2=9.3; //Опис та ініціалізація змінних 2 виразу
    bool BRez = (!(a2=b2)^(-(c2<d2))); //Побудування 2 виразу
    std::cout<<ARez<<'\n'<<BRez<<'\n';  //Вивід результатів 1 і 2 виразів
    //Завдання 2
    const long constA=49; //Ініціалізація константи
    long B=-65, E=2; //Ініціалізація змінних B,E
    long C; //Створення змінної C
    long *pC; //Опис вказівної змінної 
    pC=&C; //Ініціалізація вказівної змінної адресою змінної С
    *pC=23; //Операція розіменування
    bool CRez = ((constA^(-B))-*pC)>=(13+(E<<sizeof(long))); //Побудування виразу
    std::cout<<CRez; //Вивід результату виразу
}