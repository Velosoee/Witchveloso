import os 
os.system("clear")


# Elabore um algorítimo para solicitar dois números ao final mostre na tela:
# "Média, a soma, o produto, o menor e o maior valor
# Usando uma linha para cada reultado

primeiro_numero = float(input("digite a primeira nota:"))
segundo_numero = float(input("digite a segunda nota: "))

media = (primeiro_numero + segundo_numero) / 2
produto = primeiro_numero + segundo_numero

#media = (primeiro_numero + segudo numero) /2


if primeiro_numero < segundo_numero:
     menor = primeiro_numero
     maior = segundo_numero
else:
     menor = segundo_numero
     maior = primeiro_numero


print("\nexibindo resultados: ")
print(f"Média: {media}")
print(f"Produto: {produto}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")