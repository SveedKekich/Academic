/**
 * Done by:
 * Student Name: Svitlichnyi Dmitro
 * Student Group: 123
 * RGR
 * variant 21
 */
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using std::cout, std::cin, std::vector, std::string;
bool IsValid(const string &input)
{
    vector<char> sequence;
    bool exclamation = false;
    std::copy(input.begin(), input.end(), std::back_inserter(sequence));
    if (sequence[0] != '0' || sequence[sequence.size() - 1] != '1')
    {
        return false;
    }
    else
    {
        for (int i = 1; i < sequence.size() - 1; i++)
        {
            if (sequence[i] == '!')
            {
                exclamation = true;
            }
            else
            {
                bool IsReal = false;
                for (int k = 0; k < 10; k++)
                {
                    char num = '0' + k;
                    if (sequence[i] == num)
                    {
                        IsReal = true;
                        break;
                    }
                }
                if (IsReal == false)
                {
                    return false;
                }
            }
        }
        if (exclamation == true)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
int main()
{
    string input;
    cin >> input;
    if (IsValid(input) == true)
    {
        cout << "true" << '\n';
    }
    else
    {
        cout << "false" << '\n';
    }
}