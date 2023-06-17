
class MMC:

    def __init__(self, lista_numeros: list):
        self.__numeros = MMC.__processo_ternary_op(type(lista_numeros) if not isinstance(lista_numeros, list) else lista_numeros)
        self.__numeros = tuple([MMC.__validacao_numeros(x) for x in self.__numeros])
        self.valores = list()
        self.fatorar()
        

    @staticmethod
    def __processo_ternary_op(item) -> TypeError:
        if not isinstance(item, list):
            raise TypeError(f"O objeto informado deve ser um objeto iterável do tipo |list|, não |{type(item).__name__}|")
        else:
            return item


    @staticmethod
    def __validacao_numeros(item) -> TypeError:
        if not isinstance(item, int):
            raise TypeError(f"Os dados do iterável devem ser objetos do tipo |int|, não |{type(item).__name__}|")
        else:
            return item
        

    @staticmethod
    def __calcular_mdc(v1, v2):
        while v2 != 0:
            v1, v2 = v2, v1 % v2
        return v1


    def fatorar(self):
        qtd = len(self.__numeros)
        if qtd < 2:
            raise ValueError(f"É necessário fornecer pelo menos dois valores. Informado: {qtd} ")

        mmc = self.__numeros[0]
        for i in range(len(self.__numeros)):
            mmc = (mmc * self.__numeros[i]) // MMC.__calcular_mdc(mmc, self.__numeros[i])
        self.valores.append(mmc)
        

    
if __name__ == "__main__":
    for x in [[90,80],[180,140],[90,80,200]]:
        calculo = MMC(x)
        print(calculo.valores)
  
