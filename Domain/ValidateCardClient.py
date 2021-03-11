from Domain.ValidateDate import ValidateDate
from Service.DuplicateCNPException import DuplicateCNPException


class ValidateCardClient:

    def validate(self, tovalidatecard, card_repo):
        '''
        Functia valideaza cardul
        :param tovalidatecard: cardul care trebuie validat
        :param card_repo: repository a cardurilor
        :return:
        '''
        CNPCardClient = tovalidatecard.getCNP()
        for cards in card_repo.read():
            if cards.getCNP() == CNPCardClient and cards.getID() != tovalidatecard.getID():
                raise DuplicateCNPException('Deja exista un card client cu CNP-ul asta')
        ValidateDate(tovalidatecard.getDateOfBirth())
        ValidateDate(tovalidatecard.getDateOfRegistration())
