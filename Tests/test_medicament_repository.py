from Domain.medicament import Medicament
from Repository.json_repository import JsonRepository
from utils import clear_file


def test_medicament_repository():
    filename = 'test_medicamente.json'
    clear_file(filename)
    medicament_repository = JsonRepository(filename)
    added = Medicament('1', 'Paracetamol', 'Terapia', 5, 'nu')
    medicament_repository.create(added)
    assert medicament_repository.read(added.id_entity) == added
