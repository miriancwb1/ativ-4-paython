# Inicializa o número e a soma
numero = 1234  # Você pode mudar este valor
soma = 0

# Loop enquanto o número for maior que 0
while numero > 0:
    soma += numero % 10  # Adiciona o último dígito à soma
    numero //= 10        # Remove o último dígito

print(soma)  # Imprime a soma dos dígitos
