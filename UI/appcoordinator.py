from Domain.ValidateCar import ValidateCar
from Domain.ValidateCardClient import ValidateCardClient
from Domain.ValidateTransaction import ValidateTransaction
from Repository.GenericFileRepository import GenericFileRepository
from Repository.RepositoryCar import RepositoryCar
from Repository.RepositoryCardClient import RepositoryCardClient
from Repository.RepositoryTransaction import RepositoryTransaction
from Service.ServiceCar import ServiceCar
from Service.ServiceCardClient import ServiceCardClient
from Service.ServiceTransaction import ServiceTransaction
from UI.Console import Console

# car_repository = RepositoryCar()
# cardClient_repository = RepositoryCardClient()
# transaction_repository = RepositoryTransaction()
car_repository = GenericFileRepository('Cars.pkl')
cardClient_repository = GenericFileRepository('Cards.pkl')
transaction_repository = GenericFileRepository('Transactions.pkl')
car_validator = ValidateCar()
cardClient_validator = ValidateCardClient()
transaction_validator = ValidateTransaction()

car_service = ServiceCar(car_repository, transaction_repository, car_validator)
cardClient_service = ServiceCardClient(cardClient_repository, cardClient_validator)
transaction_service = ServiceTransaction(transaction_repository, car_repository, cardClient_repository,
                                         transaction_validator)
console = Console(car_service, cardClient_service, transaction_service)

console.run_console()
