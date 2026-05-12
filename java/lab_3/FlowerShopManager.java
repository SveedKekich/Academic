package lab_3;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Flower {
    private int id;
    private String name;
    private String type;
    private String species;
    private String subspecies;
    private double price;
    private int quantity;

    public Flower(int id, String name, String type, String species, String subspecies, double price, int quantity) {
        this.id = id;
        this.name = name;
        this.type = type;
        this.species = species;
        this.subspecies = subspecies;
        this.price = price;
        this.quantity = quantity;
    }

    public int getId() { return id; }
    public String getName() { return name; }
    public String getType() { return type; }
    public String getSpecies() { return species; }
    public String getSubspecies() { return subspecies; }
    public double getPrice() { return price; }
    public int getQuantity() { return quantity; }

    @Override
    public String toString() {
        return String.format("| %-5d | %-12s | %-12s | %-12s | %-15s | %-8.2f | %-8d |", 
                id, name, type, species, subspecies, price, quantity);
    }
}

public class FlowerShopManager {
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        List<Flower> inventory = new ArrayList<>();
        
        System.out.println("--- Flower Shop Inventory Input ---");
        for (int i = 0; i < 5; i++) {
            System.out.println("Enter details for flower #" + (i + 1));
            inventory.add(inputFlowerWithValidation());
        }

        displayInventory("Initial Inventory", inventory);

        System.out.println("\n--- Task 1: Indoor blooming plants ---");
        List<Flower> bloomingIndoor = new ArrayList<>();
        for (Flower f : inventory) {
            if (f.getType().equalsIgnoreCase("Indoor") || f.getType().equalsIgnoreCase("Кімнатна")) {
                bloomingIndoor.add(f);
            }
        }
        displayInventory("Blooming Indoor Plants", bloomingIndoor);

        System.out.println("\n--- Task 2: Search subspecies by name ---");
        System.out.print("Enter flower name to search for subspecies: ");
        String searchName = scanner.next();
        
        List<Flower> subspeciesResult = new ArrayList<>();
        for (Flower f : inventory) {
            if (f.getName().equalsIgnoreCase(searchName)) {
                subspeciesResult.add(f);
            }
        }
        displayInventory("Subspecies of " + searchName, subspeciesResult);
    }

    private static Flower inputFlowerWithValidation() {
        while (true) {
            try {
                System.out.print("ID (int): ");
                int id = Integer.parseInt(scanner.next());

                System.out.print("Name: ");
                String name = scanner.next();

                System.out.print("Type (e.g., Indoor): ");
                String type = scanner.next();

                System.out.print("Species: ");
                String species = scanner.next();

                System.out.print("Subspecies: ");
                String subspecies = scanner.next();

                System.out.print("Price (double): ");
                double price = Double.parseDouble(scanner.next());
                if (price < 0) throw new IllegalArgumentException("Price cannot be negative.");

                System.out.print("Quantity (int): ");
                int quantity = Integer.parseInt(scanner.next());
                if (quantity < 0) throw new IllegalArgumentException("Quantity cannot be negative.");

                return new Flower(id, name, type, species, subspecies, price, quantity);

            } catch (NumberFormatException e) {
                System.out.println("Error: Invalid data type entered. Please try again.");
            } catch (IllegalArgumentException e) {
                System.out.println("Error: " + e.getMessage());
            }
        }
    }

    private static void displayInventory(String title, List<Flower> flowers) {
        System.out.println("\n" + title);
        if (flowers.isEmpty()) {
            System.out.println("No data found for the given criteria.");
            return;
        }
        System.out.println("---------------------------------------------------------------------------------------------");
        System.out.println("| ID    | Name         | Type         | Species      | Subspecies      | Price    | Quantity |");
        System.out.println("---------------------------------------------------------------------------------------------");
        for (Flower f : flowers) {
            System.out.println(f);
        }
        System.out.println("---------------------------------------------------------------------------------------------");
    }
}
