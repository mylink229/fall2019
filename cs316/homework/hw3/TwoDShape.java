public class TwoDShape implements Shape{
    private String shape;
    /*private double base;
    private double height;*/

    // left side
    private double side1; 
    // bottom side
    private double side2;
    // right side
    private double side3;
    // top side
    private double side4;

    private double triangleLeg;


    public TwoDShape(String shape, double side1) {
        this.shape = shape;
        this.side1 = side1;
    }

    public TwoDShape(
        String shape, 
        double side1,
        double side2,
        double side3
        ) {
        this.shape = shape;
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    public TwoDShape(
        String shape, 
        double side1,
        double side2,
        double side3,
        double side4
        ) {
        this.shape = shape;
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
        this.side4 = side4;
    }

    @Override
    public double getVolume() {
        return 0;
    }

    @Override
    public double getArea() {
        double area = 0;
        switch (this.shape) {
            case "square":
                area = this.side1 * this.side3;
                break;
            case "triangle":
                double s = ((this.side1 + this.side2 + this.side3) / 2);
                double element = 
                area = Math.sqrt();
                break;
        }
        return area;
    }

    @Override
    public String printShape() {
       String  returnedShaped = this.shape;
       return returnedShaped;
    }
}