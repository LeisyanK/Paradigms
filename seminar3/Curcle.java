package seminar3;

public class Curcle extends Shape{
    private double radius;

    public Curcle(int r) {
        this.radius = r;
    }

    @Override
    public double getArea() {
        // TODO Auto-generated method stub
        // throw new UnsupportedOperationException("Unimplemented method 'getArea'");
        return Math.PI * radius * radius;
    }

    @Override
    public double getPerimeter() {
        // TODO Auto-generated method stub
        // throw new UnsupportedOperationException("Unimplemented method 'getPerimeter'");
        return 2 * Math.PI * radius;
    }
    
}
