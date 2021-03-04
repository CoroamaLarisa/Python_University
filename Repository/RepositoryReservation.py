import json

from Domain.DuplicateIdException import DuplicateIdException
from Domain.Reservation import Reservation


class RepositoryReservation:
    def __init__(self, fileName):
        self.__file = fileName
        self.__readFile()

    def __readFile(self):
        # Functia returneaza lista de rezervari
        try:
            with open(self.__file, "r") as f_read:
                saved_reservations = json.load(f_read)
                self.__storage.clear()
                for saved_reservation in saved_reservations:
                    reservation = Reservation(*saved_reservation)
                    self.__storage[reservation.getID()] = reservation
        except FileNotFoundError:
            self.__storage = {}

    #             id = int(components[0])
    #            idFilm = int(components[1])
    #           idCard = int(components[2])
    #          date = components[3]
    #         hour = components[4]
    #        reservation = Reservation(id, idFilm, idCard, date, hour)
    #       self.__storage.append(reservation)
    # except FileNotFoundError:
    #    self.__storage = []

    def __writeFile(self):
        '''
        Functia scrie toate rezervarile
        :param listReservations: list, lista de rezervari
        :return:
        '''
        to_save = []
        for reservation in self.__storage.values():
            reservation_repr = [reservation.getId(), reservation.getIdFilm(), reservation.getIdCard(),
                                reservation.getDate(), reservation.getHour()]
            to_save.append(reservation_repr)
        with open(self.__file, 'w') as f_write:
            json.dump(to_save, f_write)

    def addReservation(self, reservation):
        '''
        Functia adauga o rezervare
        :param reservation: rezervare
        :return:
        '''
        self.__readFile()
        reservationID = reservation.getId()
        if reservationID in self.__storage:
            raise DuplicateIdException("invalid")
        self.__storage[reservation.getId()] = reservation
        self.__writeFile()

    def removeReservation(self, reservation):
        '''
        Functia sterge o rezervare
        :param reservation: rezervare
        :return:
        '''

        del self.__storage[reservation.getId()]
        self.__writeFile()

    def read(self, reservation_id=None):
        '''
        Gets a reservation by id or all the reservations
        :param reservation_id: optional, the reservation id
        :return: the list of reservations or the reservation with the given id
        '''
        self.__readFile()
        if reservation_id is None:
            return self.__storage.values()

        if reservation_id in self.__storage:
            return self.__storage[reservation_id]
        return None

    def updateReservation(self, reservation):
        '''
        Modifica o rezervare
        :param reservation: rezervare
        :return:
        '''
        for reserv in self.__storage.values():
            if reservation.getId() == reserv.getId():
                self.__storage[reservation.getId()]=reservation
        self.__writeFile()

