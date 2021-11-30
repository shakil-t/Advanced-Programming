/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package encrypt;

/**
 *
 * @author shakil
 */
public class InvalidCharException extends Exception {
    InvalidCharException(String msg){
        super(msg);
        System.out.println(msg);
    }
}
