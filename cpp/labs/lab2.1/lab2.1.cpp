/**
 * Зроблено:
 * ПІБ: Світличний Дмитро Євгенович
 * Група студента: 123
 * Lab 2.1
 */
#include <iostream>
// 9 Варіант
int main()
{
    // Task 1
    int arr[11]; // Створюємо масив розміром 11
    for (int i = 0; i < 11; i++)
    {
        if (i % 2 == 0)
        {
            arr[i] = i - 7;
        }
        else
        {
            arr[i] = 7 + i;
        }
    }
    int size = 11;
    for (int i = 0; i < size - 1; i++)
    {
        for (int j = 0; j < size - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    // Task 2
    int arr1[10];
    int arr2[10];
    int arr3[10];
    for (int i = 0; i < 10; i++)
    {
        arr1[i] = i * i + 76;
    }
    for (int i = 0; i < 10; i++)
    {
        arr2[i] = 85 - i;
    }
    int k = 0;
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if (arr1[i] == arr2[j])
            {
                arr3[k] = arr1[i];
                k++;
                break;
            }
        }
    }
    int result = 0;
    for (int i = 0; i < k; i++)
    {
        result += arr3[i];
    }
    // Task 3
    int matrix1[5][4] = {{11, 21, -3, 4},

                         {5, -6, 0, 8},

                         {9, 0, 11, 2},

                         {4, -4, 4, 1},

                         {0, 1, -9, 6}};
    float matrix2[5][5] = {{1.1, -2.0, -8.34, 5.5, 1.2},

                           {-0.2, 1.34, 2.2, -3.5, 1.1},

                           {-2.9, -3.1, 4.4, 7.2, -8.1},

                           {-2.6, -1.2, 3.4, 5.4, 6.6},

                           {0, 1, -9, 6, 8.4}};
    int res1[4];
    for (int i = 0; i < 4; i++)
    {
        int sum = 0;
        for (int j = 0; j < 5; j++)
        {
            sum += matrix1[j][i];
        }
        res1[i] = sum;
    }
    float res2[2];
    int f = 0;
    for (int i = 0; i < 5; i++)
    {
        int j = 4;
        if (matrix2[i][j] < 0)
        {
            res2[f] = matrix2[i][j];
            f++;
        }
        j--;
    }
}