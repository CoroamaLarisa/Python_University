class ValidateFilm:
    def validatePrice(self, film):
        if film.getPrice() < 0:
            raise ValueError("Pretul trebuie sa fie strict pozitiv")

    def validateYear(self, film):
        if film.getYear() <= 0:
            raise ValueError("Anul trebuie sa fie valid")
