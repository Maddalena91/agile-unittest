class Money:
    def __init__(self,numIntero):
        if type(numIntero) != int:
            if type(numIntero) == str:
                raise Exception("Sorry, le stringhe non sono accettate")
            else:
                raise TypeError("Sorry, il numero non è un intero")
        if numIntero < 0:
            raise Exception("Sorry, il numero inserito non può essere negativo")
        self.numIntero = numIntero

    def getNumber(self):
        return self.numIntero

    def isGreaterThan(self, money2):
        return self.numIntero > money2.getNumber()

    def isLessThan(self, money2):
        return self.numIntero < money2.getNumber() 

    def sum(self, money2):
        n = self.numIntero + money2.getNumber()
        return Money(n)

    def subtraction(self, money2):
        n = self.numIntero - money2.getNumber()
        if n <= 0:
            raise Exception("Sorry, il numero è negativo")
        return Money(n)