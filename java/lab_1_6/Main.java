package lab_1_6;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public class Main {
    public static void bucketSort(double[] arr) {
        int n = arr.length;
        if (n <= 0) return;

        ArrayList<Double>[] buckets = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            buckets[i] = new ArrayList<>();
        }

        for (int i = 0; i < n; i++) {
            int bucketIdx = (int) (arr[i] * n);
            if (bucketIdx >= n) {
                bucketIdx = n - 1;
            }
            buckets[bucketIdx].add(arr[i]);
        }

        int index = 0;
        for (int i = 0; i < n; i++) {
            Collections.sort(buckets[i]);
            for (int j = 0; j < buckets[i].size(); j++) {
                arr[index++] = buckets[i].get(j);
            }
        }
    }

    private static double[] generateRandomArray(int size) {
        double[] arr = new double[size];
        Random random = new Random();
        for (int i = 0; i < size; i++) {
            arr[i] = random.nextDouble();
        }
        return arr;
    }

    public static void main(String[] args) {
        int[] sizes = {100, 10000, 1000000};

        System.out.println(String.format("| %-15s | %-20s |", "Розмір масиву (N)", "Час виконання (мс)"));
        System.out.println("---------------------------------------------");

        for (int size : sizes) {
            double[] arr = generateRandomArray(size);

            long startTime = System.currentTimeMillis();
            bucketSort(arr);
            long endTime = System.currentTimeMillis();

            long duration = endTime - startTime;
            System.out.println(String.format("| %-15d | %-20d |", size, duration));
        }
        System.out.println("---------------------------------------------");
    }
}