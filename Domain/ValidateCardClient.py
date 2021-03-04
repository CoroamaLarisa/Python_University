from Domain.DuplicateCNP import DuplicateCNP


class ValidateCardClient:
    def validateCNP(self, CNPvalidated, repo_card, id):
        for value in repo_card.read():
            if value.getCNP() == CNPvalidated and value.getID() != id:
                raise DuplicateCNP

    def validateDate(self, date):
        dateToValidate = date.split('.')
        if len(dateToValidate) != 3:
            raise ValueError('Gresit data')
        else:
            day = int(dateToValidate[0])
            month = int(dateToValidate[1])
            year = int(dateToValidate[2])
            if not (1 <= day <= 31) and (1 <= month <= 12) and year > 0:
                raise ValueError('Gresit data')
