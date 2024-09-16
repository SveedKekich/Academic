/**
 * Зроблено:
 * ПІБ: Світличний Дмитро Євгенович
 * Група студента: 123
 * Lab 1.3
 */
#include <iostream>
#include <stdio.h>
int main(){
   unsigned int x1 = 89, y1 = 122, result1 = 0; //Створення змінних 1 та 2 операнди та результату
   result1 = x1 & y1; //Виконання операції "Порозрядне І"
   std::cout<<result1<<'\n'; //Вивід результату
   unsigned int x2 = 134, y2 = 65, result2 = 0;
   result2 = x2 | y2; //Виконання операції "Порозрядне АБО"
   std::cout<<result2<<'\n'; 
   unsigned int x3 = 43, y3 = 87, result3 = 0;
   result3 = x3 ^ y3; //Виконання операції "Порозрядне АБО яке виключає"
   std::cout<<result3<<'\n'; 
   unsigned int x4 = 916, y4 = 10, result4 = 0;
   result4 = x4 << y4; //Виконання операції "Зсув ліворуч"
   std::cout<<result4<<'\n'; 
   unsigned int x5 = 86, y5 = 10, result5 = 0;
   result5 = x5 >> y5; //Виконання операції "Зсув праворуч"
   std::cout<<result5<<'\n'; 
   int x6=27, result6=0;
   result6 = ~(x6); //Виконання операції "Порозрядне заперечення"
   std::cout<<result6<<'\n'; 
}