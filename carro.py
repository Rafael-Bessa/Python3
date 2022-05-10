"""Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

- Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
- O consumo é especificado no construtor e o nível de combustível inicial é 0.
- Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
- Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
- Forneça um método adicionarGasolina( ), para abastecer o tanque"""


class Carro:

    def __init__(self,consumo):
        print("Verificando Construtor, construindo objeto")
        self.consumo = consumo
        self.nivel = 0

    def andar(self,distancia):
        km = 0
        litros_usados = distancia/self.consumo
        if(self.nivel >= litros_usados):
            self.nivel -= litros_usados
            km = distancia
            print(f"Você andou {km} km")
        else:
            print("Você não tem gasolina para andar a distância que deseja")

    def obterGasolina(self):
         print(f"Você tem {self.nivel} litros de gasolina no tanque")

    def adicionarGasolina(self,litros):
        self.nivel += litros
