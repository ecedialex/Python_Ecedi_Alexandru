from Domain.card_validator import CardValidator
from Domain.medicament_validator import MedicamentValidator
from Repository.json_repository import JsonRepository
from Service.card_service import CardService
from Service.medicament_service import MedicamentService
from Service.tranzactie_service import TranzactieService
from Tests.test_medicament_repository import test_medicament_repository
from UserInterface.Console import Console


def main():
    medicament_repository = JsonRepository('medicamente.json')
    medicament_validator = MedicamentValidator()
    medicament_service = \
        MedicamentService(medicament_repository,
                          medicament_validator)

    card_repository = JsonRepository('carduri.json')
    card_validator = CardValidator()
    card_service = CardService(card_repository, card_validator)

    tranzactie_repository = JsonRepository('tranzactii.json')
    tranzactie_service = \
        TranzactieService(tranzactie_repository,
                          card_repository,
                          medicament_repository)
    console = Console(medicament_service,
                      card_service,
                      tranzactie_service)
    console.run_console()


if __name__ == '__main__':
    test_medicament_repository()
    main()
