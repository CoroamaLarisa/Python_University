class CardClient:

    def __init__(self, ID, surname, name, CNP, dateOfBirth, dateOfRegistration, isRemoved):
        self.__ID = ID
        self.__surname = surname
        self.__name = name
        self.__CNP = CNP
        self.__dateOfBirth = dateOfBirth
        self.__dateOfRegistration = dateOfRegistration
        self.__isRemoved = isRemoved

    def getID(self):
        return self.__ID

    def getSurname(self):
        return self.__surname

    def getName(self):
        return self.__name

    def getCNP(self):
        return self.__CNP

    def getIsRemoved(self):
        return self.__isRemoved

    def getDateOfBirth(self):
        return self.__dateOfBirth

    def getDateOfRegistration(self):
        return self.__dateOfRegistration

    def __eq__(self, other):
        if not isinstance(other, CardClient):
            return False
        return self.getID() == other.getID() and self.getName() == other.getName() and self.getCNP() == other.getCNP() \
               and self.getDateOfBirth() == other.getDateOfBirth() and \
               self.getDateOfRegistration() == other.getDateOfRegistration() \
               and self.getSurname() == other.getSurname() and self.getIsRemoved() == other.getIsRemoved()

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return 'Card {}. {} - {} - {} - {} - {} - {}\n'.format(self.__ID,
                                                               self.__surname,
                                                               self.__name,
                                                               self.__CNP,
                                                               self.__dateOfBirth,
                                                               self.__dateOfRegistration,
                                                               self.__isRemoved)

    def get_text_format(self):
        return '{},{},{},{},{},{},{}'.format(self.__ID,
                                             self.__surname,
                                             self.__name,
                                             self.__CNP,
                                             self.__dateOfBirth,
                                             self.__dateOfRegistration,
                                             self.__isRemoved)
