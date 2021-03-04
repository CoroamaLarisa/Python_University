from Domain.CardClient import CardClient
from Domain.Film import Film
from Domain.Reservation import Reservation

# cerintele 8,9 cu map si filter
#
from Services.Undo_Redo import Operations


class UserInterface:
    def __init__(self, serviceFilm, serviceCardClient, serviceReservation):
        self.__serviceFilm = serviceFilm
        self.__serviceCardClient = serviceCardClient
        self.__serviceReservation = serviceReservation
        self.__operations_undo = []
        self.__operations_redo = []

    def __show_list(self, objects):
        for object in objects:
            print(object)

    def __show_menu(self):
        print('1. Film')
        print('2. Carduri')
        print('3. Rezervari')
        print('4.Undo')
        print('5.Redo')
        print('x. Exit')

    def run_console(self):

        while True:
            self.__show_menu()
            op = input('Optiune: ')
            if op == '1':
                self.__show_menu_films()
            elif op == '2':
                self.__show_menu_cards()
            elif op == '3':
                self.__show_menu_reservations()
            elif op == '4':
                self.Undo()
            elif op == '5':
                self.Redo()
            elif op == 'x':
                break
            else:
                print('Comanda invalida!')

    def __show_films(self):
        print('-> Film <-')
        print('1.Adaugare')
        print('2.Stergere')
        print('3.Modifica')
        print('4.Afisare')
        print('5.Populare')
        print('6.Search full text')
        print('7.Ordonare descr dupa nr de rezervari')
        print('8.Stergere cascada')
        print('9.Undo?')
        print('10.Redo?')
        print('11.Binary_search')
        print('x.Back')

    def __show_menu_films(self):
        while True:
            self.__show_films()
            option = input('Optiunea : ')
            if option == '1':
                self.__handleAddFilm()
            elif option == '2':
                self.__handleRemoveFilm()
            elif option == '3':
                self.__handleUpdateFilm()
            elif option == '4':
                self.__show_list(self.__serviceFilm.getAllFilms())
            elif option == '5':

                self.__populateFilm()
            elif option == '6':
                self.__search_text()
            elif option == '7':
                self.__show_list(self.__serviceFilm.descr_by_number_of_reservations())
            elif option == '8':
                self.stergere_cascada_film()
            elif option == '9':
                self.Undo()
            elif option == '10':
                self.Redo()
            elif option == '11':
                self.binary()
            elif option == 'x':
                break
            else:
                print('Optiunea nu e valida!')

    def binary(self):
        x = int(input("Id-ul pe care il cautati: "))
        result = self.__serviceFilm.binary_search(x)
        if result != -1:
            print("Pozitia e: ", result)
        else:
            print("Nu exista obiectul cu asta")

    def __search_text(self):
        string_film = input('ce sa caute?: ')
        for thing in self.__serviceFilm.search_text(string_film):
            print(thing)

    def __populateFilm(self):
        n = int(input('De cate ori vreti sa se intample: '))
        list_films = self.__serviceFilm.populate(n)
        populari = Operations(lambda: self.__serviceFilm.populate(n),
                              lambda: self.__serviceFilm.removepopulate_film(list_films)
                              )
        self.__operations_undo.append(populari)

    def __handleAddFilm(self):
        try:
            id = int(input('Id-ul: '))
            title = input('Titlu: ')
            year = int(input('Anul: '))
            price = int(input('Pret: '))
            inProgram = True
            ok = int(input('Daca filmul nu este in program scrieti 1 :'))
            if ok == 1:
                inProgram = False
            add_film = Operations(lambda: self.__serviceFilm.addFilmService(id, title, year, price, inProgram),
                                  lambda: self.__serviceFilm.removeFilm(id))
            add_film.apply_action()
            self.__operations_undo.append(add_film)
            self.__operations_redo = []
            print('Filmul a fost adaugat')
        except Exception as ve:
            print('Erori:', ve)

    def __handleRemoveFilm(self):
        try:
            id = int(input('Id-ul filmului care trebuie sters:  '))
            film_create = self.__serviceFilm.get_film(id)
            delete = Operations(lambda: self.__serviceFilm.removeFilm(id),
                                lambda: self.__serviceFilm.addFilmService(film_create.getID(), film_create.getTitle(),
                                                                          film_create.getYear(),
                                                                          film_create.getPrice(),
                                                                          film_create.getInProgram()
                                                                          ))
            delete.apply_action()
            self.__operations_undo.append(delete)
            self.__operations_redo = []
        except Exception as ve:
            print(ve)

    def __handleUpdateFilm(self):
        '''

        :return:
        '''
        try:
            id = int(input('Id-ul filmului de modificat: '))
            title = input('Noul Titlu: ')
            year = int(input('Noul An: '))
            price = int(input('Noul Pret: '))
            inProgram = True
            ok = int(input('Daca filmul nu este in program scrieti 1 :'))
            if ok == 1:
                inProgram = False
            undo_film = self.__serviceFilm.get_film(id)
            update = Operations(lambda: self.__serviceFilm.updateFilm(id, title, year, price, inProgram, False),
                                lambda: self.__serviceFilm.updateFilm(undo_film.getID(), undo_film.getTitle(),
                                                                      undo_film.getYear(),
                                                                      undo_film.getPrice(), undo_film.getInProgram(),
                                                                      False))
            update.apply_action()
            self.__operations_undo.append(update)
            self.__operations_redo = []
        except Exception as ve:
            print('Erori: ')
            for error in ve.args[0]:
                print(error)

    def __show_cards(self):
        print('-> Card Client <-')
        print('1.Adaugare')
        print('2.Stergere')
        print('3.Modifica')
        print('4.Afisare')
        print('5.Populare')
        print('6.Cautare full text')
        print('7.Stergere cascada')
        print('8.Ordonarea cardurilor dupa numarul de puncte pe care il au')
        print('9.Incrementarea cardurilor care se afla intre anumite 2 date ')
        print('10.Undo')
        print('11.Redo')
        print('x.Back')

    def __show_menu_cards(self):
        while True:
            self.__show_cards()
            option = input('Optiunea : ')
            if option == '1':
                self.__handleAddCardClient()
            elif option == '2':
                self.__handleRemoveCardClient()
            elif option == '3':
                self.__handleUpdateCardClient()
            elif option == '4':
                self.__show_list(self.__serviceCardClient.getAllCards())
            elif option == '5':
                self.__populateCard()
            elif option == '6':
                self.__search_text_card()
            elif option == '7':
                self.stergere_cascada_card()
            elif option == '8':
                for thing in self.__serviceCardClient.card_client_descr_by_points():
                    print(thing)
            elif option == '9':
                self.increment_cards_by_date()
            elif option == '10':
                self.Undo()
            elif option == '11':
                self.Redo()
            elif option == 'x':
                break
            else:
                print('Optiunea nu e valida!')

    def __populateCard(self):
        n = int(input('De cate ori vreti sa se intample: '))
        list_cards = self.__serviceCardClient.populate(n)
        populari = Operations(lambda: self.__serviceCardClient.populate(n),
                              lambda: self.__serviceCardClient.remove_populate_card(list_cards)
                              )
        self.__operations_undo.append(populari)
        self.__operations_redo = []

    def __handleAddCardClient(self):
        try:
            id = int(input('Id-ul: '))
            surname = input('Surname : ')
            name = input('Numele: ')
            CNP = int(input('CNP: '))
            dateOfBirth = input("data de nastere: ")
            dateRegistration = input("data inregistrarii: ")
            point = int(input('Puncte: '))
            add_card = Operations(
                lambda: self.__serviceCardClient.addCardClient(id, surname, name, CNP, dateOfBirth, dateRegistration,
                                                               point),
                lambda: self.__serviceCardClient.removeCardClient(id))
            add_card.apply_action()
            self.__operations_undo.append(add_card)
            self.__operations_redo = []
            print('Cardul a fost adaugat')
        except Exception as ve:
            print('Erori: ', ve)

    def __handleRemoveCardClient(self):
        """
        handles the remove
        :return:
        """
        try:
            id = int(input('Id-ul cardului care trebuie sters:  '))
            card_create = self.__serviceCardClient.get_card(id)
            delete = Operations(lambda: self.__serviceCardClient.removeCardClient(id),
                                lambda: self.__serviceCardClient.addCardClient(card_create.getID(),
                                                                               card_create.getSurname(),
                                                                               card_create.getName(),
                                                                               card_create.getCNP(),
                                                                               card_create.getDateOfBirth(),
                                                                               card_create.getDateRegistration(),
                                                                               card_create.getPoint()))
            delete.apply_action()
            self.__operations_undo.append(delete)
            self.__operations_redo = []
        except Exception as ve:
            print(ve)

    def __handleUpdateCardClient(self):
        """
        Handles the update
        :return:
        """
        try:
            id = int(input('Id-ul filmului de modificat: '))
            surname = input('Noul prenume : ')
            name = input('Noul nume: ')
            CNP = int(input('Noul CNP: '))
            dateOfBirth = input("Noua data de nastere")
            dateRegistration = input("Noua data a inregistrarii")
            point = int(input('Noile puncte: '))
            card_create = self.__serviceCardClient.get_card(id)
            update = Operations(lambda: self.__serviceCardClient.updateCardClient(id, surname, name, CNP, dateOfBirth,
                                                                                  dateRegistration, point,
                                                                                  False),
                                lambda: self.__serviceCardClient.updateCardClient(card_create.getID(),
                                                                                  card_create.getSurname(),
                                                                                  card_create.getName(),
                                                                                  card_create.getCNP(),
                                                                                  card_create.getDateOfBirth(),
                                                                                  card_create.getDateRegistration(),
                                                                                  card_create.getPoint(),
                                                                                  False))
            update.apply_action()
            self.__operations_undo.append(update)
            self.__operations_redo = []
        except Exception as ve:
            print('Erori: ', ve)

    def __search_text_card(self):
        string_ = input('ce sa caute?:  ')
        for thing in self.__serviceCardClient.search_text(string_):
            print(thing)

    def increment_cards_by_date(self):
        """
        Find the reservation between the hours imputed by the user
        :return:
        """

        value = int(input('Introduceti valoarea cu care doriti sa incrementati'))
        date1 = input("Introduceti prima data: ")
        date2 = input("Introduceti a doua data: ")
        self.__serviceCardClient.increment_by_date(date1, date2, value, list(self.__serviceCardClient.getAllCards()))

    # 13.4.1966 13.7.1966
    def __show_reservations(self):
        print('-> Rezervari <-')
        print('1.Adaugare')
        print('2.Stergere')
        print('3.Modifica')
        print('4.Afisare')
        print('5.Filtrare printe ore')
        print('6.Stergere printe date')
        print('7.Undo')
        print('8.Redo')
        print('x.Back')

    def __show_menu_reservations(self):
        while True:
            self.__show_reservations()
            option = input('Optiunea : ')
            if option == '1':
                self.__handleAddReservation()
            elif option == '2':
                self.__handleRemoveReservation()
            elif option == '3':
                self.__handleUpdateReservation()
            elif option == '4':
                self.__show_list(self.__serviceReservation.getReservations())
            elif option == '5':
                self.find_reservations_by_hours()
            elif option == '6':
                self.delete_reservations_by_date()
            elif option == '7':
                self.Undo()
            elif option == '8':
                self.Redo()
            elif option == 'x':
                break
            else:
                print('Optiunea nu e valida!')

    def __handleAddReservation(self):
        try:
            id = int(input('Id-ul: '))
            idFilm = int(input('Id-ul filmului: '))
            idCard = int(input('Id-ul cardului: '))
            date = input("data: ")
            hour = input('Ora: ')
            add_reservation = Operations(
                lambda: self.__serviceReservation.addReservation(id, idFilm, idCard, date, hour),
                lambda: self.__serviceReservation.removeReservation(id))
            add_reservation.apply_action()
            self.__operations_undo.append(add_reservation)
            self.__operations_redo = []
        except Exception as ve:
            print('Erori: ', ve)

    def __handleRemoveReservation(self):
        try:
            id = int(input('Id-ul reservarii care trebuie stearsa:  '))
            reservation_create = self.__serviceReservation.get_reservation(id)
            delete = Operations(lambda: self.__serviceReservation.removeReservation(id),
                                lambda: self.__serviceReservation.addReservation(reservation_create.getID(),
                                                                                 reservation_create.getIdFilm(),
                                                                                 reservation_create.getIdCard(),
                                                                                 reservation_create.getDate(),
                                                                                 reservation_create.getHour()
                                                                                 ))
            delete.apply_action()
            self.__operations_undo.append(delete)
            self.__operations_redo = []
        except Exception as ve:
            print('Erori: ', ve)

    def __handleUpdateReservation(self):
        """
        Updated a reservation with the id imputed into the file
        :return:
        """
        try:
            id = int(input('Id-ul: '))
            idFilm = int(input('Id-ul filmului: '))
            idCard = int(input('Id-ul cardului: '))
            date = input("data: ")
            hour = input('Ora: ')
            reservation_create = self.__serviceReservation.get_reservation(id)
            update = Operations(lambda: self.__serviceReservation.updateReservation(id,
                                                                                    idFilm, idCard, date, hour, False),
                                lambda: self.__serviceReservation.addReservation(reservation_create.getID(),
                                                                                 reservation_create.getIdFilm(),
                                                                                 reservation_create.getIdCard(),
                                                                                 reservation_create.getDate(),
                                                                                 reservation_create.getHour(),
                                                                                 ))
            update.apply_action()
            self.__operations_undo.append(update)
            self.__operations_redo = []

        except Exception as ve:
            print('Erori:', ve)

    def find_reservations_by_hours(self):
        """
        Find the reservation between the hours imputed by the user
        :return:
        """
        hour1 = input("Introduceti prima ora: ")
        hour2 = input("Introduceti a doua ora: ")
        res = self.__serviceReservation.find_reservation_hour(hour1, hour2)
        for serv in res:
            print(serv)

    def delete_reservations_by_date(self):
        """
        Find the reservation between the hours imputed by the user
        :return:
        """
        date1 = input("Introduceti prima data: ")
        date2 = input("Introduceti a doua data: ")
        self.__serviceReservation.delete_by_date(date1, date2)

    # self.__id,
    # self.__surname,
    # self.__name,
    # self.__CNP,
    # self.__dateOfBirth,
    # self.__dateRegistration,
    # self.__points)
    def stergere_cascada_card(self):
        idCard = int(input("Introduceti id de la Filmul care trebuie sters: "))
        lista = self.delete_id_card_and_reservation(idCard)
        card = self.__serviceCardClient.get_card(idCard)
        cascada = Operations(lambda: self.delete_id_card_and_reservation(idCard),
                             lambda: self.undo_delete_card_and_reservation(lista, card))
        self.__operations_undo.append(cascada)
        self.__operations_redo=[]

    def delete_id_card_and_reservation(self, idCard):
        list_reservations = []
        for card in self.__serviceCardClient.getAllCards():
            if card.getID() == idCard:
                useful_card = card
                try:
                    self.__serviceCardClient.updateCardClient(idCard, useful_card.getSurname(), useful_card.getName(),
                                                              useful_card.getCNP(), useful_card.getDateOfBirth(),
                                                              useful_card.getDateRegistration(), useful_card.getPoint(),
                                                              True)
                except Exception as ve:
                    print('Erori', ve)
                for res in self.__serviceReservation.getReservations():
                    if res.getIdCard() == idCard:
                        list_reservations.append(res)
                        self.__serviceReservation.removeReservation(res.getID())
        return list_reservations

    def undo_delete_card_and_reservation(self, lista, useful_card):
        self.__serviceCardClient.updateCardClient(useful_card.getID(), useful_card.getSurname(), useful_card.getName(),
                                                  useful_card.getCNP(), useful_card.getDateOfBirth(),
                                                  useful_card.getDateRegistration(), useful_card.getPoint(),
                                                  True)
        for reservation_create in lista:
            self.__serviceReservation.addReservation(reservation_create.getID(),
                                                     reservation_create.getIdFilm(),
                                                     reservation_create.getIdCard(),
                                                     reservation_create.getDate(),
                                                     reservation_create.getHour())

    def stergere_cascada_film(self):
        idFilm = int(input("Introduceti id de la Filmul care trebuie sters: "))
        lista = self.delete_id_film_and_reservation(idFilm)
        film = self.__serviceFilm.get_film(idFilm)
        cascada = Operations(lambda: self.delete_id_film_and_reservation(idFilm),
                             lambda: self.undo_delete_film_and_reservation(lista, film))
        self.__operations_undo.append(cascada)

    def delete_id_film_and_reservation(self, idFilm):

        list_reservations = []
        for film in self.__serviceFilm.getAllFilms():
            if film.getID() == idFilm:
                useful_Film = film

                try:
                    self.__serviceFilm.updateFilm(idFilm, useful_Film.getTitle(), useful_Film.getYear(),
                                                  useful_Film.getPrice(), useful_Film.getInProgram(),
                                                  True)

                except Exception as ve:
                    print('Erori', ve)
                for res in self.__serviceReservation.getReservations():
                    if res.getIdFilm() == idFilm:
                        list_reservations.append(res)
                        self.__serviceReservation.removeReservation(res.getID())
        return list_reservations

    def undo_delete_film_and_reservation(self, lista, film):
        self.__serviceFilm.updateFilm(film.getID(), film.getTitle(), film.getYear(),
                                      film.getPrice(), film.getInProgram(),
                                      False)
        for reservation_create in lista:
            self.__serviceReservation.addReservation(reservation_create.getID(),
                                                     reservation_create.getIdFilm(),
                                                     reservation_create.getIdCard(),
                                                     reservation_create.getDate(),
                                                     reservation_create.getHour())

    def Undo(self):
        try:
            if len(self.__operations_undo) > 0:
                undo = self.__operations_undo.pop()
                undo.apply_reverse_action()
                self.__operations_redo.append(undo)
            else:
                raise ValueError("Nu se poate face Undo")
        except Exception as ve:
            print('Erori', ve)

    def Redo(self):
        try:
            if len(self.__operations_redo) > 0:
                redo = self.__operations_redo.pop()
                redo.apply_action()
                self.__operations_undo.append(redo)
            else:
                raise ValueError("Nu se poate face Undo")
        except Exception as ve:
            print('Erori', ve)

