from typing import Any

preco=float(input('Qual o preço do produto na loja?'))
novo= preco - (preco * 10 / 100)
print(f'O preço promocional de nosso produto é de R$ {novo:.2f}, com o valor promocional de 10%')