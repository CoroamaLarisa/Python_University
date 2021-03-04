class ValidateReservation:
    def validateDate(self, date):
        dateToValidate = date.split('.')
        if len(dateToValidate) != 3:
            raise ValueError('Gresit data')
        else:
            day = int(dateToValidate[0])
            month = int(dateToValidate[1])
            year = int(dateToValidate[2])
            if not ((0 < day < 32) or (0 < month < 13) or year > 0):
                raise ValueError('Gresit data')

    def validateHour(self, hour):
        hour = hour.split(':')
        hours = int(hour[0])
        minutes = int(hour[1])
        if hours > 23 or minutes > 59:
            raise ValueError('Ora trebuie sa fie valida : de la 00:00 la 23:59')

    def validate_id_film(self, idFilm, repo_film):
        if repo_film.read(idFilm) is None:
            raise ValueError('Nu exista film cu id-ul asta')
