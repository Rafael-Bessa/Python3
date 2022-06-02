from validate_docbr import CPF


class VERIFICA_CPF:

    def __init__(self, cpf):
        cpf = str(cpf)
        if self.valida_cpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF INVÁLIDO")

    # consigo chamar o print lá no outro arquivo
    def __str__(self):
        return self.formata_cpf()

    @staticmethod
    def valida_cpf(documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("NÚMERO DE DÍGITOS INVÁLIDO")

    def formata_cpf(self):
        primeira_parte = self.cpf[:3]
        segunda_parte = self.cpf[3:6]
        terceira_parte = self.cpf[6:9]
        quarta_parte = self.cpf[9:]

        return (f'{primeira_parte}.{segunda_parte}.'
                f'{terceira_parte}-{quarta_parte}')
