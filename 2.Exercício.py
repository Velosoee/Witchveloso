# Limpar o terminal.
import os
os.system("clear")

# Elabore um algoritimo para solicitar ao usuario um valor e escreva a linguagem: 
"É MAIOR QUE 10!"
# e se o valor lido não for maior que 10, caso contrário escrever:
# "NÃO É MAIOR QUE 10!".
# se o número digitado for igual a 10, escereva a linguagem:
"É IGUAL A 10!"

numero = int(input("digite um número"))

if numero == 10:
   print("É IGUAL A 10!")
elif numero >10: 
   print("É MAIOR QUE 10!")
else: 
   print("NÃO É MAIOR QUE 10!")
