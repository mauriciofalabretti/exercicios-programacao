/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package exercicio01;

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 *
 * @author Mauricio
 */
public class Exercicio01 {
    
    //Função para somar dois valores
    public static int soma(int n1, int n2) {
        int s = n1 + n2;
        return s;
    }

    //Função para validar a entrada de inteiros
    public static int validaInt(Scanner teclado, String mensagem){
        while(true){
            try{
                System.out.print(mensagem);
                int n = teclado.nextInt();
                return n;
            } catch(InputMismatchException e){
                teclado.nextLine(); //Limpa o buffer do teclado
                System.out.println("Valor deve ser um número inteiro!" + e);
            }
        }
    }
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner teclado = new Scanner(System.in);
        
        int v1 = validaInt(teclado, "Digite o primeiro valor: ");
        int v2 = validaInt(teclado, "Digite o segundo valor: ");
         
        int resultado = soma(v1, v2);
        System.out.println("O resultado da soma entre " + v1 + " e " + v2 + " é: " + resultado);
        
        teclado.close();
    }
    
}
