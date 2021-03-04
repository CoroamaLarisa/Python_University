import datetime
import random
import string

from Domain.CardClient import CardClient
from Domain.Reservation import Reservation


class ServiceReservation:

    def __init__(self, repositoryReservation, validator, repositoryFilm, repositoryCard):
        self.__repo = repositoryReservation
        self.__validator = validator
        self.__repo_film = repositoryFilm
        self.__repo_card = repositoryCard

    def addReservation(self, id, idFilm, idCard, date, hour):
        '''
        
        :param id: 
        :param idFilm: 
        :param idCard: 
        :param date: 
        :param hour: 
        :return: 
        '''
        self.__validator.validateDate(date)
        self.__validator.validateHour(hour)
        self.__validator.validate_id_film(idFilm, self.__repo_film)
        for film in self.__repo_film.read():
            if film.getID() == idFilm:
                if film.getInProgram():

                    self.__validator.validateDate(date)
                    self.__validator.validateHour(hour)
                    reservation = Reservation(id, idFilm, idCard, date, hour)
                    self.__repo.create(reservation)

                    if self.__repo_card.read(idCard) is not None:
                        self.percent_updated(idCard, idFilm)
                else:
                    raise ValueError("Filmul nu este in program")

    def percent_updated(self, idCard, idFilm):
        """
        Updates the points on the card based on the films price
        :param idCard:
        :param idFilm:
        :return:
        """
        card = self.__repo_card.read(idCard)
        film = self.__repo_film.read(idFilm)
        newPoints = card.getPoint() + (film.getPrice() * (10 / 100))
        card = CardClient(card.getID(), card.getSurname(), card.getName(), card.getCNP(), card.getDateOfBirth(),
                          card.getDateRegistration(), newPoints, card.getIsRemoved())
        self.__repo_card.update(card)

    def updateReservation(self, id, idFilm, idCard, date, hour, is_removed):
        '''
        
        :param is_removed:
        :param id:
        :param idFilm: 
        :param idCard: 
        :param date: 
        :param hour: 
        :return: 
        '''
        to_be_updated = self.__repo.read(id)
        reservation = Reservation(id, idFilm, idCard, date, hour, is_removed)
        self.__validator.validate_id_film(idFilm, self.__repo_film)
        self.__validator.validateHour(reservation)
        self.__validator.validateDate(date)

        self.__repo.update(reservation)

    def removeReservation(self, id):
        '''
        Sterge un reservation
        :param id: int, id-ul
        :return:
        '''

        reservation = self.__repo.read(id)
        self.__repo.delete(id)


    def getReservations(self):
        '''
        Returneaza toate 
        :return:
        '''
        return self.__repo.read()

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

    def reservation_hours(self, hour, minute, hour1, hour2, minute1, minute2):
        if hour1 < hour < hour2:
            return 1
        elif hour1 == hour and minute1 <= minute:
            return 1
        elif hour2 == hour and minute <= minute2:
            return 1
        return 0

    def find_reservation_hour(self, hour1, hour2):
        hour1 = hour1.split(':')
        hours1 = int(hour1[0])
        minutes1 = int(hour1[1])
        hour2 = hour2.split(':')
        hours2 = int(hour2[0])
        minutes2 = int(hour2[1])
        lista = list(filter(
            lambda x: self.reservation_hours(x.getIntHour()[0], x.getIntHour()[1], hours1, hours2, minutes1, minutes2),
            self.__repo.read()))
        # for reservation in self.__repo.read():
        #     hours_reservation = reservation.getIntHour()
        #     lista.append(reservation.getIntHour())
        # lista2 = list(filter(self.reservation_hours(x[0], x[1], hour1, hour2, minute1, minute2),lista))
        return lista

    def datetime_date(self, date, date1, date2):
        if date1 > date2:
            date1, date2 = date2, date1
        zero_date = datetime.timedelta(0)
        if date2 - date >= zero_date and date - date1 >= zero_date:
            return 1
        return 0

    def delete_by_date(self, date1, date2):
        self.__validator.validateDate(date1)
        self.__validator.validateDate(date2)
        get_date1_format = self.get_datetime_format(date1)
        get_date2_format = self.get_datetime_format(date2)
        lista = list(filter(lambda x: self.datetime_date(x.get_datetime_date(), get_date1_format, get_date2_format),
                            self.__repo.read()))

        for obiect in lista:
            self.__repo.delete(obiect.getID())

    def get_reservation(self,id):
        return self.__repo.read(id)
    # def removeCascada(self,idCard,idFilm):
    #     if self.__repo_card.read(idCard) is None:

    # def search_text(self, string_reservation):
    #     for reservation in self.__repo.read():
    #         if reservation.get_text_format() == string_reservation:
    #             return reservation
    #
