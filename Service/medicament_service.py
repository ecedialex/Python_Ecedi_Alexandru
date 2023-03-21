from typing import List

from Domain.medicament import Medicament
from Domain.medicament_validator import MedicamentValidator
from Repository.repository import Repository


class MedicamentService:
    def __init__(self,
                 medicament_repository: Repository,
                 medicament_validator: MedicamentValidator):
        self.medicament_repository = medicament_repository
        self.medicament_validator = medicament_validator

    def add_medicament(self,
                       id_medicament,
                       nume_medicament,
                       producator_medicament,
                       pret_medicament,
                       necesita_reteta):
        """
        Verifica si adauga un medicament in lista daca este valid
        :param id_medicament: id-ul medicamentului
        :param nume_medicament: numele medicamentului
        :param producator_medicament: producatorul medicamentului
        :param pret_medicament: pretul medicamentului
        :param necesita_reteta: se specifica daca medicamentul necesita reteta
        :return: fisierul medicamente cu lista de medicamente
        """
        medicament = Medicament(id_medicament,
                                nume_medicament,
                                producator_medicament,
                                pret_medicament,
                                necesita_reteta)

        self.medicament_validator.validate(medicament)
        self.medicament_repository.create(medicament)

    def update_medicament(self,
                          id_medicament,
                          nume_medicament,
                          producator_medicament,
                          pret_medicament,
                          necesita_reteta):

        medicament = Medicament(id_medicament,
                                nume_medicament,
                                producator_medicament,
                                pret_medicament,
                                necesita_reteta)

        self.medicament_validator.validate(medicament)
        self.medicament_repository.update(medicament)

    def delete_medicament(self, id_medicament: str):
        self.medicament_repository.delete(id_medicament)

    def get_all(self) -> List[Medicament]:
        return self.medicament_repository.read()

    def get_id(self, id):
        return self.medicament_repository.read(id)

    def get_pret(self, id):
        medicamente = self.get_all()
        for medicament in medicamente:
            print(medicament)
            if medicament.id_entity == int(id):
                return medicament.pret_medicament

    def full_text_search_medicament(self, text):
        medicamente = self.get_all()
        result = []

        for medicament in medicamente:
            if text.lower() in str(medicament.id_entity):
                result.append(medicament)
            elif text.lower() in medicament.nume_medicament.lower():
                result.append(medicament)
            elif text.lower() in medicament.producator_medicament.lower():
                result.append(medicament)
            elif text.lower() in str(medicament.pret_medicament).lower():
                result.append(medicament)
            elif text.lower() in medicament.necesita_reteta.lower():
                result.append(medicament)
        return result

    def price_increase(self):
        procent = int(input('Dati procentul de crestere a pretului: '))
        pret_minim = int(
            input('Dati pretul minim pentru aplicarea reducerii: '))
        medicamente = self.get_all()
        for medicament in medicamente:
            if int(medicament.pret_medicament) <= int(pret_minim):
                pret = int(medicament.pret_medicament)
                pret_nou = (pret + ((pret * procent) / 100))
                self.update_medicament(medicament.id_entity,
                                       medicament.nume_medicament,
                                       medicament.producator_medicament,
                                       pret_nou,
                                       medicament.necesita_reteta)

        return medicamente
