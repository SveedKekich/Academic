package lab_1_5;

import java.util.Scanner;

class Student {
    private String lastName;
    private String group;
    private String faculty;
    private long insurancePolicy;

    public Student(String lastName, String group, String faculty, long insurancePolicy) {
        this.lastName = lastName;
        this.group = group;
        this.faculty = faculty;
        this.insurancePolicy = insurancePolicy;
    }

    public long getInsurancePolicy() {
        return insurancePolicy;
    }

    public String getGroup() {
        return group;
    }

    public String getFaculty() {
        return faculty;
    }

    @Override
    public String toString() {
        return String.format("| %-12s | %-6s | %-12s | %-12d |", 
                lastName, group, faculty, insurancePolicy);
    }
}

public class Main {
    public static int binarySearch(Student[] students, long targetPolicy) {
        int low = 0;
        int high = students.length - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (students[mid].getInsurancePolicy() == targetPolicy) {
                return mid;
            }
            if (students[mid].getInsurancePolicy() < targetPolicy) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }

    public static void printArray(Student[] students) {
        System.out.println(new String(new char[53]).replace("\0", "-"));
        System.out.printf("| %-12s | %-6s | %-12s | %-12s |\n", 
                "Прізвище", "Група", "Факультет", "Поліс");
        System.out.println(new String(new char[53]).replace("\0", "-"));
        for (Student student : students) {
            System.out.println(student);
        }
        System.out.println(new String(new char[53]).replace("\0", "-"));
    }

    public static void main(String[] args) {
        Student[] students = {
            new Student("Іванов", "ІП-31", "ФІОТ", 100002),
            new Student("Петров", "ІП-31", "ФІОТ", 100005),
            new Student("Сидоров", "ІП-32", "ФІОТ", 100012),
            new Student("Коваленко", "КН-21", "ФЕКС", 100019),
            new Student("Бойко", "КН-21", "ФЕКС", 100020),
            new Student("Мельник", "КН-22", "ФЕКС", 100035),
            new Student("Шевченко", "ПІ-41", "ІПСА", 100040),
            new Student("Бондар", "ПІ-41", "ІПСА", 100044),
            new Student("Ткаченко", "ПІ-42", "ІПСА", 100051),
            new Student("Козак", "ОМ-11", "ФМФ", 100060),
            new Student("Мороз", "ОМ-11", "ФМФ", 100067),
            new Student("Лисенко", "ОМ-12", "ФМФ", 100072),
            new Student("Кравченко", "БІ-21", "ФБМІ", 100078),
            new Student("Поліщук", "БІ-21", "ФБМІ", 100083),
            new Student("Марченко", "БІ-22", "ФБМІ", 100089),
            new Student("Олійник", "ЕК-31", "ФЕА", 100091),
            new Student("Руденко", "ЕК-31", "ФЕА", 100094),
            new Student("Гончар", "ЕК-32", "ФЕА", 100096),
            new Student("Кузнєцов", "РТ-11", "РТФ", 100098),
            new Student("Савченко", "РТ-11", "РТФ", 100100)
        };

        System.out.println("ВМІСТ ОДНОВИМІРНОГО МАСИВУ (УПОРЯДКОВАНИЙ ЗА ПОЛІСОМ):");
        printArray(students);

        Scanner scanner = new Scanner(System.in);
        System.out.print("Введіть номер медичного полісу для пошуку: ");
        long targetPolicy = scanner.nextLong();

        int resultIndex = binarySearch(students, targetPolicy);

        System.out.println("\nРЕЗУЛЬТАТ ВИКОНАННЯ ЗАВДАННЯ:");
        if (resultIndex != -1) {
            Student found = students[resultIndex];
            System.out.println("Студента знайдено!");
            System.out.println("Факультет: " + found.getFaculty());
            System.out.println("Група: " + found.getGroup());
        } else {
            System.out.println("Студента з таким номером полісу не знайдено.");
        }
        scanner.close();
    }
}