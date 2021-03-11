class Transaction:

    def __init__(self, ID, IDCar, IDCardClient, sumPieces, sumMan, date, hour, discount):
        self.__ID = ID
        self.__IDCar = IDCar
        self.__IDCardClient = IDCardClient
        self.__sumPieces = sumPieces
        self.__sumMan = sumMan
        self.__date = date
        self.__hour = hour
        self.__discount = discount


    def getID(self):
        return self.__ID

    def getDiscount(self):
        return self.__discount

    def getIDCar(self):
        return self.__IDCar

    def getIDCardClient(self):
        return self.__IDCardClient

    def getSumPieces(self):
        return self.__sumPieces

    def getSumMan(self):
        return self.__sumMan

    def getDate(self):
        return self.__date

    def getHour(self):
        return self.__hour

    def __eq__(self, other):
        if not isinstance(other, Transaction):
            return False
        return self.getID() == other.getID() and self.getDate() == other.getDate() and self.getHour() == other.getHour() \
               and self.getIDCar() == other.getIDCar() and self.getIDCardClient() == other.getIDCardClient() and \
               self.getSumMan() == other.getSumMan() and self.getSumPieces() == other.getSumPieces() \
               and self.getDiscount() == other.getDiscount()

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return 'Transaction {}.{}.{} - {} -{} - {} - {} - {}\n'.format(self.getID(),
                                                                       self.getIDCar(),
                                                                       self.getIDCardClient(),
                                                                       self.getSumPieces(),
                                                                       self.getSumMan(),
                                                                       self.getDate(),
                                                                       self.getHour(),
                                                                       self.getDiscount()
                                                                       )
