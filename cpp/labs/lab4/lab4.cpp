/**
 * Зроблено:
 * ПІБ: Світличний Дмитро Євгенович
 * Група студента: 123
 * Lab 1.4
 */
//9 варіант
#include <iostream>
#include <math.h>
int main(){
    unsigned short sA;
    unsigned short *psB;
    psB = &sA;
    *psB = 612;
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
    void *pV;
    int sizesA = sizeof(sA);
    int sizepsA = sizeof(psB);
    int sizeiA = sizeof(iA);
    int sizepiB = sizeof(piB);
    int sizefA = sizeof(fA);
    int sizepfB = sizeof(pfB);
    int sizedA = sizeof(dA);
    int sizepdB = sizeof(pdB);
    pV = &psB;
}