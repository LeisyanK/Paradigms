package seminar3;

public class Triangle extends Shape{
    private int side1;
    private int side2;

    public Triangle(int a, int b){
        this.side1 = a;
        this.side2 = b;
    }

    @Override
    public double getArea() {
        // TODO Auto-generated method stub
        // throw new UnsupportedOperationException("Unimplemented method 'getArea'");
        return (side1 * side2) / 2;
    }

    @Override
    public double getPerimeter() {
        // TODO Auto-generated method stub
        // throw new UnsupportedOperationException("Unimplemented method 'getPerimeter'");
        return this.side1 + this.side2 + Math.sqrt(this.side1 * this.side1 + this.side2 * this.side2);
    }
 
}