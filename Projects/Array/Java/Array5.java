/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package array5;

/**
 *
 * @author Shakila
 */
import java.util.Scanner;
public class Array5 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner(System.in);
        double[] array = new double[20];
        int counter = 0;
        System.out.println(" Enter the numbers ");
        for (int i = 0; i < 20; i++) {
            array[i] = input.nextDouble();
        }
        double m;
        System.out.println(" Choose one of the numbers ");
        m = input.nextDouble();
        for (int j = 0; j < 20; j++) {
            if (array[j] == m) {
                counter++;
            }
        }
        System.out.println(counter);
    }

}
