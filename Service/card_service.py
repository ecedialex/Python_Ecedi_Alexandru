from typing import List
from Domain.card_client import Card
from Domain.card_validator import CardValidator
from Repository.repository import Repository


class CardService:
    def __init__(self,
                 card_repository: Repository,
                 card_validator: CardValidator):
        self.card_repository = card_repository
        self.card_validator = card_validator

    def add_card(self,
                 id_card,
                 nume,
                 prenume,
                 CNP,
                 data_nasterii,
                 data_inregistrarii):
        """
        Adauga un card in fisier
        :param id_card: id-ul cardului - va fi unic
        :param nume: numele titularului de card
        :param prenume: prenumele titularului
        :param CNP: cnp-ul titularului (unic)
        :param data_nasterii: data nasterii titularului
        :param data_inregistrarii: data inregistrarii cardului
        :return: -
        """

        card = Card(id_card, nume, prenume, CNP, data_nasterii,
                    data_inregistrarii)
        self.card_validator.validate(card)
        self.card_repository.create(card)

    def update_card(self,
                    id_card,
                    nume,
                    prenume,
                    CNP,
                    data_nasterii,
                    data_inregistrarii):

        card = Card(id_card, nume, prenume, CNP, data_nasterii,
                    data_inregistrarii)
        self.card_validator.validate(card)
        self.card_repository.update(card)

    def delete_card(self, id_card: str):
        self.card_repository.delete(id_card)

    def get_all(self) -> List[Card]:
        return self.card_repository.read()

    def full_text_search_card(self, text):
        carduri = self.get_all()
        result = []

        for card in carduri:
            if text.lower() in str(card.id_entity):
                result.append(card)
            elif text.lower() in card.nume_client.lower():
                result.append(card)
            elif text.lower() in card.prenume_client.lower():
                result.append(card)
            elif text.lower() in card.CNP.lower():
                result.append(card)
            elif text.lower() in str(card.data_nasterii).lower():
                result.append(card)
            elif text.lower() in str(card.data_inregistrarii).lower():
                result.append(card)
        return result
