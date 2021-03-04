import pickle

from Domain.CardClient import CardClient
from Repository.RepositoryError import RepositoryError


class GenericFileRepository:

    def __init__(self, fileName):
        self.__storage = {}
        self.__fileName = fileName

    def __loadFromFile(self):

        try:
            with open(self.__fileName, 'rb') as f_read:
                self.__storage = pickle.load(f_read)
        except FileNotFoundError:
            self.__storage.clear()
        except Exception:
            self.__storage.clear()

    def __saveToFile(self):

        with open(self.__fileName, 'wb') as f_write:
            pickle.dump(self.__storage, f_write)

    def create(self, entity):
        self.__loadFromFile()

        idEntity = entity.getID()
        if idEntity in self.__storage:
            raise RepositoryError('Entitatea cu id-ul acesta deja exista')

        self.__storage[idEntity] = entity
        self.__saveToFile()

    def read(self, idEntity=None):
        self.__loadFromFile()
        if idEntity is None:
            return self.__storage.values()

        if idEntity in self.__storage:
            return self.__storage[idEntity]

        return None

    def update(self, entity):
        self.__loadFromFile()
        idEntity = entity.getID()

        if idEntity not in self.__storage:
            raise RepositoryError('Nu este o entitate cu id-ul asta')

        self.__storage[idEntity] = entity
        self.__saveToFile()

    def delete(self, idEntity):
        self.__loadFromFile()

        if idEntity not in self.__storage:
            raise RepositoryError('Nu exista o entitate cu id-ul asta')

        del self.__storage[idEntity]
        self.__saveToFile()
