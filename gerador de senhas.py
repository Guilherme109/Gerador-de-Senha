import random

# Defina a função para gerar uma senha aleatória
def gerar_senha():
  # Define o conjunto de caracteres possíveis
  caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

  # Gera uma senha aleatória com 16 caracteres
  senha = "".join(random.choice(caracteres) for i in range(16))

  return senha

# Gere uma senha aleatória
senha = gerar_senha()

# Exiba a senha
print("Sua senha aleatória é:", senha)
