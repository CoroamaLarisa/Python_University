class Film:
    def __init__(self, id, title, year, price, inProgram, is_removed):
        self.__id = id
        self.__title = title
        self.__year = year
        self.__price = price
        self.__inProgram = inProgram
        self.__is_removed = is_removed

    def getID(self):
        return self.__id

    def getIsRemoved(self):
        return self.__is_removed

    def getTitle(self):
        return self.__title

    def getYear(self):
        return self.__year

    def getPrice(self):
        return self.__price

    def getInProgram(self):
        return self.__inProgram

    def setId(self, newId):
        self.__id = newId

    def setTitle(self, newTitle):
        self.__title = newTitle

    def setYear(self, newYear):
        self.__year = newYear

    def setPrice(self, newPrice):
        self.__price = newPrice

    def setInProgram(self, newInProgram):
        self.__inProgram = newInProgram

    def __eq__(self, other):
        if not isinstance(other, Film):
            return False
        return self.getID() == other.getID() and self.getTitle() == other.getTitle() and \
            self.getYear() == other.getYear() and self.getPrice() == other.getPrice() and \
            self.getInProgram() == other.getInProgram() and self.getIsRemoved() == other.getIsRemoved()

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return 'Film {}. {} - {} - {} -{}-{}\n'.format(self.__id,
                                                       self.__title,
                                                       self.__year,
                                                       self.__price,
                                                       self.__inProgram,
                                                       self.__is_removed)

    def get_text_format(self):
        return "{},{},{},{},{},{}".format(self.getID(),
                                          self.getTitle(),
                                          self.getYear(),
                                          self.getPrice(),
                                          self.getInProgram(),
                                          self.getIsRemoved())
