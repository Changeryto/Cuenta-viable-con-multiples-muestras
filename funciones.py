

class Calc_promed:
    def __init__(self, lol, alic=0.1, mayor_dil=1E-4):
        self.lol = lol
        self.alic = alic
        self.mayor_dil = mayor_dil
        for i in range(0, 5):
            while '' in self.lol[i]:
                self.lol[i].remove('')
        self.cumcol = 0
        self.nd = ''

    def promed(self):
        """Esta función va a recibir una lista de listas
        va a registrar el número de items válidos en cada lista
        y va a regresar el promedio ponderado de colonias"""
        self.cumcol = 0
        self.nd = ''

        for i in range(0, 5):
            self.nd += str(len(self.lol[i]))
            #print(self.nd)
            for j in range(len(self.lol[i])):
                self.cumcol += int(self.lol[i][j])

        return self.cumcol / (int(self.nd)/10000)

    def calc_ufc(self):
        """Esta función recibe el promedio de colonias,
        la alícuota de transferencia y la dilución mayor (unidad)
        y regresa la cantidad de UFC/mL o g"""
        ufc = self.promed() * (1/self.alic) * (1/self.mayor_dil)
        return "{:.2E}".format(ufc)

    @property
    def denominador(self):
        self.nd = ''
        for i in range(0, 5):
            self.nd += str(len(self.lol[i]))

        return str((int(self.nd)/10000))
        #return 'aaaa'

    @property
    def numerador(self):
        ret = ''
        for i in self.lol:
            for j in i:
                ret += f'{j} + '
        #print(ret[0:-3])
        return ret[0:-3]

    @property
    def tot_col(self):
        ret = 0
        for i in self.lol:
            for j in i:
                ret += j
        return ret


"""
if __name__ == '__main__':
    lol = [[1,2,3,'',''], [4,5,6,'',''], [7,8,9,'',''], ['','','','',''], ['','','','','']]
    print(cal_prom(lol))

    lol2 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    print(cal_prom(lol2))
"""