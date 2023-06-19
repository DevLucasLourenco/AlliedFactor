class MMC:

    def __init__(self):
        self.__numeros = ...
        self.valores = list()
        self.flag = False


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
    def __calcular_mdc(v1, v2) -> int:
        while v2 != 0:
            v1, v2 = v2, v1 % v2
        return v1


    def get(self, lista_numeros: list):
        self.__numeros = MMC.__processo_ternary_op(type(lista_numeros) if not isinstance(lista_numeros, list) else lista_numeros)
        self.__numeros = tuple([MMC.__validacao_numeros(x) for x in self.__numeros])

        self.flag = True


    def run(self):
        if self.flag:
            qtd = len(self.__numeros)
            if qtd < 2:
                raise ValueError(f"É necessário fornecer pelo menos dois valores. Informado: {qtd} ")

            mmc = self.__numeros[0]
            for i in range(len(self.__numeros)):
                mmc = (mmc * self.__numeros[i]) // MMC.__calcular_mdc(mmc, self.__numeros[i])
            self.valores.append(mmc)
        
        else:
            raise RuntimeError(f"Tentiva de encontrar valores informados inválida. Passe os valores correspondentes.")
        

    def clear(self) -> list.clear:
        self.valores.clear()

    
    
if __name__ == "__main__":
    instancia = MMC()


    # exemplo1
    instancia.get([90,80])
    instancia.run()
    print(instancia.valores)


    # limpar lista de resultados
    instancia.clear()


    # exemplo2
    for x in [[180,140], [90,80,200], [30,40,50]]:
        instancia.get(x)
        instancia.run()
        
    print(instancia.valores)
