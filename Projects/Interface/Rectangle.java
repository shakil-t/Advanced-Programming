/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pkginterface;

/**
 *
 * @author Shakila
 */
public class Rectangle implements Resizeable {

    @Override
    public void Resize(double w, double h, double x) {
        w = w * x;
        h = h * x;
        System.out.println(" New width :" + w);
        System.out.println(" New height :" + h);
    }

    @Override
    public void getArea(double w, double h) {
        System.out.println(" Area :" + w * h);
    }

    @Override
    public void getPerimeter(double x, double y) {
        System.out.println(" Perimeter :" + 2 * (x + y));
    }

}
