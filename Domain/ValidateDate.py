class ValidateDate:
    def __init__(self, date):
        '''
        Functia valideaza o data
        :param date: data care trebuie validata
        '''
        dateToValidate = date.split(".")

        if len(dateToValidate) != 3:
            raise ValueError('Nu merge data pusa')
        else:
            day = int(dateToValidate[0])
            month = int(dateToValidate[1])
            year = int(dateToValidate[2])
            if (0 > day or day > 31) and (0 > month or month > 12) and year < 0:
                raise ValueError('Nu merge data pusa')
