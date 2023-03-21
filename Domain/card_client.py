from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Card(Entity):
    """
    Creeaza entitatea card_client
    """
    nume_client: str
    prenume_client: str
    CNP: str
    data_nasterii: str
    data_inregistrarii: str
