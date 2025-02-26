import os
os.system ("clear")

# Escreva um programa utilizando o comando match-case que imprima um mês do ano
# de acordo com o número digitado pelo usuário.

# Entrada

mês = input ("digite um número para o mês do ano: ")
 
 # Processamento
match mês:
   
   case 1:
      print("Janeiro")
   case 2:
      print("Fevereiro")
   case 3:
      print("Março")
   case 4:
      print("Abril")
   case 5:
      print("Maio")
   case 6:
      print("Junho")
   case 7:
      print("Julho")
   case 8:
      print("Agosto")
   case 9:
      print("Setembro")
   case 10:
      print("Outubro")
   case 11:
      print("Novembro")
   case 12:
      print("Dezembro")
   case _:  
    resultado = "Opção inválida."