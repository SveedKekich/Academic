package lab_2_1;

interface IntegrableFunction {
    double evaluate(double x);
}

public class Main {
    public static double integrateRectangles(IntegrableFunction f, double a, double b, double h) {
        double sum = 0;
        for (double x = a + h / 2; x < b; x += h) {
            sum += f.evaluate(x);
        }
        return sum * h;
    }

    public static double integrateTrapezoids(IntegrableFunction f, double a, double b, double h) {
        double sum = 0.5 * (f.evaluate(a) + f.evaluate(b));
        for (double x = a + h; x < b; x += h) {
            sum += f.evaluate(x);
        }
        return sum * h;
    }

    public static double integrateSimpson(IntegrableFunction f, double a, double b, double h) {
        int n = (int) Math.round((b - a) / h);
        if (n % 2 != 0) {
            n++;
            h = (b - a) / n;
        }
        
        double sum = f.evaluate(a) + f.evaluate(b);
        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            if (i % 2 == 0) {
                sum += 2 * f.evaluate(x);
            } else {
                sum += 4 * f.evaluate(x);
            }
        }
        return (h / 3) * sum;
    }

    public static void main(String[] args) {
        IntegrableFunction f = x -> Math.sqrt(1 + Math.pow(x, 5));
        double a = 0.0;
        double b = 2.0;
        double h = 0.25;

        double resRect = integrateRectangles(f, a, b, h);
        double resTrap = integrateTrapezoids(f, a, b, h);
        double resSimp = integrateSimpson(f, a, b, h);

        System.out.println("---------------------------------------------");
        System.out.printf("| %-22s | %-16s |\n", "Метод інтегрування", "Результат");
        System.out.println("---------------------------------------------");
        System.out.printf("| %-22s | %-16.6f |\n", "Прямокутників (середніх)", resRect);
        System.out.printf("| %-22s | %-16.6f |\n", "Трапецій", resTrap);
        System.out.printf("| %-22s | %-16.6f |\n", "Сімпсона", resSimp);
        System.out.println("---------------------------------------------");
    }
}