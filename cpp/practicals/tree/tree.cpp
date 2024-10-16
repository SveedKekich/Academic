/**
 * Done by:
 * Student Name: Svitlichnyi Dmitro
 * Student Group: 123
 * Christmas Tree
 */
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <string>
#include <ctime>
#include <thread>   
#include <chrono>  

void ResetColor()
{
    std::cout << "\033[0m";
}
void SetGreenColor()
{
    std::cout << "\033[32m";
}
void SetYellowColor()
{
    std::cout << "\033[33m";
}
void SetRandomColor()
{
    int color = 30 + (rand() % 7 + 1);
    std::cout << "\033[" << color << "m";
}

void DrawTree(const std::vector<std::vector<std::vector<char>>>& tree, std::ofstream& file, const int TotalWidth)
{
    std::cout << "\033[2J\033[H";

    for (auto a : tree)
    {
        int width = 10;
        for (auto b : a)
        {
            int padding = (TotalWidth - b.size()) / 2;
            std::cout << std::string(padding, ' ');
            file << std::string(padding, ' ');
            for (auto c : b)
            {
                if (c != '*')
                {
                    SetRandomColor(); 
                }
                else
                {
                    SetGreenColor();  
                }
                std::cout << c;
                file << c;
            }
            std::cout << '\n';
            file << '\n';
            width--;
        }
    }

    SetYellowColor();
    for (int i = 0; i < 3; i++)
    {
        int padding = (TotalWidth - 1) / 2;
        std::cout << std::setw(padding) << '*' << '\n';
        file << std::setw(padding) << '*' << '\n';
    }
    ResetColor();
}

int main()
{
    srand(time(NULL));
    std::ofstream file("./christmas_tree.txt");
    int n, m = 5;
    char star = '*';
    char toys[] = {'@', '$', '&', '#'};
    const int TotalWidth = 50;

    std::cin >> n;
    std::vector<std::vector<std::vector<char>>> tree;
    
    for (int i = 0; i < n; i++)
    {
        int width = 10;
        std::vector<std::vector<char>> base;
        for (int j = 1; j <= m; j += 2)
        {
            std::vector<char> row;
            for (int k = 0; k < j; k++)
            {
                if (rand() % 4 == 0)
                {
                    row.push_back(toys[rand() % 4]);  
                }
                else
                {
                    row.push_back(star);
                }
            }
            width--;
            base.push_back(row);
        }
        m += 2;
        tree.push_back(base);
    }
    while (true)
    {
        DrawTree(tree, file, TotalWidth);
        std::this_thread::sleep_for(std::chrono::seconds(1));  
    }
file.close();
    return 0;
}
