/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package array3;

/**
 *
 * @author Shakila
 */
import java.util.Scanner;
public class Array3 {

    /**
     * @param args the command line arguments
     */
    public static double getMax(double[] array) {
        double max = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }
        return max;
    }
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner(System.in);
        double[] array = new double[20];
        System.out.println(" Enter the numbers ");
        for (int i = 0; i < 20; i++) {
            array[i] = input.nextDouble();
        }
        double max = getMax(array);
        System.out.println(" Max value is " + max);
        for (int j = 0; j < 20; j++) {
            if (array[j] == max) {
                System.out.println(j);
            }
        }
    }

}
