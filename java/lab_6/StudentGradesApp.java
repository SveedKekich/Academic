package lab_6;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Arrays;

public class StudentGradesApp {
    public static void main(String[] args) {
        Map<String, List<Integer>> gradeJournal = new HashMap<>();

        gradeJournal.put("Іваненко", Arrays.asList(95, 98, 100, 92));
        gradeJournal.put("Петренко", Arrays.asList(85, 70, 90, 88));
        gradeJournal.put("Сидоренко", Arrays.asList(91, 95, 89, 94));
        gradeJournal.put("Коваленко", Arrays.asList(60, 75, 80, 70));
        gradeJournal.put("Бондаренко", Arrays.asList(99, 100, 97, 98));

        System.out.println("Повний журнал успішності:");
        gradeJournal.forEach((name, grades) -> System.out.println(name + ": " + grades));

        Map<String, Double> lowPerformers = new HashMap<>();

        for (Map.Entry<String, List<Integer>> entry : gradeJournal.entrySet()) {
            double average = calculateAverage(entry.getValue());
            
            if (average < 90) {
                lowPerformers.put(entry.getKey(), average);
            }
        }

        System.out.println("\nСтуденти, чий середній бал нижче за 90:");
        if (lowPerformers.isEmpty()) {
            System.out.println("Таких студентів не знайдено.");
        } else {
            lowPerformers.forEach((name, avg) -> 
                System.out.printf("Студент: %s | Середній бал: %.2f\n", name, avg));
        }
    }

    private static double calculateAverage(List<Integer> grades) {
        if (grades == null || grades.isEmpty()) return 0;
        int sum = 0;
        for (int grade : grades) {
            sum += grade;
        }
        return (double) sum / grades.size();
    }
}