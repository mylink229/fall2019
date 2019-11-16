import java.util.scanner;

public class DateValidation {
    public static boolean validateDate() {
        return str.matches("\\d{2}/\\d{2}/\\d{4}");
    }

    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Enter a date in MM/DD/YYYY");
        String userInput = keyboard.next();
    }
}
