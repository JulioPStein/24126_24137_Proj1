class Matematica:
    def __init__(self, base : int):
        self._numeroBase = base

    @property
    def numBase(self):
        return self._numeroBase

    def fatorial(self, x : int) -> int:
        fatorial = 1
        if x == 0:
            return 1
        while x >= 1:
            fatorial *= x
            x -= 1
        return fatorial
    
    def triangulo_de_Pascal(self):
        import mat
        mate = mat.Matematica(self._numeroBase)
        L = self._numeroBase
        k = 0 # começa em 0
        n = 0 # //
        linhaAtual = 1
        lista = []
        while n < L:
            linha = ""
            k = 0
            while k <= n:
                
                calculo = mate.fatorial(n) / (mate.fatorial(k) * mate.fatorial(n-k))
                linha = f"{linha}{calculo:6.0f}"
                k += 1
            n += 1
            lista.append(linha)
        return lista
    