/**
 * Зроблено:
 * ПІБ: Світличний Дмитро Євгенович
 * Група студента: 123
 * Lab 2.2
 */
// 9 варіант
#include <iostream>
using std::cout,
    std::cin, std::string;
enum Names
{
    David,
    Tom,
    Andrew,
    Kate,
    Mary,
    Olga
};
struct Student
{
    Names name;
    int year;
    int month;
};
struct Student2
{
    string nationality;
    int course;
    float average_grade;
};
void Task_1()
{
    Student myStudents[7];
    myStudents[0] = {Tom, 2006, 1};

    myStudents[1] = {David, 2007, 12};

    myStudents[2] = {Kate, 2006, 6};

    myStudents[3] = {Andrew, 2006, 9};

    myStudents[4] = {Olga, 1999, 2};

    myStudents[5] = {Mary, 2005, 1};
    myStudents[6].name = Andrew;

    myStudents[6].year = 2007;

    myStudents[6].month = 7;
    float count = 0;
    for (int i = 0; i < 7; i++)
    {
        if (myStudents[i].month == 12 || myStudents[i].month < 3)
        {
            count++;
        }
    }
    float result = (count * 100) / 7;
    cout << result << "%\n";
}
void Task_2()
{
    Student2 myStudents2[7];
    myStudents2[0] = {"Ukrainian", 3, 4.4};
    myStudents2[1] = {"Ukrainian", 1, 5};
    myStudents2[2] = {"Nigerian", 4, 3};
    myStudents2[3] = {"Ukrainian", 3, 3.8};
    myStudents2[4] = {"Croatian", 2, 5};
    myStudents2[5] = {"Ukrainian", 2, 5};
    myStudents2[6] = {"Ukrainian", 1, 4.7};
    float count2 = 0;
    for (int i = 0; i < 7; i++)
    {
        if (myStudents2[i].nationality == "Ukrainian" && myStudents2[i].average_grade > 4.5)
        {
            count2++;
        }
    }
    float result2 = (count2 * 100) / 7;
    cout << result2 << "%\n";
}
int main()
{
    Task_1();
    Task_2();
}