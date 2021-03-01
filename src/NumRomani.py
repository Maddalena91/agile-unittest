'''
Creo la classe Numeri romani, se la stringa data in input contiene numeri romani, vengono
convertiti altrimenti il programma lancia una exception

'''

class NumRomani:
    def __init__(self,inputLetRomana):
        self.listOriginalNumConverted = []
        self.listNumConverted = []
        letterRoman = inputLetRomana.upper()
        self.romanNumAllowed = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for s in letterRoman:
            if s in self.romanNumAllowed:
                self.listOriginalNumConverted.append(self.romanNumAllowed[s])
                self.listNumConverted.append(self.romanNumAllowed[s])
            else:
                raise Exception('Sorry, il dato inserito non è un numero romano')          


    def ToInteger(self):
        somma = 0
        for n in self.listNumConverted:
            if n < self.listNumConverted[self.listNumConverted.index(n)+1]:
                print(f'{somma} = {somma} + ({self.listNumConverted[self.listNumConverted.index(n)+1]} - {n})')
                somma = somma + (self.listNumConverted[self.listNumConverted.index(n)+1] - n)
                print(f'totale = {somma}')
                self.listNumConverted.remove(self.listNumConverted[self.listNumConverted.index(n)+1])
            else:
                print(f'{somma} = {somma} + {n}')
                somma = somma + n
                print(f'totale = {somma}')
        print(self.listOriginalNumConverted)
        return(somma)


str1  = NumRomani("MCMXLIV")