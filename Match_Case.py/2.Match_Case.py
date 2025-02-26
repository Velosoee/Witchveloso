# Limpar terminal.
import os 
os.system("clear")

# Faça um algorítimo que solicite dois número
# e um caractere que calcula as operções básicas (+ - * /).
# Mostre os números informaddos pelo usuário,
# o operador escolhido e o resultado.

# Entrada 
primeiro_numero = int(input("Digite um número: "))
operador = input("Digite a operação que deseja (+ - * /): ")
segundo_numero = int(input("Digite um número): "))

# Processamento 
match operador: 
  case "+":
     resultado = primeiro_numero + segundo_numero
  case "-":
     resultado = primeiro_numero + segundo_numero
  case "*":
     resultado = primeiro_numero + segundo_numero
  case "/":
     resultado = primeiro_numero + segundo_numero
  case _:
     resultado = "Opção inválida."

   # Saída  
     print(f"\Primeiro numero: {primeiro_numero}")
     print(f"operação: {operador}")
     print(f"segundo numero: {segundo_numero}")
     print(f"Resultado: {resultado}")
