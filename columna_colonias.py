Dixon = {
    3: 0.97021,
    4: 0.82973,
    5: 0.71028
}

class Columna_colonias:
    """Esta clase recibe una lista con los elementos
    de su columna"""

    def __init__(self, vals_s, vals, col):
        self.orig = vals_s
        for i in self.orig:
            try:
                self.orig[self.orig.index(i)] = int(i)
            except Exception:
                pass

        self.vals = vals
        for i in self.vals:
            try:
                self.vals[self.vals.index(i)] = int(i)
            except Exception:
                pass
        self.col = col

        while '' in self.vals:
            self.vals.remove('')


        self.vals.sort()

    def rechazo(self):
        """Esta función hace una prueba de Dixon de dos colas,
        si no hay suficientes repeticiones se regresa False
        primero calcula el valor Q del extremo mínimo y el maximo
        tras ello se compara con los valores Q de tabla
        si se valida la hipótesis nula, se regresa False
        si se valida la hipótesis aternativa, regresa un string para
        ser instado en una caja de alerta"""
        if len(self.vals) < 3:
            return False
        else:
            q_a = abs(self.vals[0] - self.vals[1]) / (self.vals[-1] - self.vals[0])
            q_b = (self.vals[-1] - self.vals[-2]) / (self.vals[-1] - self.vals[0])

            if q_a > Dixon.get(len(self.vals)):
                return f'Considere descartar el valor {self.col}{self.orig.index(self.vals[0])+1}\nPrueba Q de Dixon con 95% de confianza'
            elif q_b > Dixon.get(len(self.vals)):
                return f'Considere descartar el valor {self.col}{self.orig.index(self.vals[-1])+1}\nPrueba Q de Dixon con 95% de confianza'
            else:
                return False

    @property
    def depured(self):
        return self.vals


