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
public interface Resizeable {
    public abstract void Resize(double w, double h, double x);
    public abstract void getArea(double w, double h);
    public abstract void getPerimeter(double x, double y);
}
