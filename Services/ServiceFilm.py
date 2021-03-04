import random
import string

from Repository.RepositoryFilm import *
from Services.Undo_Redo import Operations


class ServiceFilm:
    def __init__(self, repositoryFilm, validator, reservation_repository):
        self.__repo = repositoryFilm
        self.__validator = validator
        self.__reservation_repository = reservation_repository
        self.__operations_undo = []
        self.__operations_redo = []

    def addFilmService(self, id, title, year, price, inProgram):
        """
        Functia adauga un film nou
        :param id: int, id-ul filmului
        :param title: str, titlul filmului
        :param year: int, anul aparitiei
        :param price: int, pretul
        :param inProgram: True daca e in ptogram, False daca nu
        :return:
        """

        film = Film(id, title, year, price, inProgram, False)
        self.__validator.validatePrice(film)
        self.__validator.validateYear(film)

        self.__repo.create(film)

        # self.__undo.append(lambda: self.__repo.delete(film.getID()))

    def updateFilm(self, id, newTitle, newYear, newPrice, newInProgram, is_removed):
        """
        Functia modifica un film
        :param is_removed:
        :param id: int, id-ul filmului
        :param newTitle: str, noul titlu
        :param newYear: int, noul an
        :param newPrice: int, noul pret
        :param newInProgram: noul status
        :return:
        """
        undo_film = self.__repo.read(id)
        if is_removed:
            film = Film(id, newTitle, newYear, newPrice, newInProgram, True)
        else:
            film = Film(id, newTitle, newYear, newPrice, newInProgram, False)
        self.__validator.validatePrice(film)
        self.__validator.validateYear(film)
        self.__repo.update(film)

    def __id_film_exists_in_reservation(self, id_film):
        for reservation in self.__reservation_repository.read():
            if reservation.getIdFilm() == id_film:
                return True
        return False

    def removeFilm(self, id):
        """
        Deletes a movie
        :param id: int, the id of the movie
        :return:
        """
        if self.__id_film_exists_in_reservation(id):
            raise ValueError("Filmul nu se poate sterge deoarece exista o rezervare cu acest film")
        film_to_delete = self.__repo.read(id)
        if film_to_delete is not None:
            self.__repo.delete(id)

    def getAllFilms(self):
        """
        Returns all movies
        :return:
        """
        return self.__repo.read()

    def populate(self, n):
        """
        The function populates a class with random info that abides by the attribute's rules
        :return:
        """
        films_added = []
        i = 0
        while i < n:
            try:

                list_films = []
                letters = string.ascii_lowercase
                id = random.randint(1, 101)
                title = ''.join(random.choice(letters) for i in range(10))
                year = random.randint(0, 2000)
                price = random.randint(0, 2000)
                inProgram = random.choice(["da", "nu"])
                if inProgram == "da":
                    inProgram = True
                else:
                    inProgram = False

                film = Film(id, title, year, price, inProgram, False)
                self.__validator.validatePrice(film)
                self.__validator.validateYear(film)
                if self.__repo.read(id) is not None:
                    raise Exception()
                self.__repo.create(film)
                films_added.append(film)
                i += 1
            except Exception:
                pass
        return films_added
        # self.__undo.append(lambda: self.__repo.delete(id))

    def search_text(self, string_film):
        """
        Searches the film that matches the description of the string
        :param string_film: the string that has the info of the attributes
        :return:
        """
        lista = []
        for descriptive_film in self.__repo.read():
            if string_film in descriptive_film.get_text_format():
                lista.append(descriptive_film)
        return lista

    def removepopulate_film(self, list_films):
        for thing in list_films:
            self.__repo.delete(thing.getID())

    def my_sorted_quicksort(self, lista, key=lambda x: x, reverse=False):
        """
        Implements my own sorted
        :param reverse:
        :param key:
        :param lista:
        :return:
        """
        if not lista:
            return []
        else:
            pivot = lista[0]
            greater_than_pivot = [nr for nr in lista if key(nr) > pivot]

            equal_to_pivot = [nr for nr in lista if key(nr) == pivot]
            less_than_pivot = [nr for nr in lista if key(nr) < pivot]
            return self.my_sorted_quicksort(greater_than_pivot, key) + \
                   equal_to_pivot + self.my_sorted_quicksort(less_than_pivot, key)

    def descr_by_number_of_reservations(self):
        dict = {}
        list_times = []
        for film in self.__repo.read():
            times = 0
            for reservation in self.__reservation_repository.read():
                if reservation.getIdFilm() == film.getID():
                    times += 1
            dict[film.getID()] = times
            if times not in list_times:
                list_times.append(times)

        lista = self.my_sorted_quicksort(list_times, key=lambda x: x)
        lista_reservari = []
        for index in lista:
            for key in dict.keys():
                if dict[key] == index:
                    lista_reservari.append(self.__repo.read(key))

        return lista_reservari

    def get_film(self, id):
        return self.__repo.read(id)

    def binary_search(self, x):
        lista = []
        for thing in self.__repo.read():
            lista.append(thing.getID())

        binary = self.my_sorted_quicksort(lista, key=lambda d: d)
        l = 0
        r = len(binary) - 1
        while l <= r:
            mid = (l + r) // 2

            if binary[mid] == x:
                return mid

                # If x is greater, ignore left half
            elif binary[mid] > x:
                l = mid + 1

            # If x is smaller, ignore right half
            else:
                r = mid - 1
        return -1
