/*public class Shape {
    protected double base;
    protected double height;
    protected double width;
    protected double side1;
    protected double side2;
    protected double side3;
    protected double side4;
    protected double diameter;
    protected double radius = diameter / 2;
    protected double circumference;
    protected double distance;
    protected double distance1;
    protected double distance2;
    protected boolean twoDimensionalShape;

    public Shape () {
    }

    public Shape(double base, double height, boolean twoDimensionalShape) {
        this.base = base;
        this.height = height;
        this.twoDimensionalShape = twoDimensionalShape;
    }

    public Shape(double base, double height, double width, boolean twoDimensionalShape) {
        this.base = base;
        this.height = height;
        this.width = width;
        this.twoDimensionalShape = twoDimensionalShape;
    }
}*/

interface Shape {
    public double getArea();
    public double getVolume();
    public String printShape();
}
