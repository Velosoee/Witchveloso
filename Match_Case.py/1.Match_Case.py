# Exemplo de estrutura condicional aninhada.
# match-case substitui o uso do if-elif-else

dia = input("digite dia da semana")
 
match dia:
   case "segunda":
      print("hoje é segunda feira")
   case "terça":
      print("hoje é terça feira")
   case "quarta":
      print("hoje é quarta feira")  
   case "quinta":
      print("hoje é quinta feira")
   case "sexta":
      print("hoje é sexta feira")
   case "sábado" | "domingo":
      print("hoje é fim de semana")

   case _: 
      print("Dia inválido.")

      print(dia)
        
      print("== FIM ==")

