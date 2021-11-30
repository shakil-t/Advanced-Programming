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
public class Interface {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //Starting to learn OOP with the example of rectangles
        Rectangle a = new Rectangle();
        a.getArea(2, 3);
        a.getPerimeter(2, 3);
        a.Resize(2, 3, 2);
        a.getArea(2, 3);
        a.getPerimeter(2, 3);
    }

}
