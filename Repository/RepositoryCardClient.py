class RepositoryCardClient:
    def __init__(self):
        self.__storage = {}

    def create(self, cardClient):
        idCardClient = cardClient.getID()
        CNPCardClient = cardClient.getCNP()

        if idCardClient in self.__storage:
            raise KeyError('Deja exista un card client cu id-ul asta')

        for cards in self.__storage.values():
            if cards.getCNP() == CNPCardClient:
                raise KeyError('Deja exista un card client cu CNP-ul asta')

        self.__storage[idCardClient] = cardClient

    def read(self, idCardClient=None):

        if idCardClient is None:
            return self.__storage.values()
        if idCardClient in self.__storage:
            return self.__storage[idCardClient]

        return None

    def update(self, newCard):

        idNewCard = newCard.getID()
        if idNewCard not in self.__storage:
            raise KeyError('Nu exista un card client cu id-ul asta')

        self.__storage[idNewCard] = newCard

    def delete(self, idCard):

        if idCard not in self.__storage:
            raise KeyError('Nu exista un card client cu id-ul asta')
        del self.__storage[idCard]

    def clear(self):
        self.__storage.clear()
