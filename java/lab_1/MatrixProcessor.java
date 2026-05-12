package lab_1;
import java.util.Random;

public class MatrixProcessor {
    public static void main(String[] args) {
        System.out.println("Розробник: Світличний Д. Є.");

        int rows = 4;
        int cols = 3;
        int[][] B = new int[rows][cols];
        Random random = new Random();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                B[i][j] = random.nextInt(101) - 50; 
            }
        }

        System.out.println("Матриця до обробки:");
        printMatrix(B);

        int sumNegativeOdd = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (B[i][j] < 0 && B[i][j] % 2 != 0) {
                    sumNegativeOdd += B[i][j];
                }
            }
        }

        System.out.println("\nРезультати:");
        System.out.println("- сума всіх від'ємних непарних елементів: " + sumNegativeOdd);
        System.out.println("- матриця В:");
        printMatrix(B);
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int element : row) {
                System.out.printf("%4d ", element);
            }
            System.out.println();
        }
    }
}