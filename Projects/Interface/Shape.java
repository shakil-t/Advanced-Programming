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
public abstract class Shape {
 public int numSides;
 public Shape(int numSides){
     this.numSides=numSides;
 }
 public int getNumSides(){
     return numSides;
 }
 public abstract double getArea(double w,double h);
 public abstract double getPerimeter(double x,double y,double z);
}
