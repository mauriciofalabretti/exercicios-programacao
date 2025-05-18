/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package desafio01poo2;

import java.util.InputMismatchException;
import java.util.NoSuchElementException;
import java.util.Scanner;

/**
 *
 * @author Mauricio
 */
public class Desafio01POO2 {
    //Função para tratamento de erros
    public static int validaEntrada(Scanner teclado, String mensagem){
        while(true){
            try{
                System.out.print(mensagem);
                String input = teclado.nextLine();
                if (input.isEmpty() == true){
                    throw new NoSuchElementException("Campo vazio!");
                } else{
                    int numero = Integer.parseInt(input);
                    return numero;
                }
            } catch(InputMismatchException e){
                teclado.nextLine(); //Limpa buffer do Scanner
                System.out.println("Valor deve ser um número inteiro! Tente novamente!");
            } catch(NoSuchElementException e){
                teclado.nextLine(); 
                System.out.println("Digite um valor! " + e);
            }
        }
    }
    //Função para validar uma divisão
    public static float divisaoValida(int dividendo, int divisor){
        while(true){
            try{
                if (divisor == 0) {
                    throw new ArithmeticException("Divisão inválida!");
                } else{
                    float divisao = (float) dividendo / divisor;
                    return divisao;
                }
            } catch(ArithmeticException e){
                System.out.println("O divisor deve ser maior que zero!");
                return Float.NaN;
            } 
        }
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner teclado = new Scanner(System.in);
        
        //Entrada de dados
        int n1 = validaEntrada(teclado, "Digite o primeiro número: ");
        int n2 = validaEntrada(teclado, "Digite o segundo número: ");
        
        //Processamento de dados
        float divisao = divisaoValida(n1, n2); 
        
        //Saída de dados
        System.out.printf("O resultado da divisão é %.2f\n", divisao);
         
    }
    
}
