# Inicializa o número e o fatorial
numero = 5  # Você pode mudar este valor para calcular o fatorial de outro número
fatorial = 1
contador = numero

# Loop enquanto o contador for maior que 0
while contador > 0:
    fatorial *= contador  # Multiplica o fatorial pelo contador
    contador -= 1         # Decrementa o contador

print(fatorial)  # Imprime o fatorial
