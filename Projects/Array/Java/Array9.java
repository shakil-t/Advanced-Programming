/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package array9;

/**
 *
 * @author Shakila
 */
import java.util.Scanner;
public class Array9 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner(System.in);
        double[][] matrix = new double[2][2];
        System.out.println(" Enter the elements of the matrix ");
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                matrix[i][j] = input.nextDouble();
            }
        }
        double a = matrix[1][1];
        double d = matrix[2][2];
        double b = matrix[1][2];
        double c = matrix[2][1];
        System.out.println(d * a);
    }

}
