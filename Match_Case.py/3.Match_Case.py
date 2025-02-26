import os
os.system("clear")


# Faça um algorítimo que mostre o menu com opções de um cardápio de restaurante
# para pessoa.
# A pessoa vai escolher o prato desejado digitando o código do prato[
# Após escolher o prato, o açlgoítimo deve mostrar o nome e o valor do prato escolhido,

# Entrada
opcao = int(input("""
código \t Prato \t\t\t valor
1 \t Picanha \t\t R$ 25,00
2 \t Lasanha \t\t R$ 20,00
3 \t Strogonoff \t\t R$ 18,00
4 \t Bife acebolado \t R$ 15,00
5 \t Pão com Ovo \t\t R$ 5,00

digite a opção desejada:
"""))

# Processamento
match opcao:
    case 1:
     print("Picanha - R$ 25,00 ")
    case 2:
      print("Lasanha - R$ 20,00 ")
    case 3:
      print("Strogonoff - R$ 18,00 ")
    case 4:
      print("Bife acebolado - R$ 15,00 ")
    case 5:
      print("Pão com Ovo - R$ 5,00 ")
    case _:
      resultado = "Opção inválida."

    

