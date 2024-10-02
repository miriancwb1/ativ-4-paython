# Inicializa os primeiros dois números da sequência
a, b = 0, 1
contador = 0

# Loop para gerar os primeiros 10 números de Fibonacci
while contador < 10:
    print(a)          # Imprime o número atual
    a, b = b, a + b  # Atualiza os números da sequência
    contador += 1    # Incrementa o contador
