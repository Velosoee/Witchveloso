import os 
os.system("clear")  

# elabore  um algorítimo para solicitar ao usuário o login e a senha.
# considere que os dados do usuário já estãocadastrados
# caso o login e senha estejam correto, mostre a mensagem:
# "Bem-vindo!"
# Caso contrário,mostre a mensagem: 
# "Login ou senha inválidos."

login_cadastrado = "marta"
senha_cadastrada = "123"

login = input("digite o login")
senha = input("digite a senha")

if login == login_cadastrada and senha == senha_cadastrada:
  print("Bem-vindo")
else: 
  print("Longin ou senha inválidos")