"""
1. CRUD film: id, titlu, an apariție, preț bilet, în program. Prețul să fie strict pozitiv.
2. CRUD card client: id, nume, prenume, CNP, data nașterii (dd.mm.yyyy), data înregistrării
(dd.mm.yyyy), puncte acumulate. CNP-ul trebuie să fie unic.
3. CRUD rezervare: id, id_film, id_card_client (poate fi nul), data și ora. Clientul
acumulează pe card 10% (parte întreagă) din prețul filmului Se tipărește numărul total
de puncte de pe card. Rezervarea se poate face doar dacă filmul este încă în program.
4. Căutare filme și clienți după titlu, nume, prenume, CNP etc. Căutare full text.
5. Afișarea tuturor rezervărilor dintr-un interval de ore dat, indiferent de zi.  ---FACUT CU FILTER
6. Afișarea filmelor ordonate descrescător după numărul de rezervări. --- FACUT CU MY SORTED PSEUDO-QUICKSORT
7. Afișarea cardurilor client ordonate descrescător după numărul de puncte de pe card. -- FACUT CU SORTED
8. Ștergerea tuturor rezervărilor dintr-un anumit interval de zile. -- FACUT CU FILTER
9. Incrementarea cu o valoare dată a punctelor de pe toate cardurile a căror zi de naștere
se află într-un interval dat. -- RECURSIV
"""
