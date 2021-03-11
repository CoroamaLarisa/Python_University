class RepositoryCar:
    def __init__(self):
        self.__storage = {}

    def create(self, car):
        carID = car.getID()
        if carID in self.__storage:
            raise KeyError('Deja este o masina cu id-ul asta')

        self.__storage[carID] = car

    def read(self, carID=None):

        if carID is None:
            return self.__storage.values()

        if carID in self.__storage:
            return self.__storage[carID]

        return None

    def update(self, newCar):
        newCarID = newCar.getID()
        if newCarID not in self.__storage:
            raise KeyError('Nu exista o masina cu ID-ul asta')

        self.__storage[newCarID] = newCar

    def delete(self, idCar):
        if idCar not in self.__storage:
            raise KeyError('Nu exista o masina cu id-ul asta')

        del self.__storage[idCar]

    def clear(self):
        self.__storage.clear()