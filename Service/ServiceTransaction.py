import datetime
import random
import string

from Domain.Car import Car
from Domain.CardClient import CardClient
from Domain.Transaction import Transaction
from Domain.ValidateDate import ValidateDate


class ServiceTransaction:
    def __init__(self, repository, carsRepository, cardRepository, transactionValidator):
        self.__repository = repository
        self.__carsRepository = carsRepository
        self.__cardRepository = cardRepository
        self.__validator = transactionValidator

    def addTransaction(self, ID, IDCar, IDCardClient, sumPieces, sumMan, date, hour, reducedSum):
        """
        Functia adauga o tranzactie pe baza parametrilot
        :param ID: id-ul tranzactiei
        :param IDCar: id-ul masinii din tranzactie
        :param IDCardClient: id-ul cardului din tranzactie
        :param sumPieces: suma pieselor masinii
        :param sumMan: suma manoperei tranzactiei
        :param date: data in care s-a efectuat tranzactia
        :param hour: ora la care s-a efectuat tranzactia
        :param reducedSum: suma cu care s-a redus pe baza reducerilor
        :return:
        """
        for card in self.__cardRepository.read():
            if card.getID() == IDCardClient:
                reducedSum += sumMan * 10 / 100
                sumMan = sumMan * 90 / 100
                break

        for cars in self.__carsRepository.read():
            if cars.getID() == IDCar and cars.getInGuarantee():
                reducedSum += sumPieces
                sumPieces = 0

        transaction = Transaction(ID, IDCar, IDCardClient, sumPieces, sumMan, date, hour, reducedSum)
        self.__validator.validate(transaction, self.__carsRepository)
        self.__repository.create(transaction)
        print('Pretul platit: ', sumPieces + sumMan)
        if reducedSum != 0:
            print('Reducerile acordate:', reducedSum)

    def removeTransaction(self, idTransaction):
        self.__repository.delete(idTransaction)

    def updateTransaction(self, ID, IDCar, IDCardClient, sumPieces, sumMan, date, hour, reducedSum):
        """
        Functia modifica o masina prin parametrii dati
        :param ID: id-ul tranzactiei
        :param IDCar: id-ul masinii din tranzactie
        :param IDCardClient: id-ul cardului din tranzactie
        :param sumPieces: suma pieselor masinii
        :param sumMan: suma manoperei tranzactiei
        :param date: data in care s-a efectuat tranzactia
        :param hour: ora la care s-a efectuat tranzactia
        :param reducedSum: suma cu care s-a redus pe baza reducerilor
        :return:
        """
        transaction = Transaction(ID, IDCar, IDCardClient, sumPieces, sumMan, date, hour, reducedSum)
        self.__validator.validate(transaction, self.__carsRepository)
        self.__repository.update(transaction)

    def getAll(self):
        return self.__repository.read()

    def get_transaction(self, id):
        return self.__repository.read(id)

    def populate(self, n):
        """
        Functia populeaza entitatea Tranzactie
        :return:
        """
        list_tran = []
        i = 0
        while i < n:
            try:
                id = random.randint(1, 101)
                id_car = random.randint(1, 101)
                id_cardClient = random.randint(1, 101)
                sumPieces = random.randint(1, 100000)
                sumMan = random.randint(1, 200000)
                day = random.randint(0, 31)
                month = random.randint(0, 12)
                year = random.randint(1950, 2000)
                date = "{}.{}.{}".format(day, month, year)
                hours = random.randint(0, 24)
                minutes = random.randint(0, 59)
                hour = "{}:{}".format(hours, minutes)
                self.addTransaction(id,
                                    id_car,
                                    id_cardClient,
                                    sumPieces,
                                    sumMan,
                                    date,
                                    hour,
                                    0
                                    )
                tran = Transaction(id,
                                   id_car,
                                   id_cardClient,
                                   sumPieces,
                                   sumMan,
                                   date,
                                   hour,
                                   0)
                list_tran.append(tran)

                i += 1
            except Exception as e:
                pass

        return list_tran

    def remove_populate(self, list_tran):
        for t in list_tran:
            self.__repository.delete(t.getID())

    def clear(self):
        self.__repository.clear()

    def showTransactionWithSumInInterval(self, lessSum, greaterSum):
        """
        Functia returneaza tranzactiile a caror suma sunt intr-un anumit interval
        :param lessSum: suma mica
        :param greaterSum: suma mare
        :return: dictionarul cu tranzactii care se potrivesc
        """

        return list(
            filter(lambda transaction: lessSum < transaction.getSumMan() + transaction.getSumPieces() < greaterSum,
                   self.__repository.read()))

    def card_in_transaction(self, id_card):
        for transaction in self.__repository.read():
            if transaction.getIDCardClient() == id_card:
                return True

        return False

    def showCardClientDescOrd(self):
        '''
        Functia arata cardurile in ordine descrescatoare pe baza reducerilor acumulate
        :return:
        '''
        transactions = self.__repository.read()
        maxPerID = {}
        for transaction in transactions:
            idCard = transaction.getIDCardClient()
            sumDiscount = transaction.getDiscount()
            if idCard not in maxPerID:
                maxPerID[idCard] = 0
            maxPerID[idCard] += sumDiscount
        cards = filter(lambda c: self.card_in_transaction(c.getID()), self.__cardRepository.read())
        return sorted(cards, key=lambda c: maxPerID[c.getID()], reverse=True)

    def get_date_format(self, date):
        newdate = date.split('.')
        day = int(newdate[0])
        month = int(newdate[1])
        year = int(newdate[2])
        fulldate = datetime.datetime(year, month, day)
        return fulldate

    def undo_erase_based_on_date(self, list_t):
        for t in list_t:
            self.__repository.create(t)

    def eraseTransactionBasedOnDate(self, date1, date2):
        list_t = []
        ValidateDate(date1)
        ValidateDate(date2)
        get_date1 = self.get_date_format(date1)
        get_date2 = self.get_date_format(date2)
        if get_date1 > get_date2:
            get_date1, get_date2 = get_date2, get_date1

        listToRemove = filter(lambda transaction: get_date1 < self.get_date_format(transaction.getDate()) < get_date2,
                              self.__repository.read())
        for transaction in listToRemove:
            list_t.append(transaction)
            self.removeTransaction(transaction.getID())
        return list_t

    def undo_delete_id_car_and_transaction(self, list_tran, idCar):
        car = self.__carsRepository.read(idCar)
        newcar = Car(car.getID(), car.getModel(), car.getYearPurchase(), car.getNoKm(),
                     car.getInGuarantee(), False)
        self.__carsRepository.update(newcar)
        for t in list_tran:
            self.__repository.create(t)

    def delete_id_car_and_transaction(self, idCar):
        """
        Functia sterge in cascada o tranzactie dupa id-ul unei masini date
        :return:
        """
        list_t = []
        for car in self.__carsRepository.read():
            if car.getID() == idCar:
                useful_car = car
                try:
                    newCar = Car(idCar, useful_car.getModel(), useful_car.getYearPurchase(),
                                 useful_car.getNoKm(),
                                 useful_car.getInGuarantee(), True)
                    self.__carsRepository.update(newCar)
                except Exception as ve:
                    print('Erori', ve)
                for tran in self.__repository.read():
                    if tran.getIDCar() == idCar:
                        list_t.append(tran)
                        self.removeTransaction(tran.getID())
        return list_t

    def delete_id_card_and_transaction(self, idCard):
        """
        Functia sterge in cascada o tranzactie dupa id-ul unei masini date
        :return:
        """
        list_t = []
        for card in self.__cardRepository.read():
            if card.getID() == idCard:
                useful_card = card
                try:
                    # ID, surname, name, CNP, dateOfBirth, dateOfRegistration, isRemoved
                    newCard = CardClient(idCard, useful_card.getSurname(), useful_card.getName(),
                                         useful_card.getCNP(), useful_card.getDateOfBirth(),
                                         useful_card.getDateOfRegistration(), True)
                    self.__cardRepository.update(newCard)
                except Exception as ve:
                    print('Erori', ve)
                for tran in self.__repository.read():
                    if tran.getIDCardClient() == idCard:
                        list_t.append(tran)
                        self.__repository.removeTransaction(tran.getID())
        return list_t

    def undo_delete_id_card_and_transaction(self, list_t, idCard):
        card = self.__cardRepository.read(idCard)
        newCard = CardClient(card.getID(), card.getSurname(),
                             card.getName(), card.getCNP()
                             , card.getDateOfBirth(), card.getDateOfRegistration(),
                             False)
        self.__cardRepository.update(newCard)

        for t in list_t:
            self.__repository.create(t)
