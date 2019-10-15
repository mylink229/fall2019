public class TwoDShape implements Shape{
    private String shape;
    // left side
    private double side1 = 0; 
    // bottom side
    private double side2 = 0;
    // right side
    private double side3 = 0;
    // top side
    private double side4 = 0;

    private double diameter = 0;

    private double radius = 0;

    //circle or square
    public TwoDShape(String shape, double side1) {
        this.shape = shape;
        switch (shape) {
            case "circle":
                this.side1 = side1;
            case "square":
                this.side1 = side1;
                this.side2 = side1;
                this.side3 = side1;
                this.side4 = side1;
        }
    }

    //triangle
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
                return area;
            case "triangle":
                double s = ((this.side1 + this.side2 + this.side3) / 2);
                double element = (s * (s - this.side1) * (s - this.side2) * (s - this.side3));
                area = Math.sqrt(element);
                return area;
            case "circle":
                this.diameter = (this.side1 / Math.PI);
                this.radius = this.diameter / 2;
                area = (Math.PI * this.radius);
                return area;
        }
        return area;
    }

    @Override
    public String printShape() {
       String  returnedShaped = this.shape;
       return returnedShaped;
    }
}