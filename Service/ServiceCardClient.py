import random
import string

from Domain.CardClient import CardClient
from Service.DuplicateCNPException import DuplicateCNPException


class ServiceCardClient:
    def __init__(self, repository, cardValidator):
        self.__repository = repository
        self.__validator = cardValidator

    def addCard(self, ID, surname, name, CNP, dateOfBirth, dateOfRegistration, isRemoved):
        """
        Functia adauga un card
        :param ID: id-ul cardului
        :param surname: numele clientului cardului
        :param name: prenumele clientului cardului
        :param CNP: CNP-ul  clinetului cardului
        :param dateOfBirth: Data de nastere a clientului
        :param dateOfRegistration: Data de inregistrare a clientului
        :param isRemoved: daca cardul este sters sau nu
        :return:
        """
        card = CardClient(ID, surname, name, CNP, dateOfBirth, dateOfRegistration, isRemoved)

        self.__validator.validate(card, self.__repository)
        self.__repository.create(card)

    def removeCard(self, idCard):
        """
        Functia sterse un card cu id-ul dat
        :param idCard: id-ul cardului
        :return:
        """
        self.__repository.delete(idCard)

    def updateCard(self, ID, surname, name, CNP, dateOfBirth, dateOfRegistration, isRemoved):
        """
        Functia modifica cardul cu id-ul dat prin parametrii dati
        :param ID: id-ul cardului
        :param surname: numele clientului cardului
        :param name: prenumele clientului cardului
        :param CNP: CNP-ul  clinetului cardului
        :param dateOfBirth: Data de nastere a clientului
        :param dateOfRegistration: Data de inregistrare a clientului
        :param isRemoved: daca cardul este sters sau nu
        :return:
        """
        newCard = CardClient(ID, surname, name, CNP, dateOfBirth, dateOfRegistration, isRemoved)
        self.__validator.validate(newCard, self.__repository)
        self.__repository.update(newCard)

    def getAll(self):
        return self.__repository.read()

    def search_text(self, string_cards):
        """
        Functia cauta un card printr-un string
        :param string_cards: string-ul prin care se cauta
        :return:
        """
        lista = []

        for cards in self.__repository.read():
            if string_cards in cards.get_text_format():
                lista.append(cards)

        return lista

    def populate(self, n):
        """
        Functia populeaza entitatea CardClient cu valori random
        :return:
        """
        cards_list = []
        i = 0
        while i < n:
            try:
                letters = string.ascii_lowercase
                id = random.randint(1, 10001)
                surname = ''.join(random.choice(letters) for i in range(10))
                name = ''.join(random.choice(letters) for i in range(10))
                CNP = random.randint(1000000000000, 7000000000000)
                day1 = random.randint(0, 31)
                month1 = random.randint(0, 12)
                year1 = random.randint(1950, 2000)
                dateOfBirth = "{}.{}.{}".format(day1, month1, year1)
                day2 = random.randint(0, 31)
                month2 = random.randint(0, 12)
                year2 = random.randint(1950, 2000)
                dateOfRegistration = "{}.{}.{}".format(day2, month2, year2)
                self.addCard(id, surname, name, CNP, dateOfBirth, dateOfRegistration, False)
                card = CardClient(id, surname, name, CNP, dateOfBirth, dateOfRegistration, False)
                cards_list.append(card)
                i += 1
            except Exception as e:
                pass
        return cards_list

    def remove_populate(self, list_cards):
        for card in list_cards:
            self.__repository.delete(card.getID())

    def clear(self):
        self.__repository.clear()

    def get_card(self, id):
        return self.__repository.read(id)
