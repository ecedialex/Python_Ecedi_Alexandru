import datetime

from typing import List
from Domain.tranzactie import Tranzactie
from Repository.repository import Repository
from ViewModels.TransactionsBetweenTwoDates import TransactionsBetweenTwoDates


class TranzactieService:
    def __init__(self,
                 tranzactie_repository: Repository,
                 card_repository: Repository,
                 medicament_repository: Repository):

        self.tranzactie_repository = tranzactie_repository
        self.card_repository = card_repository
        self.medicament_repository = medicament_repository

    def add_tranzactie(self,
                       id_tranzactie: str,
                       id_medicament: str,
                       id_card: str,
                       nr_bucati: str,
                       data_tranzactie,
                       ora_tranzactie,
                       valoare_tranzactie,
                       reducere):
        """
        Verifica si adauga un card in lista daca este valid
        :param reducere:
        :param valoare_tranzactie:
        :param ora_tranzactie:
        :param data_tranzactie:
        :param nr_bucati:
        :param id_medicament:
        :param id_tranzactie: id-ul tranzactiei
        :param id_card: id-ul medicamentului
        :return: fisierul medicamente cu lista de medicamente
        """

        id_medicament = f'{id_medicament}'
        medicament = self.medicament_repository.read(id_medicament)
        s = float(medicament.pret_medicament) * float(nr_bucati)
        valoare_tranzactie = s
        valoare_tranzactie_initiala = valoare_tranzactie
        if id_card != '0':
            if medicament.necesita_reteta == 'nu':
                valoare_tranzactie = (float(valoare_tranzactie) -
                                      float(valoare_tranzactie) / 10)

            elif medicament.necesita_reteta == 'da':
                valoare_tranzactie = (float(valoare_tranzactie) -
                                      float((valoare_tranzactie * 15) / 100))

        else:
            valoare_tranzactie = float(medicament.pret_medicament) * \
                                 float(nr_bucati)
        if valoare_tranzactie_initiala != valoare_tranzactie:
            reducere = float(valoare_tranzactie_initiala) \
                       - float(valoare_tranzactie)
        else:
            reducere = float(0)
        tranzactie = Tranzactie(id_tranzactie,
                                id_medicament,
                                id_card,
                                nr_bucati,
                                data_tranzactie,
                                ora_tranzactie,
                                valoare_tranzactie,
                                reducere)
        self.tranzactie_repository.create(tranzactie)

    def update_tranzactie(self,
                          id_tranzactie: str,
                          id_medicament: str,
                          id_card: str,
                          nr_bucati: str,
                          data_tranzactie,
                          ora_tranzactie,
                          valoare_tranzactie,
                          reducere):

        tranzactie = Tranzactie(id_tranzactie,
                                id_medicament,
                                id_card,
                                nr_bucati,
                                data_tranzactie,
                                ora_tranzactie,
                                valoare_tranzactie,
                                reducere)
        self.tranzactie_repository.update(tranzactie)

    def delete_tranzactie(self, id_tranzactie: int):
        self.tranzactie_repository.delete(id_tranzactie)

    def get_all(self) -> List[Tranzactie]:
        return self.tranzactie_repository.read()

    def get_transactions_between_dates(self):
        results = []
        try:
            d1, m1, y1 = [int(x) for x in input("Introdu stanga intervalului:"
                                                "(DD/MM/YYYY) : ").split('/')]
            b1 = datetime.date(y1, m1, d1)

            d2, m2, y2 = [int(x) for x in input("Introdu dreapta intervalului:"
                                                "(DD/MM/YYYY) : ").split('/')]
            b2 = datetime.date(y2, m2, d2)

            for tr in self.tranzactie_repository.read():
                if tr.data_tranzactie > b1 and tr.data_tranzactie < b2:
                    results.append \
                        (TransactionsBetweenTwoDates(tr.id_entity,
                                                     tr.data_tranzactie))
        except ValueError as ve:
            print('Eraore: ', ve)
        return results

    def handle_generate_random_tr(self):
        medicamente = self.medicament_repository.read()
        carduri = self.card_repository.read()
        id_uri_med = [med.id_entity for med in medicamente]
        id_uri_card = [card.id_entity for card in carduri]

        return id_uri_med, id_uri_card

    def delete_transactions_b_d(self):

        try:
            d1, m1, y1 = [int(x) for x in input("Introdu stanga intervalului:"
                                                "(DD/MM/YYYY) : ").split('/')]
            b1 = datetime.date(y1, m1, d1)

            d2, m2, y2 = [int(x) for x in input("Introdu dreapta intervalului:"
                                                "(DD/MM/YYYY) : ").split('/')]
            b2 = datetime.date(y2, m2, d2)

            for tr in self.tranzactie_repository.read():
                if tr.data_tranzactie >= b1 and tr.data_tranzactie <= b2:
                    self.tranzactie_repository.delete(tr.id_entity)

        except ValueError as ve:
            print('Eraore: ', ve)

    def sales_each_med(self):
        result = []
        medicamente = self.medicament_repository.read()
        tranzactii = self.get_all()
        for medicament in medicamente:
            bucati = [int(tranzactie.nr_bucati) for tranzactie in tranzactii
                      if int(medicament.id_entity) == int(
                    tranzactie.id_medicament)]
            result.append((medicament, sum(bucati)))
        return sorted(result, key=lambda x: x[1], reverse=True)

    def discount_each_card(self):
        result = []
        carduri = self.card_repository.read()
        tranzactii = self.tranzactie_repository.read()
        for card in carduri:
            reducere = [int(tranzactie.reducere) for tranzactie in tranzactii
                        if int(tranzactie.id_card) == int(card.id_entity)]
            result.append((card.nume_client, card.id_entity, sum(reducere)))
        return sorted(result, key=lambda x: x[2], reverse=True)

    def waterfall_delete(self):
        id = int(input('Dati ID-ul medicamentului ce va fi sters: '))
        for tranzactie in self.get_all():
            if int(tranzactie.id_medicament) == int(id):
                self.tranzactie_repository.delete(tranzactie.id_entity)
        self.medicament_repository.delete(id)
