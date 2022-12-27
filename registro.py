class MEDICAMENTO:
    def __init__(self, codigo, nombre, tipo, almacenamiento, costo):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.almacenamiento = almacenamiento
        self.costo = costo
    
    def __str__(self):
        renglon = ''
        renglon += '{:<10}'.format(self.codigo)
        renglon += ' '
        renglon += '{:<20}'.format(str(self.nombre))
        renglon += ' '
        renglon += '{:>15}'.format(self.tipo)
        renglon += ' '
        renglon += '{:>15}'.format(self.almacenamiento)
        renglon += ' '
        renglon += '{:>15}'.format(self.costo)
        return renglon


def get_titulos():
    renglon = ''
    renglon += '{:<10}'.format("Codigos")
    renglon += ' '
    renglon += '{:<20}'.format("Nombre")
    renglon += ' '
    renglon += '{:>15}'.format("Tipo")
    renglon += ' '
    renglon += '{:>15}'.format("Almacenamiento")
    renglon += ' '
    renglon += '{:>15}'.format("Costo")
    return renglon
