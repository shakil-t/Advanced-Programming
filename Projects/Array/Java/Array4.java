/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package array4;

/**
 *
 * @author Shakila
 */
import java.util.Scanner;
public class Array4 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner(System.in);
        int[] array = new int[10];
        boolean flag = false;
        System.out.println(" Enter the students number ");
        for (int i = 0; i < 10; i++) {
            array[i] = input.nextInt();
        }
        int m;
        System.out.println(" Enter the student number ");
        m = input.nextInt();
        for (int j = 0; j < 10; j++) {
            if (array[j] == m) {
                flag = true;
            }
        }
        if (flag == true) {
            System.out.println(" Seen! ");
        } else {
            System.out.println(" Not seen! ");
        }
    }

}
