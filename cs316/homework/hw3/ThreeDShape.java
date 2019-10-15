public class ThreeDShape implements Shape{
    private String shape;
    private double side1 = 0;
    private double side2 = 0;
    private double side3 = 0;
    private double side4 = 0;
    private double side5 = 0;
    private double side6 = 0;
    private double side7 = 0;
    private double side8 = 0;
    private double side9 = 0;
    private double side10 = 0;
    private double side11 = 0;
    private double side12 = 0;

    private double diameter = 0;
    private double radius = 0;

    public ThreeDShape(String shape, double side1) {
        this.shape = shape;
        switch (shape) {
            case "cube":
                this.side1 = side1;
                this.side2 = side1;
                this.side3 = side1;
                this.side4 = side1;
                this.side5 = side1;
                this.side6 = side1;
                this.side7 = side1;
                this.side8 = side1;
                this.side9 = side1;
                this.side10 = side1;
                this.side11 = side1;
                this.side12 = side1;
            case "sphere":
                this.side1 = side1;
                this.diameter = (this.side1 / Math.PI);
                this.radius = this.diameter / 2;
            case "tetrahedron":
                this.side1 = side1;
                this.side2 = side1;
                this.side3 = side1;
                this.side4 = side1;
                this.side5 = side1;
                this.side6 = side1;
        }
    }

    @Override
    public double getVolume() {
        double volume = 0;
        switch (this.shape) {
            case "cube":
                volume = Math.pow(this.side1, 3);
                return volume;
            case "tetrahedron":
                double numerator = (Math.pow(this.side1, 3));
                double denominator = (6 * (Math.sqrt(2)));
                volume = numerator / denominator;
                return volume;
            case "sphere":
                volume = ((4/3) * Math.PI * Math.pow(this.radius, 3));
                return volume;
        }
        return volume;
    }

    @Override
    public double getArea() {
        double area = 0;
        switch (this.shape) {
            case "cube":
                area = this.side1 * this.side3;
                return area;
            case "tetrahedron":
                double s = ((this.side1 + this.side2 + this.side3) / 2);
                double element = (s * (s - this.side1) * (s - this.side2) * (s - this.side3));
                area = Math.sqrt(element);
                return area;
            case "sphere":
                this.diameter = (this.side1 / Math.PI);
                this.radius = this.diameter / 2;
                area = (Math.PI * this.radius);
                return area;
        }
        return area;
    }

    @Override
    public String printShape() {
        String returnedShape = this.shape;
        return returnedShape;
    }
}