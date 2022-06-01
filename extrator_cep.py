# Aprendendo a usar Expressões regulares
import re

endereco = "Rua José Pinheiro, 145, Jardim Piratininga, São Paulo, 03716-070"

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789]"
                    "[0123456789][0123456789]")

busca = padrao.search(endereco)  # se tiver , ele retorna match, caso contrario retorna None
cep = busca.group()
print(cep)
