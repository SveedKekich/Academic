using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var expressions = new List<Expression>
        {
            new Expression(2, 3, 5, 1),
            new Expression(1, 1, 4, 2),
            new Expression(1, 2, 8, 0.5) 
        };

        for (int i = 0; i < expressions.Count; i++)
        {
            try
            {
                double result = expressions[i].Calculate();
                Console.WriteLine($"Expression {i + 1} result: {result}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error in expression {i + 1}: {ex.Message}");
            }
        }
    }
}
