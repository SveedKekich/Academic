package lab_2_2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        String fileName = "words.txt";

        try (FileWriter writer = new FileWriter(fileName)) {
            writer.write("(5%A)\n");
            writer.write("hello\n");
            writer.write("(789*XYZ)\n");
            writer.write("(56%)\n");
            writer.write("(5%ABC)\n");
            writer.write("(4*A)\n");
            writer.write("(9999*Z)\n");
            writer.write("test(5%A)\n");
        } catch (IOException e) {
            e.printStackTrace();
        }

        String regex = "^\\([5-9]+[%*][A-Z]+\\)$";
        Pattern pattern = Pattern.compile(regex);

        System.out.println("Знайдені слова, що відповідають регулярному виразу:");
        System.out.println("------------------------------------------------");

        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                Matcher matcher = pattern.matcher(line);
                if (matcher.matches()) {
                    System.out.println(line);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("------------------------------------------------");
    }
}