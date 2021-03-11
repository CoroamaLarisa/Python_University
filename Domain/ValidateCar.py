
class ValidateCar:

    def validate(self, car):
        '''
        Functia valideaza masina
        :param car: masina care trebuie validata
        :return:
        '''
        if car.getYearPurchase() < 0 or car.getNoKm() < 0:
            raise ValueError(' Km și anul fabricației să fie strict pozitivi.')
