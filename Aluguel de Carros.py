dias = int(input('Quantos dias o carro está alugado?'))
Km = float(input('Quantos quilômetros foram percorridos?'))
pago=(dias*60)+(Km*0.15)
print(f'O total a pagar é R${pago:.2f}')
