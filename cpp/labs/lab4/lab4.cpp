/**
 * Зроблено:
 * ПІБ: Світличний Дмитро Євгенович
 * Група студента: 123
 * Lab 1.4
 */
#include <iostream>
#include <math.h>
int main(){
    unsigned short sA; //Cтворення змінної
    unsigned short *psB; //Створення вказівника
    psB = &sA; //Ініціювання вказівних змінних адресами змінних
    *psB = 612; //Присвоєння значення змінній
    int iA;
    int *piB;
    piB = &iA;
    *piB = -805;
    float fA;
    float *pfB;
    pfB = &fA;
    *pfB = 14.4328;
    double dA;
    double *pdB;
    pdB = &dA;
    *pdB = -30.22e100;
    void *pV; //Створення нетипізованої вказівної зміни
    int sizesA = sizeof(sA); //Створення змінної яка дорівнює розміру змінної
    int sizepsA = sizeof(psB); //Створення змінної яка дорівнює розміру вказівної змінної
    int sizeiA = sizeof(iA);
    int sizepiB = sizeof(piB);
    int sizefA = sizeof(fA);
    int sizepfB = sizeof(pfB);
    int sizedA = sizeof(dA);
    int sizepdB = sizeof(pdB);
    pV = &psB; //Ініціювання нетипізованої вказівної змінної адресом типізованої вказівної змінної
}