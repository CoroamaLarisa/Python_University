import datetime


class CardClient:
    def __init__(self, id, surname, name, CNP, dateOfBirth, dateRegistration, points, is_removed):
        self.__id = id
        self.__surname = surname
        self.__name = name
        self.__CNP = CNP
        self.__dateOfBirth = dateOfBirth
        self.__dateRegistration = dateRegistration
        self.__points = points
        self.__is_removed = is_removed

    def getID(self):
        return self.__id

    def getIsRemoved(self):
        return self.__is_removed

    def getSurname(self):
        return self.__surname

    def getName(self):
        return self.__name

    def getCNP(self):
        return self.__CNP

    def getDateOfBirth(self):
        return self.__dateOfBirth

    def getDateRegistration(self):
        return self.__dateRegistration

    def getPoint(self):
        return self.__points

    def getIntBirthdayDate(self):
        date = self.getDateOfBirth().split('.')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        return [day, month, year]

    def get_datetime_date_of_birth(self):
        """
        Transforms a string into a datetime format
        :param date:
        :return:
        """
        date = self.__dateOfBirth.split('.')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        datetime_format = datetime.datetime(year, month, day)
        return datetime_format

    def get_datetime_date_registration(self):
        """
        Transforms a string into a datetime format
        :param date:
        :return:
        """
        date = self.__dateRegistration.split('.')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        datetime_format = datetime.datetime(year, month, day)
        return datetime_format


    def __eq__(self, other):
        if not isinstance(other, CardClient):
            return False
        return self.getID() == other.getID() and self.getSurname() == other.getSurname() and \
            self.getName() == other.getName() and self.getCNP() == other.getCNP() and \
            self.getDateOfBirth() == other.getDateOfBirth() and \
            self.getDateRegistration() == other.getDateRegistration() and \
            self.getPoint() == other.getPoint() and self.getIsRemoved() == other.getIsRemoved()

    def __ne__(self, other):
        return not self == other

    # return self.storage.values()
    def __str__(self):
        return 'CardClient {}. {} - {} - {} -{} - {} - {}-{}\n'.format(self.__id,
                                                                       self.__surname,
                                                                       self.__name,
                                                                       self.__CNP,
                                                                       self.__dateOfBirth,
                                                                       self.__dateRegistration,
                                                                       self.__points,
                                                                       self.__is_removed)

    def get_text_format(self):
        return "{},{},{},{},{},{},{}".format(self.getID(),
                                             self.getSurname(),
                                             self.getName(),
                                             self.getCNP(),
                                             self.getDateOfBirth(),
                                             self.getDateRegistration(),
                                             self.getPoint(),
                                             self.getIsRemoved())
