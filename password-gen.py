import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.whitespace
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha

print("--- Gerador de Senhas ---")
tamanho = int(input("Digite o tamanho da senha: "))
print("Sua senha gerada é:", gerar_senha(tamanho))
