from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Tranzactie(Entity):
    """
    Creeaza entitatea tranzactie
    """
    id_medicament: str
    id_card: str
    nr_bucati: str
    data_tranzactie: str
    ora_tranzactie: str
    valoare_tranzactie: float
    reducere: float
