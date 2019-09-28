public class Main {
    public static void main(String[] args) {
        try {
            DateAndTime obj1 = new DateAndTime(59, 59, 1, 30, 12, 1998);
            String original = obj1.toString();

            System.out.println(obj1.toString());

            obj1.incrementSec();
            System.out.println("Adding sec..." + obj1.toString());

            obj1.incrementMin();
            System.out.println("Adding min..." + obj1.toString());

            obj1.incrementHr();
            System.out.println("Adding hr..." + obj1.toString());

            obj1.incrementDay();
            System.out.println("Adding day..." + obj1.toString());

            obj1.incrementMonth();
            System.out.println("Adding month..." + obj1.toString());

            obj1.incrementYear();
            System.out.println("Adding year..." + obj1.toString());

            String editted = obj1.toString();

            System.out.println("Original: " + original);
            System.out.println("Editted: " + editted);
        } catch (OutOfBounds e) {
            System.out.println(e.getMessage());
        }
    }
}