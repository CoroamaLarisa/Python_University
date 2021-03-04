from Domain.ValidateCardClient import ValidateCardClient
from Domain.ValidateFilm import ValidateFilm
from Domain.ValidateReservation import ValidateReservation
from Repository.GenericFileRepository import GenericFileRepository
from Services.ServiceCardClient import ServiceCardClient
from Services.ServiceFilm import ServiceFilm
from Services.ServiceReservation import ServiceReservation
from UserInterface.Console import UserInterface

fileName1 = "Cinema.txt"
fileName2 = "Carduri.txt"
fileName3 = "Rezervari.txt"


def run():
    repo_CardClient = GenericFileRepository(fileName2)
    repo_Film = GenericFileRepository(fileName1)
    repo_Reservation = GenericFileRepository(fileName3)
    card_validator = ValidateCardClient()
    film_validator = ValidateFilm()
    reservation_validator = ValidateReservation()
    serviceCardClient = ServiceCardClient(repo_CardClient, card_validator,repo_Reservation)
    serviceFilm = ServiceFilm(repo_Film, film_validator,repo_Reservation)

    serviceReservation = ServiceReservation(repo_Reservation, reservation_validator, repo_Film, repo_CardClient)

    console = UserInterface(serviceFilm, serviceCardClient, serviceReservation)

    console.run_console()


# randomizer = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
# print(randomizer)
# print(random.randint(1,100))
run()
