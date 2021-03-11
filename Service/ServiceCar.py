import random
import string

from Domain.Car import Car
from Service.CarExistsInTransactionException import CarExistsInTransactionException


class ServiceCar:
    def __init__(self, repository, transactionRepository, carValidator):
        self.__repository = repository
        self.__tranRepo = transactionRepository
        self.__validator = carValidator

    def addCar(self, ID, model, yearPurchase, noKm, inGuarantee, isRemoved):
        '''
        Functia adauga o masina in repository
        :param ID: id-ul masinii
        :param model: modelul masinii
        :param yearPurchase: anul de achizitie
        :param noKm: numarul de km
        :param inGuarantee: daca masina e in garantie sau nu
        :param isRemoved: daca masina a fost stearsa
        :return:
        '''
        if inGuarantee not in ['da', 'nu']:
            raise ValueError('Garantia trebuie sa fie da sau nu')
        if inGuarantee == 'da':
            inGuarantee = True
        else:
            inGuarantee = False

        car = Car(ID, model, yearPurchase, noKm, inGuarantee, isRemoved)
        self.__validator.validate(car)
        self.__repository.create(car)

    def removeCar(self, idCar):
        '''
        Functia sterse masina cu id-ul dat
        :param idCar: id-ul masinii care trebuie stearsa
        :return:
        '''
        self.__repository.delete(idCar)

    def updateCar(self, ID, model, yearPurchase, noKm, inGuarantee, isRemoved):
        '''
        Functia modifica o masina
        :param ID: id-ul masinii
        :param model: modelul masinii
        :param yearPurchase: anul in care a fost cumparat
        :param noKm: numar de kilometrii
        :param inGuarantee: daca masina e in garantie sau nu
        :param isRemoved: daca masina a fost stearsa sau nu
        :return:
        '''
        if inGuarantee not in ['da', 'nu']:
            raise ValueError('Garantia trebuie sa fie da sau nu')
        if inGuarantee == 'da':
            inGuarantee = True
        else:
            inGuarantee = False

        car = Car(ID, model, yearPurchase, noKm, inGuarantee, isRemoved)
        self.__validator.validate(car)
        self.__repository.update(car)

    def getAll(self):
        '''
        Functia returneaza dictionarul cu masini
        :return:
        '''
        return self.__repository.read()

    def search_text(self, string_car):
        '''
        functia cauta in masini un text
        :param string_car: string-ul dupa care cauta utilizatorul masina
        :return:
        '''
        lista = []
        for car in self.__repository.read():
            if string_car in car.get_text_format():
                lista.append(car)
        return lista

    def populate(self, n):
        '''
        Functia populeaza enitatea masini
        :return:
        '''
        cars_added = []
        i = 0
        while i < n:
            try:
                letters = string.ascii_lowercase
                id = random.randint(1, 10001)
                model = ''.join(random.choice(letters) for i in range(10))
                yearPurchase = random.randint(1900, 2021)
                noKm = random.randint(0, 200)
                inGuarantee = random.choice(['da', 'nu'])
                self.addCar(id, model, yearPurchase, noKm, inGuarantee, False)
                car = Car(id, model, yearPurchase, noKm, inGuarantee, False)
                cars_added.append(car)
                i += 1
            except Exception as e:
                pass

        return cars_added

    def remove_populate(self, list_cars):
        for c in list_cars:
            self.removeCar(c.getID())

    def get_car(self, id):
        return self.__repository.read(id)

    def clear(self):
        self.__repository.clear()

    def car_is_in_a_transaction(self, id_car):

        for transaction in self.__tranRepo.read():
            if transaction.getIDCar() == id_car:
                return True

        return False

    def my_sorted_desc(self, l, key):

        if len(l) == 0:
            return []
        pivot = key(l[0])
        equal_to_pivot = [nr for nr in l if key(nr) == pivot]
        less_than_pivot = [nr for nr in l if key(nr) < pivot]
        greater_than_pivot = [nr for nr in l if key(nr) > pivot]

        return self.my_sorted_desc(greater_than_pivot, key) + equal_to_pivot + self.my_sorted_desc(less_than_pivot, key)

    def showCarsBasedOnSumMan(self):
        '''
        Functia arata masini in ordine descrescatoare in functie de suma de la manopera
        :return:
        '''
        transactions = self.__tranRepo.read()
        maxPerID = {}
        for transaction in transactions:
            idCar = transaction.getIDCar()
            sumMan = transaction.getSumMan()
            if idCar not in maxPerID:
                maxPerID[idCar] = 0
            maxPerID[idCar] += sumMan

        car_in_tran = list(filter(lambda car: self.car_is_in_a_transaction(car.getID()), self.__repository.read()))

        car_max_sum = self.my_sorted_desc(car_in_tran, key=lambda car: maxPerID[car.getID()])

        return car_max_sum

    def updateInGuarantee(self,l,l_upgraded):
        '''
        Updateaza Garantia masinilor
        :return:
        '''

        if len(l) == 0:
            return None
        if (l[0].getYearPurchase() < 2016 and l[0].getInGuarantee()) or (l[0].getNoKm() > 60000 and l[0].getInGuarantee()):
            self.updateCar(l[0].getID(), l[0].getModel(), l[0].getYearPurchase(), l[0].getNoKm(), 'nu', False)
            l_upgraded.append(l[0])
        self.updateInGuarantee(l[1:],l_upgraded)

    def undo_update(self, l_upgraded):
        for car in l_upgraded:
            self.__repository.update(car)
        l_upgraded.clear()

    def permutari(self):
        results = []

        def inner(permutare_curenta):
            if len(permutare_curenta) == len(self.__repository.read()):
                results.append(permutare_curenta)
                return

            for car in self.__repository.read():
                if car not in permutare_curenta:
                    inner(permutare_curenta + [car])

        inner([])
        lista_finala = []

        for r in results:
            lista_p = []
            for car in r:
                lista_p.append(car.get_text_format())
            lista_finala.append(lista_p)

        return lista_finala
