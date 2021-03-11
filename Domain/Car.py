class Car:

    def __init__(self, ID, model, yearPurchase, noKm, inGuarantee, isRemoved):
        self.__ID = ID
        self.__model = model
        self.__yearPurchase = yearPurchase
        self.__noKm = noKm
        self.__inGuarantee = inGuarantee
        self.__isRemoved = isRemoved

    def getID(self):
        return self.__ID

    def getIsRemoved(self):
        return self.__isRemoved

    def getModel(self):
        return self.__model

    def getYearPurchase(self):
        return self.__yearPurchase

    def getNoKm(self):
        return self.__noKm

    def getInGuarantee(self):
        return self.__inGuarantee

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False

        return self.getID() == other.getID() and self.getModel() == other.getModel() and \
               self.getYearPurchase() == other.getYearPurchase() and self.getNoKm() == other.getNoKm() \
               and self.getInGuarantee() == other.getInGuarantee() and self.getIsRemoved() == other.getIsRemoved()

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return 'Car {}. {} - {} - {} - {} - {}\n'.format(self.__ID,
                                                         self.__model,
                                                         self.__yearPurchase,
                                                         self.__noKm,
                                                         self.__inGuarantee,
                                                         self.__isRemoved)

    def get_text_format(self):
        return '{},{},{},{},{},{}'.format(self.__ID,
                                          self.__model,
                                          self.__yearPurchase,
                                          self.__noKm,
                                          self.__inGuarantee,
                                          self.__isRemoved)
