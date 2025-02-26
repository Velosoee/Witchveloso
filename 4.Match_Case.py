import os
os.system("clear")

# Desenvolva um programa que receba como entrada um número inteiro
# que represente um dos 7 dias da semana e imprima na tela se esse 
# dia útil, final de semana ou inválido.
# Considere que Domingo é o dia 1 e Sábado o dia 7.

# Entrada

dia = input("digite um número para o dia da semana: ")
 
 # Processamento
match dia:
   case 1:
      print("Domingo")
   case 2:
      print("Segunda Feira")
   case 3:
      print("Terça Feira")
   case 4:
      print("Quarta Feira ")
   case 5:
      print("Quinta Feira")
   case 6:
      print("Sexta Feira")
   case 7:
      print("Sábado")
   case _:
      resultado = "Opção inválida."