from Domain.CardClient import *
from Domain.DuplicateIdException import DuplicateIdException


class RepositoryCardClient:
    def __init__(self, fileName):
        self.__file = fileName
        self.__Cards = []
        self.__Cards = self.__readFile()

    def __readFile(self):
        # Functia returneaza lista de carduri
        list = []
        f = open(self.__file, "r")
        lines = f.readlines()
        for line in lines:
            cardString = line[:-1]
            components = cardString.split("/")
            id = int(components[0])
            surname = components[1]
            name = components[2]
            CNP = int(components[3])
            dateOfBirth = components[4]
            dateRegistration = components[5]
            point = int(components[6])
            card = CardClient(id, surname, name, CNP, dateOfBirth, dateRegistration, point)
            list.append(card)
        f.close()
        return list

    def __writeFile(self, listCards):
        '''
        Functia scrie toate crdurile
        :param listCards: list, lista de carduri
        :return:
        '''
        f = open(self.__file, "w")
        content = " "
        for card in listCards:
            line = "{}/{}/{}/{}/{}/{}/{}\n".format(card.getId(), card.getSurname(), card.getName(), card.getCNP(),
                                                   card.getDateOfBirth(), card.getDateRegistration(), card.getPoint())
            content += line
        f.write(content)
        f.close()

    def addCardClient(self, cardClient):
        '''
        Functia adauga un card
        :param cardClient: card
        :return:
        '''
        for card in self.__Cards:
            if card.getId() == cardClient.getId():
                raise DuplicateIdException("invalid")
        self.__Cards.append(cardClient)
        self.__writeFile(self.__Cards)

    def removeCardCient(self, cardClient):
        '''
        Functia sterge un card
        :param cardClient: card
        :return:
        '''
        self.__Cards.remove(cardClient)
        self.__writeFile(self.__Cards)

    def getCardsClients(self):
        '''
        Funtia afiseaza toate cardurile
        :return: cardurile
        '''
        return self.__Cards[:]

    def updateCardCLient(self, cardClient):
        '''
        Functia modifica un card
        :param cardClient: card
        :return:
        '''
        for index in range(0, len(self.__Cards)):
            crtCard = self.__Cards[index]
            if crtCard.getId() == cardClient.getId():
                self.__Cards[index] = cardClient
                self.__writeFile(self.__Cards)
                return
