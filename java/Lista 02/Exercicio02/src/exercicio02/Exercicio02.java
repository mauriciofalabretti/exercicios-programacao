/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package exercicio02;

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 *
 * @author Mauricio
 */
public class Exercicio02 {
    
    //Função para validar a entrada de valores numéricos
    public static float validaNum(Scanner teclado, String mensagem){
        while(true){
            try{
                System.out.print(mensagem);
                float n = teclado.nextFloat();
                return n;
            } catch(InputMismatchException e){
                teclado.nextLine();
                System.out.println("O valor deve ser numérico! Tente novamente!");
            }
        }
    }
    
    //Função para somar
    public static float somar(float n1, float n2){
        float soma = n1 + n2;
        return soma;
    }

    //Função para dividir
    public static float dividir(float dividendo, float divisor){
        float divisao = dividendo/divisor; 
        return divisao;
    }
    
    //Função para subtrair
    public static float subtrair(float minuendo, float subtraendo){
        float subtracao = minuendo - subtraendo;
        return subtracao;
    }
    
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner teclado = new Scanner(System.in);
        
        float v1 = validaNum(teclado, "Primeiro valor: ");
        float v2 = validaNum(teclado, "Segundo valor: ");
        float v3 = validaNum(teclado, "Terceiro valor: ");
        float v4 = validaNum(teclado, "Quarto valor: ");
        
        float calc_1 = somar(v1, v2);
        float calc_2 = dividir(calc_1, v3);
        float calc_3 = subtrair(calc_2, v4);
        
        System.out.printf("\nO resultado ao final dos cálculos é %.2f\n", calc_3);
        
        teclado.close();
    }
    
}
