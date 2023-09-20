package seminar3;

public class Square extends Shape{
    private double side;

    public Square(double a) {
        this.side = a;
    }

    @Override
    public double getArea() {
        // TODO Auto-generated method stub
        // throw new UnsupportedOperationException("Unimplemented method 'get_area'");
        return side * side;
    }

    @Override
    public double getPerimeter() {
        // TODO Auto-generated method stub
        // throw new UnsupportedOperationException("Unimplemented method 'get_perimeter'");
        return 4 * side;
    }
    
}
