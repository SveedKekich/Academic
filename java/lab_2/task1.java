package lab_2;
import java.util.Random;

public class task1 {
    public static void main(String[] args) {
        Random random = new Random();
        int length = 5; 
        StringBuilder sb = new StringBuilder();
        
        sb.append(random.nextInt(9) + 1); 
        for (int i = 1; i < length; i++) {
            sb.append(random.nextInt(10));
        }
        
        String originalNumber = sb.toString();
        System.out.println("Original number:  " + originalNumber);

        StringBuilder result = new StringBuilder();

        for (int i = 0; i < originalNumber.length(); i++) {
            char c = originalNumber.charAt(i);
            int digit = Character.getNumericValue(c);
            
            String transformed;

            if (digit == 2) {
                transformed = "1";
            } else if (digit == 9) {
                transformed = "0";
            } else if (digit % 2 == 0) {
                transformed = String.valueOf(digit * 2);
            } else {
                transformed = String.valueOf(digit);
            }
            
            result.append(transformed);
        }

        System.out.println("Transformed result: " + result.toString());
    }
}