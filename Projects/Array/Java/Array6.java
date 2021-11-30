/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package array6;

/**
 *
 * @author Shakila
 */
import java.util.Scanner;
public class Array6 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner(System.in);
        int s1;
        System.out.println(" Enter the size of the first array ");
        s1 = input.nextInt();
        int s2;
        System.out.println(" Enter the size of the second array ");
        s2 = input.nextInt();
        double[] array1 = new double[s1];
        System.out.println(" Enter the elements of the first array ");
        for (int a = 0; a < s1; a++) {
            array1[a] = input.nextDouble();
        }
        double[] array2 = new double[s2];
        System.out.println(" Enter the elements of the second array ");
        for (int b = 0; b < s2; b++) {
            array2[b] = input.nextDouble();
        }
        double[] array3 = new double[s1 + s2];
        int i = 0, j = 0, k = 0;
        while (i < s1 && j < s2) {
            if (array1[i] > array2[j]) {
                array3[k] = array1[i];
                k++;
                i++;
            } else {
                array3[k] = array2[j];
                k++;
                j++;
            }
        }
        for (int c = 0; c < array3.length; c++) {
            System.out.println(array3[c]);
        }
    }

}
