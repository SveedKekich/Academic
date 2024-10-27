/**
 * Done by:
 * Student Name: Svitlichnyi Dmitro
 * Student Group: 123
 * Practical 1.4
 */
#include <iostream>
#include <math.h>
using std::cin, std::cout;
void Task1()
{
    int n, res;
    cin >> n;
    int Fib1 = 1;
    int Fib2 = 1;
    if (n == 1 || n == 2)
    {
        res = 1;
        cout << res;
    }
    else
    {
        int i = 3;
        for (;;)
        {
            res = Fib1 + Fib2;
            if (i == n)
            {
                cout << res << '\n';
                break;
            }
            else
            {
                Fib1 = Fib2;
                Fib2 = res;
                i++;
            }
        }
    }
}
void Task2()
{
    float n, res = 0, count = 0;
    cin >> n;
    for (int i = n; i > 0; i--)
    {
        if ((i % 2) != 0)
        {
            res += i;
            count++;
        }
    }
    cout << res / count << '\n';
}
void Task3()
{
    float b1, q, n;
    cin >> b1 >> q >> n;
    float sum = b1 * ((1 - pow(q, n)) / (1 - q));
    cout << sum / n << '\n';
}
int main()
{
    Task1();
    Task2();
    Task3();
}