package lab_1_4;

class Student {
    private String lastName;
    private String firstName;
    private String electiveCourse;
    private double grade;

    public Student(String lastName, String firstName, String electiveCourse, double grade) {
        this.lastName = lastName;
        this.firstName = firstName;
        this.electiveCourse = electiveCourse;
        this.grade = grade;
    }

    public double getGrade() {
        return grade;
    }

    @Override
    public String toString() {
        return String.format("| %-12s | %-10s | %-20s | %-5.1f |", 
                lastName, firstName, electiveCourse, grade);
    }
}

public class Main {
    public static void bubbleSortDescending(Student[] students) {
        int n = students.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (students[j].getGrade() < students[j + 1].getGrade()) {
                    Student temp = students[j];
                    students[j] = students[j + 1];
                    students[j + 1] = temp;
                }
            }
        }
    }

    public static void printArray(Student[] students) {
        System.out.println(new String(new char[59]).replace("\0", "-"));
        System.out.printf("| %-12s | %-10s | %-20s | %-5s |\n", 
                "Прізвище", "Ім'я", "Факультатив", "Бал");
        System.out.println(new String(new char[59]).replace("\0", "-"));
        for (Student student : students) {
            System.out.println(student);
        }
        System.out.println(new String(new char[59]).replace("\0", "-"));
    }

    public static void main(String[] args) {
        Student[] students = {
            new Student("Петренко", "Іван", "Криптографія", 84.5),
            new Student("Сидоренко", "Олена", "Штучний інтелект", 95.0),
            new Student("Козак", "Дмитро", "Веб-розробка", 71.2),
            new Student("Лисенко", "Анна", "Криптографія", 88.9),
            new Student("Мороз", "Вадим", "Штучний інтелект", 63.4)
        };

        System.out.println("МАСИВ ДО СОРТУВАННЯ:");
        printArray(students);

        bubbleSortDescending(students);

        System.out.println("\nМАСИВ ПІСЛЯ СОРТУВАННЯ (ЗА СПАДАННЯМ БАЛА):");
        printArray(students);
    }
}