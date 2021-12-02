/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pkgabstract;

/**
 *
 * @author Shakila
 */
public class RtTriangle extends Shape{

    public RtTriangle(int numSides) {
        super(numSides);
    }

    @Override
    public double getArea(double w, double h) {
        System.out.println(" Area :"+(w*h)/2);
        return (w*h)/2;
    }

    @Override
    public double getPerimeter(double x, double y, double z) {
        System.out.println(" Perimeter :"+x+y+z);
        return x+y+z;
    }
    
}
