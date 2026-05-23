package lab_2_3;

import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        int leadersCount = 5;
        int studentsCount = 20;

        BigInteger ways = BigInteger.valueOf(leadersCount).pow(studentsCount);

        System.out.println("РЕЗУЛЬТАТ ОБЧИСЛЕННЯ:");
        System.out.println("------------------------------------------------");
        System.out.println("Кількість студентів: " + studentsCount);
        System.out.println("Кількість керівників: " + leadersCount);
        System.out.println("Кількість способів розподілу: " + ways);
        System.out.println("------------------------------------------------");
    }
}