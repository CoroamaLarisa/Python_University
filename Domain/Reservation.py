import datetime


class Reservation:
    def __init__(self, id, idFilm, idCard, date, hour, is_removed=False):
        self.__id = id
        self.__idFilm = idFilm
        self.__idCard = idCard
        self.__date = date
        self.__hour = hour
        self.__is_removed = is_removed

    def getID(self):
        return self.__id

    def getIsRemoved(self):
        return self.__is_removed

    def getIdFilm(self):
        return self.__idFilm

    def getIdCard(self):
        return self.__idCard

    def getDate(self):
        return self.__date

    def getHour(self):
        return self.__hour

    # def getIsRemoved(self):
    #     return self.__is_removed

    def getIntHour(self):
        hour = self.getHour().split(':')
        hours = int(hour[0])
        minutes = int(hour[1])
        return [hours, minutes]

    def getIntDate(self):
        date = self.getDate().split('.')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        return [day, month, year]

    def get_datetime_date(self):
        """
        Transforms a string into a datetime format
        :param date:
        :return:
        """
        date = self.__date.split('.')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        datetime_format = datetime.datetime(year, month, day)
        return datetime_format

    def __eq__(self, other):
        if not isinstance(other, Reservation):
            return False
        return self.getID() == other.getID() and self.getIdFilm() == other.getIdFilm() and \
               self.getIdCard() == other.getIdCard() and \
               self.getDate() == other.getDate() and self.getHour() == other.getHour()

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return 'Reservation {}. {} - {} - {} -{}\n'.format(self.__id,
                                                           self.__idFilm,
                                                           self.__idCard,
                                                           self.__date,
                                                           self.__hour)

    def get_text_format(self):
        return "{},{},{},{},{}".format(self.getID(),
                                       self.getIdFilm(),
                                       self.getIdCard(),
                                       self.getDate(),
                                       self.getHour())

