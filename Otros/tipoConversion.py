
class TipoConversion:
    def convertirLista(self, lista):
        valor = 0
        for i in lista:
            valor, = i
        return valor

    def convertirListaTupla(self, lista):
        nuevaLista = []
        for i in lista:
            for x in i:
                nuevaLista.append(x)
        return nuevaLista

    def convertirListaFecha(self, fecha):
        dia = fecha[0:2]
        mes = fecha[3:5]
        anio = fecha[6:10]
        return (dia, mes, anio)
