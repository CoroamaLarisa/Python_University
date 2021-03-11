class ValidateTransaction:
    def validate(self, transaction,carRepo):
        '''

        :param transaction: tranzactia care trebuie validata
        :param carRepo: repository a masinilor (deoarece existenta unei tranzactii depinde de existenta unui id al
        masinii)
        :return:
        '''

        if carRepo.read(transaction.getIDCar()) is None:
            raise ValueError('Nu exista o masina cu ID-ul asta')

        hour = transaction.getHour()

        hour = hour.split(":")
        if len(hour) != 2:
            raise ValueError('Ora nu e buna')
        else:
            hours = int(hour[0])
            minutes = int(hour[1])
            if (hours > 24 or hours < 0) and (minutes > 59 or minutes < 0):
                raise ValueError('Ora nu e buna')
