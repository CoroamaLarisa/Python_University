import json

from Domain.DuplicateIdException import DuplicateIdException
from Domain.Film import Film


class Repositoryfilm:
    def __init__(self, fileName):
        self.__file = fileName
        self.__readFile()

    def __readFile(self):
        # Functia returneaza lista de rezervari
        try:
            with open(self.__file, "r") as f_read:
                saved_films = json.load(f_read)
                self.__storage.clear()
                for saved_film in saved_films:
                    film = Film(*saved_film)
                    self.__storage[film.getId()] = film
        except FileNotFoundError:
            self.__storage = {}

    #             id = int(components[0])
    #            idFilm = int(components[1])
    #           idCard = int(components[2])
    #          date = components[3]
    #         hour = components[4]
    #        film = film(id, idFilm, idCard, date, hour)
    #       self.__storage.append(film)
    # except FileNotFoundError:
    #    self.__storage = []

    def __writeFile(self):
        '''
        Functia scrie toate rezervarile
        :param listfilms: list, lista de rezervari
        :return:
        '''
        to_save = []
        for film in self.__storage.values():
            film_repr = [film.getId(), film.getTitle(), film.getYear(), film.getPrice(), film.getInProgram()]
            to_save.append(film_repr)
        with open(self.__file, 'w') as f_write:
            json.dump(to_save, f_write)

    def addfilm(self, film):
        '''
        Functia adauga o rezervare
        :param film: rezervare
        :return:
        '''
        self.__readFile()
        filmID = film.getId()
        if filmID in self.__storage:
            raise DuplicateIdException("invalid")
        self.__storage[film.getId()] = film
        self.__writeFile()

    def removefilm(self, film):
        '''
        Functia sterge o rezervare
        :param film: rezervare
        :return:
        '''

        del self.__storage[film.getId()]
        self.__writeFile()

    def read(self, film_id=None):
        '''
        Gets a film by id or all the films
        :param film_id: optional, the film id
        :return: the list of films or the film with the given id
        '''
        self.__readFile()
        if film_id is None:
            return self.__storage.values()

        if film_id in self.__storage:
            return self.__storage[film_id]
        return None

    def updatefilm(self, film):
        '''
        Modifica o rezervare
        :param film: rezervare
        :return:
        '''
        for reserv in self.__storage.values():
            if film.getId() == reserv.getId():
                self.__storage[film.getId()] = film
        self.__writeFile()
