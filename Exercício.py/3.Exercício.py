import os 
os.system("clear")

# Elabore um algorítimo para solicitar ao usuário três notas

Primeira_nota = float(input("Digite a primeira nota: "))
Segunda_nota = float(input("Digite a primeira nota: "))
Terceira_nota = float(input("Digite a primeira nota: "))

soma =Primeira_nota + Segunda_nota + Terceira_nota
media =  soma / 3 

print(f"Média: {media}")

if media < 7: 
   print("Reprovado!")
else: 
    print("Aprovado!") 

