/**
 * Done by:
 * Student Name: Svitlichnyi Dmitro
 * Student Group: 123
 * Practical 1.3
 */
#include <iostream>
using std::cin, std::cout;
void Task1()
{
    float A, B;
    cin >> A >> B;
    float res = A * B;
    if (res < 0)
    {
        res *= 2;
        cout << res << '\n';
    }
    else
    {
        res *= 1.5;
        cout << res << '\n';
    }
}
bool Task2()
{
    int A, B, C;
    cin >> A >> B >> C;
    if (A < B + C || B < A + C || C < A + B)
    {
        return true;
    }
    else
    {
        return false;
    }
}
int main()
{
    Task1();
    cout << Task2() << '\n';
}