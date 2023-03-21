from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Medicament(Entity):
    """
    Creeaza entitatea medicament
    """
    nume_medicament: str
    producator_medicament: str
    pret_medicament: int
    necesita_reteta: str
