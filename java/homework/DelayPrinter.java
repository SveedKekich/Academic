package homework;

public class DelayPrinter {
    public static void main(String[] args) {
        
        Thread t1 = new Thread(() -> {
            try {
                Thread.sleep(1000);
                System.out.println("1");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        Thread t2 = new Thread(() -> {
            try {
                Thread.sleep(2000);
                System.out.println("2");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        Thread t3 = new Thread(() -> {
            try {
                Thread.sleep(3000);
                System.out.println("3");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        t1.start();
        t2.start();
        t3.start();
    }
}