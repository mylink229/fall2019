public class Main { public static void main(String[] args) {
        TwoDShape square = new TwoDShape("square", 2.0);
        TwoDShape circle = new TwoDShape("circle", 1.0);
        TwoDShape triangle = new TwoDShape("triangle", 2.0, 2.0, 2.0);

        ThreeDShape cube = new ThreeDShape("cube", 1.0);
        ThreeDShape sphere = new ThreeDShape("sphere", 2.0);
        ThreeDShape regularTetra = new ThreeDShape("tetrahedron", 3.0);

        Class twoD = square.getClass();
        Class threeD = cube.getClass();

        Shape[] shapeArr = new Shape[6];
        shapeArr[0] = square;
        shapeArr[1] = circle;
        shapeArr[2] = triangle;

        shapeArr[3] = cube;
        shapeArr[4] = sphere;
        shapeArr[5] = regularTetra;

        for(int i = 0; i < shapeArr.length; i++) {
            System.out.println("This is a: " + shapeArr[i].printShape());
            if (shapeArr[i].getClass() == twoD) {
                System.out.println("Object: " + shapeArr[i].getClass());
                System.out.println("Area: " + shapeArr[i].getArea());
            } else if (shapeArr[i].getClass() == threeD) {
                System.out.println("Object: " + shapeArr[i].getClass());
                System.out.println("Area: " + shapeArr[i].getArea());
                System.out.println("Volume " + shapeArr[i].getVolume() + " cubed");
            }
            System.out.println("-----------------");
        }
    }
}