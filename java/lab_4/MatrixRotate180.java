package lab_4;
import java.io.*;
import java.util.Scanner;

public class MatrixRotate180 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Введіть шлях до вхідного файлу: ");
            String inputFile = scanner.nextLine();

            System.out.print("Введіть шлях до вихідного файлу: ");
            String outputFile = scanner.nextLine();

            File file = new File(inputFile);
            Scanner fileScanner = new Scanner(file);

            int n = fileScanner.nextInt();
            int[][] matrix = new int[n][n];

            System.out.println("Зчитування матриці з файлу...");

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    matrix[i][j] = fileScanner.nextInt();
                }
            }

            fileScanner.close();

            System.out.println("Початкова матриця:");
            printMatrix(matrix);

            int[][] rotated = new int[n][n];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    rotated[i][j] = matrix[n - 1 - i][n - 1 - j];
                }
            }

            System.out.println("Матриця після повороту на 180°:");
            printMatrix(rotated);

            PrintWriter writer = new PrintWriter(outputFile);

            writer.println(n);

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    writer.print(rotated[i][j] + " ");
                }
                writer.println();
            }

            writer.close();

            System.out.println("Результат успішно записано у файл.");

        } catch (FileNotFoundException e) {
            System.out.println("Помилка: файл не знайдено.");
        } catch (Exception e) {
            System.out.println("Помилка: " + e.getMessage());
        }

        scanner.close();
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int element : row) {
                System.out.print(element + " ");
            }
            System.out.println();
        }
    }
}