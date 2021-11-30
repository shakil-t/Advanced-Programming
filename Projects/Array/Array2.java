/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package array2;

/**
 *
 * @author Shakila
 */
import java.util.Scanner;
public class Array2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner(System.in);
        double[] array = new double[100];
        System.out.println(" Enter the numbers ");
        for (int i = 0; i < 100; i++) {
            array[i] = input.nextDouble();
        }
        for (int j = 0; j < 100; j++) {
            if (array[j] >= 0) {
                System.out.println(array[j]);
            }
        }
        for (int k = 0; k < 100; k++) {
            if (array[k] < 0) {
                System.out.println(array[k]);
            }
        }
    }
}
