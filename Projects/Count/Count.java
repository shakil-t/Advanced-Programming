/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package count;

/**
 *
 * @author shakil
 */
import java.io.*;
import java.util.*;
public class Count {

    /**
     * @param args the command line arguments
     */
    public static void Count(String name1 , String name2){
        String[] array1=new String[6];
        int counter=0;
        int[] array2=new int[6];
        switch(counter){
            case 0:
              array1[0]=name1;
              counter++;
              Comparison(name1,name2,array2[counter-1]);
            default :
                for(int j=0;j<counter;j++){
                    if(array1[j]==name1){
                        name1=name2;
                    }else{
                        array1[counter]=name1;
                       Comparison(name1,name2,array2[counter]);
                       name1=name2;
                    }
                }
        }
        for(int l=0;l<6;l++){
            System.out.print(array1[l]+":");
            System.out.print(array2[l]);
            System.out.println();
        }
        }
    public static void Comparison(String name2, String name3, int counter){
        if(name2==name3){
            counter++;
            name2=name3;
        }else{
            name2=name3;
        }
    }
    public static void main(String[] args) 
// This code was developed partially in collaboration with a student; however it has a few bugs
            throws FileNotFoundException {
        Scanner input=new Scanner(new File("C:/Users/shakil/count.txt"));
        while(input.hasNextLine()){
            String name1 = input.nextLine();
            Scanner nameScan=new Scanner(name1);
            String name2 = nameScan.next();
            String name3 = nameScan.next();
            Count(name2, name3);
        }  
}
}
