class Program
{
    static void Main()
    {
        int[,] data = {
            { 1, 2, 3 },
            { 4, 5, 6 },
            { 7, 8, 9 }
        };

        IntMatrix matrix = new IntMatrix(data);

        Console.WriteLine("Добутки по стовпцях:");
        for (int i = 0; i < 3; i++)
        {
            Console.WriteLine($"Стовпець {i}: {matrix[i]}");
        }

        Console.WriteLine($"\nСереднє значення елементів матриці: {matrix.Average:F2}");
    }
}
