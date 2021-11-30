/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package array1;

/**
 *
 * @author Shakila
 */
import java.util.Scanner;
public class Array1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner(System.in);
        double[] array = new double[20];
        System.out.println(" Enter the numbers ");
        for (int i = 0; i < 20; i++) {
            array[i] = input.nextDouble();
        }
        for (int j = 19; 0 <= j; j--) {
            System.out.println(array[j]);
        }
    }
}
