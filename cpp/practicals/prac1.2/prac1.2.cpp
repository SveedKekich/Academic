/**
 * Done by:
 * Student Name: Svitlichnyi Dmitro
 * Student Group: 123
 * Practical 1.2
 */
#include <iostream>
using std::cin, std::cout;
void Task1()
{
    int A;
    cin >> A;
    if ((A % 2) == 0)
    {
        A++;
        cout << A << '\n';
    }
    else
    {
        A--;
        cout << A << '\n';
    }
}
void Task2()
{
    int A, B;
    cin >> A >> B;
    if (A > 0 && B > 0)
    {
        cout << A * B << '\n';
    }
    else
    {
        cout << A + B << '\n';
    }
}
void Task3()
{
    int A, B;
    cin >> A >> B;
    if (A == B)
    {
        cout << "There is no max value" << '\n';
    }
    else if (A > B)
    {
        cout << A << '\n';
    }
    else
    {
        cout << B << '\n';
    }
}
void Task4()
{
    float A;
    cin >> A;
    if (A > 0)
    {
        A += 1;
        cout << A << '\n';
    }
    else if (A < 0)
    {
        A -= 2;
        cout << A << '\n';
    }
    else
    {
        A = 10;
        cout << A << '\n';
    }
}
int main()
{
    Task1();
    Task2();
    Task3();
    Task4();
}