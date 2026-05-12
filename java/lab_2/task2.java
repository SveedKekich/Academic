package lab_2;
public class task2 {
    public static void main(String[] args) {
        String originalText = "Hello, World! 123. This is a test: variant #17 - processing text...";
        
        String processedText = originalText.replaceAll("[^\\p{L}\\s]", "");
        
        System.out.println("=== Input Parameters ===");
        System.out.println("Transformation Rule: Keep only letters and spaces.");
        System.out.println("Regex Pattern Used: [^\\p{L}\\s]");
        System.out.println();

        System.out.println("=== Text Processing ===");
        System.out.println("Text BEFORE processing:");
        System.out.println(originalText);
        
        System.out.println("\nText AFTER processing:");
        System.out.println(processedText);
    }
}
