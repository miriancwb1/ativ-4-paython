# Inicializa o número
numero = 12345  # Você pode mudar este valor
contador = 0

# Loop enquanto o número for maior que 0
while numero > 0:
    numero //= 10  # Remove o último dígito
    contador += 1  # Incrementa o contador

print(contador)  # Imprime a contagem de dígitos
