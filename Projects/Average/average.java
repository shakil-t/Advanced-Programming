/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package average;

/**
 *
 * @author shakil
 */
import java.io.*;
import java.util.*;
public class Average {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)
    // This code reads a student's grades from the file and calculates the average
    throws FileNotFoundException {
        Scanner input = new Scanner(new File("C:/Users/shakil/average.txt"));
        Scanner in = new Scanner(System.in);
        String firstName;
        System.out.println(" Enter the student's first name ");
        firstName = in .next();
        String lastName;
        System.out.println(" Enter the student's last name ");
        lastName = in .next();
        int counter2 = 0;
        while (input.hasNextLine()) {
            String line = input.nextLine();
            Scanner lineScan = new Scanner(line);
            String name1 = lineScan.next();
            String name2 = lineScan.next();
            if (name1.equalsIgnoreCase(firstName)) {
                double[] array = new double[10];
                System.out.println(" Here are the marks :");
                double sum = 0;
                int counter = 0;
                for (int i = 0; i < 10; i++) {
                    while (lineScan.hasNextDouble()) {
                        double mark = lineScan.nextDouble();
                        array[i] = mark;
                        sum += array[i];
                        counter++;
                        System.out.println(array[i]);
                    }
                }
                System.out.println(" The average is : ");
                System.out.println(sum / counter);
            } else {
                counter2++;
            }
        }
        if (counter2 == 5) {
            System.out.println(" Invalid name! ");
        }

    }
}
