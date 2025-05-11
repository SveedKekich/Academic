using System;

public class IntMatrix
{
    private int[,] matrix;
    private double average; // закритий елемент-даний

    public IntMatrix(int[,] inputMatrix)
    {
        matrix = inputMatrix;
        CalculateAverage();
    }

    // Властивість для читання average
    public double Average => average;

    // Індексатор по стовпцю
    public int this[int columnIndex]
    {
        get
        {
            if (columnIndex < 0 || columnIndex >= matrix.GetLength(1))
                throw new IndexOutOfRangeException("Невірний індекс стовпця.");

            int product = 1;
            for (int i = 0; i < matrix.GetLength(0); i++)
                product *= matrix[i, columnIndex];

            return product;
        }
    }

    // Приватний метод для обчислення середнього значення
    private void CalculateAverage()
    {
        int sum = 0;
        int count = 0;

        foreach (int value in matrix)
        {
            sum += value;
            count++;
        }

        average = (double)sum / count;
    }
}
