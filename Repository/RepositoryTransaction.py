class RepositoryTransaction:
    def __init__(self):
        self.__storage = {}

    def create(self, transaction):
        idTransaction = transaction.getID()
        if idTransaction in self.__storage:
            raise KeyError('Deja exista o tranzactie cu id-ul asta')

        self.__storage[idTransaction] = transaction

    def read(self, idTransaction=None):

        if idTransaction is None:
            return self.__storage.values()
        if idTransaction in self.__storage:
            return self.__storage[idTransaction]

        return None

    def update(self, newTransaction):

        idNewTransaction = newTransaction.getID()
        if idNewTransaction not in self.__storage:
            raise KeyError('Nu exista o tranzactie cu id-ul asta')

        self.__storage[idNewTransaction] = newTransaction

    def delete(self, idTransaction):
        if idTransaction not in self.__storage:
            raise KeyError('Nu exista o tranzactie cu id-ul asta')

        del self.__storage[idTransaction]

    def clear(self):
        self.__storage.clear()
