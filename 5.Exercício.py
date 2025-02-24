import os
os.system

# Elabore um algorítimo usando operações lógicas para solicitar 
# ao usuáro 2 números e escrever:
# os 2 números informados.
# O maior número;
# O menor número;


primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o primeiro numero: "))

if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
   maior = segundo_numero
   menor = primeiro_numero 

print()
print(f"primeiro número: {primeiro_numero}")
print(f"segundo número:  {segundo_numero}")
if primeiro_numero == segundo_numero:
    print("os números são iguais.")
else:
  print(f"maior número: {maior}")
  print(f"menornúmero: {menor}")
