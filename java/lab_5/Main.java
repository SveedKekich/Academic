package lab_5;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

interface Searchable {
    void findByAgeLimit(int age);
}

class Park implements Searchable {
    private String parkName;
    private List<Attraction> attractions;

    public Park(String parkName) {
        this.parkName = parkName;
        this.attractions = new ArrayList<>();
        System.out.println("Парк '" + parkName + "' створено.");
    }

    class Attraction {
        private String type;
        private String workingHours;
        private double cost;
        private int ageLimit;

        public Attraction(String type, String workingHours, double cost, int ageLimit) {
            this.type = type;
            this.workingHours = workingHours;
            this.cost = cost;
            this.ageLimit = ageLimit;
        }

        @Override
        public String toString() {
            return String.format("Атракціон: %s | Час: %s | Ціна: %.2f грн | Вік: %d+", 
                                 type, workingHours, cost, ageLimit);
        }
    }

    public void addAttraction(String type, String hours, double price, int age) {
        attractions.add(new Attraction(type, hours, price, age));
        System.out.println("Атракціон '" + type + "' додано до списку.");
    }

    @Override
    public void findByAgeLimit(int age) {
        System.out.println("\n--- Результати пошуку для віку " + age + " ---");
        boolean found = false;
        for (Attraction a : attractions) {
            if (a.ageLimit <= age) {
                System.out.println(a);
                found = true;
            }
        }
        if (!found) System.out.println("На жаль, доступних атракціонів не знайдено.");
    }

    public void displayAll() {
        System.out.println("\nСписок усіх атракціонів парку " + parkName + ":");
        for (Attraction a : attractions) System.out.println(a);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введіть назву парку: ");
        Park myPark = new Park(scanner.nextLine());

        System.out.print("Скільки атракціонів ви хочете додати? ");
        int count = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < count; i++) {
            System.out.println("\nВведення даних для атракціону #" + (i + 1));
            System.out.print("Тип: ");
            String type = scanner.nextLine();
            System.out.print("Час роботи: ");
            String hours = scanner.nextLine();
            System.out.print("Вартість: ");
            double price = Double.parseDouble(scanner.nextLine());
            System.out.print("Вікове обмеження: ");
            int age = Integer.parseInt(scanner.nextLine());

            myPark.addAttraction(type, hours, price, age);
        }

        myPark.displayAll();

        System.out.print("\nВведіть вік користувача для пошуку доступних розваг: ");
        int searchAge = Integer.parseInt(scanner.nextLine());
        myPark.findByAgeLimit(searchAge);

        scanner.close();
    }
}