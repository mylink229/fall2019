public class ThreeDShape implements Shape{
    private String shape;
    private double base;
    private double width;
    private double height;

    public ThreeDShape(
        String shape, 
        double base, 
        double width,
        double height
        ) {
        this.shape = shape;
        this.base = base;
        this.width = width;
        this.height = height;
    }

    @Override
    public double getVolume() {
        double volume = (base * height * width);
        return volume;
    }

    @Override
    public double getArea() {
        double area = base * height;
        return area;
    }

    @Override
    public String printShape() {
        String returnedShape = this.shape;
        return returnedShape;
    }

}