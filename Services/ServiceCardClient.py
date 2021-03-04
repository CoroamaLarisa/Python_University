import datetime
import random
import string

from Repository.RepositoryCardClient import *


class ServiceCardClient:
    def __init__(self, repositoryCardClient, cardClientvalidator, datecard_repository):
        self.__repo = repositoryCardClient
        self.__validator = cardClientvalidator
        self.__datecard_repository = datecard_repository
        # self.__undo = []

    def addCardClient(self, id, surname, name, CNP, dateOfBirth, dateRegistration, point):
        """
        The functions adds a new card
        :param id: id-ul
        :param surname: numele
        :param name: prenumele
        :param CNP: CNP
        :param dateOfBirth: data nasterii
        :param dateRegistration: data inregistrarii
        :param point: puncte acumulate
        :return:
        """
        self.__validator.validateCNP(CNP, self.__repo, id)
        self.__validator.validateDate(dateOfBirth)
        self.__validator.validateDate(dateRegistration)
        card = CardClient(id, surname, name, CNP, dateOfBirth, dateRegistration, point, False)
        self.__repo.create(card)
        # self.__undo.append(lambda: self.__repo.delete(card.getID()))

    def updateCardClient(self, id, newSurname, newName, newCNP, newDateOfBirth, newDateRegistration, newPoint,
                         is_removed):
        """
        The function modifies a card
        :param is_removed: bool
        :param id: id-ul
        :param newSurname: nume
        :param newName: prenume
        :param newCNP: CNP
        :param newDateOfBirth: data nasterii
        :param newDateRegistration: data inregistrarii
        :param newPoint: puncte acumulate
        :return:
        """
        self.__validator.validateDate(newDateOfBirth)
        self.__validator.validateDate(newDateRegistration)
        self.__validator.validateCNP(newCNP, self.__repo, id)
        before_card = self.__repo.read(id)
        if is_removed:
            card = CardClient(id, newSurname, newName, newCNP, newDateOfBirth, newDateRegistration, newPoint, True)
        else:
            card = CardClient(id, newSurname, newName, newCNP, newDateOfBirth, newDateRegistration, newPoint, False)
        self.__repo.update(card)
        # self.__undo.append(lambda: self.__repo.update(before_card))

    def __id_card_exists_in_datecard(self, id_card):
        for datecard in self.__datecard_repository.read():
            if datecard.getIdCard() == id_card:
                return True
        return False

    def removeCardClient(self, id):
        '''
        Deletes a card
        :param id: int, id-ul
        :return:
        '''
        if self.__id_card_exists_in_datecard(id):
            raise ValueError("Cardul nu se poate sterge deoarece exista o rezervare cu acest film")
        else:
            card = self.__repo.read(id)
            self.__repo.delete(id)

    def getAllCards(self):
        """
        Returns all cards
        :return:
        """
        return self.__repo.read()

    def populate(self,n):
        """
        The function populates a class with random information that abides by the attribute's rules
        :return:
        """
        list_card = []
        films_added = []
        i = 0
        while i < n:
            try:

                letters = string.ascii_lowercase
                id = random.randint(1, 10100)
                surname = ''.join(random.choice(letters) for i in range(10))
                name = ''.join(random.choice(letters) for i in range(10))
                CNP = random.randint(1000000000000, 7000000000000)
                month1 = random.randint(0, 12)
                if month1 in [1, 3, 5, 7, 8, 10, 12]:
                    day1 = random.randint(1, 31)
                elif month1 == 2:
                    day1 = random.randint(1, 28)
                else:
                    day1 = random.randint(1, 30)
                year1 = random.randint(1950, 2000)
                dateOfBirth = "{}.{}.{}".format(day1, month1, year1)
                day2 = random.randint(1, 31)
                month2 = random.randint(1, 12)
                year2 = random.randint(1950, 2000)
                dateOfRegistration = "{}.{}.{}".format(day2, month2, year2)
                point = random.randint(0, 2000)
                self.__validator.validateDate(dateOfBirth)
                self.__validator.validateDate(dateOfRegistration)
                self.__validator.validateCNP(CNP, self.__repo, id)
                card = CardClient(id, surname, name, CNP, dateOfBirth, dateOfRegistration, point, False)
                self.__repo.create(card)
                i += 1
                list_card.append(card)
            except Exception as ve:
                pass
        return list_card

    def remove_populate_card(self, list_cards):
        for thing in list_cards:
            self.__repo.delete(thing.getID())

        # self.__undo.append(lambda: self.__repo.delete(id))

    def search_text(self, string_card):
        """
        Searches a string/variable in a card
        :param string_card:
        :return:
        """
        lista = []
        for card in self.__repo.read():
            if string_card in card.get_text_format():
                lista.append(card)
        return lista

    def card_client_descr_by_points(self):
        """
        Reorders the card by the number of points they have
        :return:
        """
        lista = list(sorted(self.__repo.read(), key=lambda x: x.getPoint(), reverse=True))
        return lista

    @staticmethod
    def get_datetime_format(date):
        """
        Transforms a string into a datetime format
        :param date:
        :return:
        """
        date = date.split('.')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        datetime_format = datetime.datetime(year, month, day)
        return datetime_format

    def datetime_date(self, date, date1, date2):
        if date1 > date2:
            date1, date2 = date2, date1
        zero_date = datetime.timedelta(0)
        if date2 - date >= zero_date and date - date1 >= zero_date:
            return 1
        return 0

    def increment_by_date(self, date1, date2, value, lista):

        if len(lista) > 0:

            self.__validator.validateDate(date1)
            self.__validator.validateDate(date2)
            get_date1_format = self.get_datetime_format(date1)
            get_date2_format = self.get_datetime_format(date2)
            if get_date1_format > get_date2_format:
                get_date1_format, get_date2_format = get_date2_format, get_date1_format
            zero_date = datetime.timedelta(0)
            if lista[0].get_datetime_date_of_birth() - get_date1_format >= zero_date and \
                    get_date2_format - lista[0].get_datetime_date_of_birth() >= zero_date:
                newPoint = lista[0].getPoint() + value
                self.updateCardClient(lista[0].getID(), lista[0].getSurname(), lista[0].getName(), lista[0].getCNP(),
                                      lista[0].getDateOfBirth(),
                                      lista[0].getDateRegistration(), newPoint, False)

            self.increment_by_date(date1, date2, value, lista[1:])

    def get_card(self, id):
        return self.__repo.read(id)

        # if get_date1_format > get_date2_format:
        #     get_date1_format, get_date2_format = get_date2_format, get_date1_format
        # for card in self.__repo.read():
        #     card_get_datetime = self.get_datetime_format(card.getDateOfBirth())
        #     zero_date = datetime.timedelta(0)
        #
        #     if (get_date2_format - card_get_datetime) > zero_date and \
        #             (card_get_datetime - get_date1_format) > zero_date:
        #         newPoint = card.getPoint() + value
        #         self.updateCardClient(card.getID(), card.getSurname(), card.getName(), card.getCNP(),
        #                               card.getDateOfBirth(),
        #                               card.getDateRegistration(), newPoint, False)

        #     if day1 <= date_card[0] <= day2 and month1 <= date_card[1] <= month2 and year1 <= \
        #             date_card[2] <= year2:
        #         newPoint = card.getPoint() + value
        #         self.updateCardClient(card.getID(), card.getSurname(), card.getName(), card.getCNP(),
        #                               card.getDateOfBirth(),
        #                               card.getDateRegistration(), newPoint, False)

    # def Undo(self):
    #     if len(self.__undo) > 0:
    #         undoes = self.__undo.pop()
    #         undoes()
    #     else:
    #         raise ValueError("Nu se poate face Undo")
