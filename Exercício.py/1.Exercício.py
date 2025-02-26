# Limpar o terminal
import os 
os.system("clear")

# Elabore um algoritimo para solicirar ao usuario um valor e
# escreva a linguagem: 
# "É MAIOR QUE 10!".
# e se o valor lido não for maior que 10, caso contrário escrever:
# "NÃO É MAIOR QUE 10!".

numero = int (input ("digite um número: "))
if numero > 10: 
  print("É MENOR QUE 10!")      
else: 
 print ("É MAIOR QUE 10!")
