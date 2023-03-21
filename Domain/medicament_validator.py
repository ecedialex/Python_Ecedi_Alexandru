from Domain.medicament import Medicament


class MedicamentValidator:

    def validate(self, medicament: Medicament):
        if int(medicament.pret_medicament) <= 0:
            raise ValueError('Pretul trebuie sa fie strict pozitiv')
        valid_retete = ['da', 'nu']
        if medicament.necesita_reteta not in valid_retete:
            raise ValueError(
                f'Campul necesita reteta trebuie sa contina : {valid_retete}')
