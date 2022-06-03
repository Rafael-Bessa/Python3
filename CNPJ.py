# https://pypi.org/project/validate-docbr/

from validate_docbr import CNPJ

# cnpj = '35379838000112'
cnpj = input("Qual o número do CNPJ >>> ")

validador = CNPJ()
if validador.validate(cnpj):
    print(f"Este CNPJ existe ({cnpj})")
else:
    print("Este CNPJ \033[1:31mnão\033[m existe")

# agora vamos colocar uma máscara no cnpj


# também tem o método para fazer a máscara
print()
print("Sua forma formatada (com máscara)")
print(validador.mask(cnpj))
