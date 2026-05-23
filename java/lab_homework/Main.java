package lab_homework;

public class Main {
    public static double[] solveLUP(double[][] A, double[] b) {
        int n = A.length;
        double[][] LU = new double[n][n];
        for (int i = 0; i < n; i++) {
            System.arraycopy(A[i], 0, LU[i], 0, n);
        }

        int[] P = new int[n];
        for (int i = 0; i < n; i++) {
            P[i] = i;
        }

        for (int i = 0; i < n; i++) {
            double maxPivot = 0;
            int pivotRow = i;
            for (int r = i; r < n; r++) {
                if (Math.abs(LU[r][i]) > maxPivot) {
                    maxPivot = Math.abs(LU[r][i]);
                    pivotRow = r;
                }
            }

            if (maxPivot < 1e-9) {
                return null;
            }

            int tempP = P[i];
            P[i] = P[pivotRow];
            P[pivotRow] = tempP;

            double[] tempRow = LU[i];
            LU[i] = LU[pivotRow];
            LU[pivotRow] = tempRow;

            for (int j = i + 1; j < n; j++) {
                LU[j][i] /= LU[i][i];
                for (int k = i + 1; k < n; k++) {
                    LU[j][k] -= LU[j][i] * LU[i][k];
                }
            }
        }

        double[] y = new double[n];
        for (int i = 0; i < n; i++) {
            double sum = 0;
            for (int j = 0; j < i; j++) {
                sum += LU[i][j] * y[j];
            }
            y[i] = b[P[i]] - sum;
        }

        double[] x = new double[n];
        for (int i = n - 1; i >= 0; i--) {
            double sum = 0;
            for (int j = i + 1; j < n; j++) {
                sum += LU[i][j] * x[j];
            }
            x[i] = (y[i] - sum) / LU[i][i];
        }

        return x;
    }

    public static void main(String[] args) {
        double[][] A = {
            {  0,   4, -1, -6},
            {  6,   7,  2,  7},
            {-10, -10,  5, -10},
            {  6,   1,  4,  0}
        };

        double[] b = {-38, 50, -70, -5};

        double[] x = solveLUP(A, b);

        System.out.println("РЕЗУЛЬТАТ РОЗВ'ЯЗАННЯ СЛАР МЕТОДОМ LUP:");
        System.out.println("---------------------------------------");
        if (x != null) {
            for (int i = 0; i < x.length; i++) {
                System.out.printf("x%d = %7.4f\n", (i + 1), x[i]);
            }
        } else {
            System.out.println("Матриця вироджена або розв'язків не існує.");
        }
        System.out.println("---------------------------------------");
    }
}