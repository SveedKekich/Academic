package lab_1_2;

class Rhombus {
    private double x1, y1;
    private double x2, y2;
    private double x3, y3;
    private double x4, y4;

    public Rhombus(double x1, double y1, double x2, double y2, 
                   double x3, double y3, double x4, double y4) {
        this.x1 = x1; this.y1 = y1;
        this.x2 = x2; this.y2 = y2;
        this.x3 = x3; this.y3 = y3;
        this.x4 = x4; this.y4 = y4;
    }

    private double sideLength(double xa, double ya, double xb, double yb) {
        return Math.sqrt(Math.pow(xb - xa, 2) + Math.pow(yb - ya, 2));
    }

    public double getPerimeter() {
        double side = sideLength(x1, y1, x2, y2);
        return 4 * side;
    }

    public double getArea() {
        double d1 = sideLength(x1, y1, x3, y3);
        double d2 = sideLength(x2, y2, x4, y4);
        return 0.5 * d1 * d2;
    }

    @Override
    public String toString() {
        return String.format("Ромб [Вершини: (%.1f,%.1f), (%.1f,%.1f), (%.1f,%.1f), (%.1f,%.1f) | Площа: %.2f | Периметр: %.2f]",
                x1, y1, x2, y2, x3, y3, x4, y4, getArea(), getPerimeter());
    }
}

class OpenAddressingHashTable {
    private Rhombus[] table;
    private int capacity;
    private int size;
    private static final double A = 0.6180339887; 

    public OpenAddressingHashTable(int capacity) {
        this.capacity = capacity;
        this.table = new Rhombus[capacity];
        this.size = 0;
    }

    private int hashFunction(double key) {
        double fractionalPart = (key * A) % 1;
        if (fractionalPart < 0) {
            fractionalPart += 1; 
        }
        return (int) (capacity * fractionalPart);
    }

    public void insert(Rhombus rhombus) {
        if (rhombus == null) return;

        if ((double) size / capacity >= 0.75) {
            resize();
        }

        double key = rhombus.getArea();
        int hash = hashFunction(key);
        int index = hash;
        int i = 0;

        while (table[index] != null) {
            i++;
            index = (hash + i) % capacity; 
            
            if (i == capacity) {
                resize();
                insert(rhombus);
                return;
            }
        }

        table[index] = rhombus;
        size++;
    }

    private void resize() {
        int oldCapacity = capacity;
        Rhombus[] oldTable = table;

        capacity = oldCapacity * 2;
        table = new Rhombus[capacity];
        size = 0;

        for (int i = 0; i < oldCapacity; i++) {
            if (oldTable[i] != null) {
                insert(oldTable[i]);
            }
        }
    }

    public void printTable() {
        System.out.println("\n=== ВМІСТ ХЕШ-ТАБЛИЦІ ===");
        for (int i = 0; i < capacity; i++) {
            if (table[i] != null) {
                System.out.printf("Індекс [%d] -> %s\n", i, table[i].toString());
            } else {
                System.out.printf("Індекс [%d] -> [Порожньо]\n", i);
            }
        }
        System.out.println("=========================");
    }
}

public class Main {
    public static void main(String[] args) {
        OpenAddressingHashTable hashTable = new OpenAddressingHashTable(7);

        Rhombus r1 = new Rhombus(0, 2, 3, 4, 6, 2, 3, 0);   
        Rhombus r2 = new Rhombus(1, 4, 4, 8, 7, 4, 4, 0);   
        Rhombus r3 = new Rhombus(0, 1, 2, 2, 4, 1, 2, 0);   
        Rhombus r4 = new Rhombus(-2, 0, 0, 3, 2, 0, 0, -3); 
        Rhombus r5 = new Rhombus(1, 1, 2, 4, 3, 1, 2, -2); 

        hashTable.insert(r1);
        hashTable.insert(r2);
        hashTable.insert(r3);
        hashTable.insert(r4); 
        hashTable.insert(r5);

        hashTable.printTable();
    }
}