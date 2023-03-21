import datetime
import random
import uuid
import names
from Service.card_service import CardService
from Service.medicament_service import MedicamentService
from Service.tranzactie_service import TranzactieService


class Console:
    def __init__(self,
                 medicament_service: MedicamentService,
                 card_service: CardService,
                 tranzactie_service: TranzactieService):

        self.medicament_service = medicament_service
        self.card_service = card_service
        self.tranzactie_service = tranzactie_service

    def show_menu(self):
        print('a[med|card|tr] - adaugare medicament/card client/tranzactie')
        print('u[med|card|tr] - actualizare medicament/card client/tranzactie')
        print('r[med|card|tr] - stergere medicament/card client/tranzactie')
        print(
            's[med|card|tr] - afisare toate medicamente'
            '/carduri client/tranzactii')
        print('fts            - full text search')
        print('generatemed    -genereaza n medicamente')
        print('generatecard   -genereaza n carduri')
        print('generatetr     -genereaza n tranzactii')
        print('sortedbysales  - afisare medicamente ordonate '
              'dupa numarul de vanzari')
        print('sortedbydiscount - ordonarea'
              ' descrescatoare a cardurilor de client'
              'dupa valoarea reducerilor obtinute ')
        print('bdates         - afisare tranzactii intre doua date')
        print('increase      - Scumpirea cu un procentaj dat '
              'a tuturor medicamentelor cu prețul '
              'mai mic decât o valoare data')
        print('deldates      -Ștergerea tuturor tranzacțiilor'
              ' dintr-un anumit interval de zile.')
        print('x - inchidere program')

    def handle_add_medicament(self):
        try:
            id_medicament = input()
            nume_medicament = input('Dati numele'
                                    ' medicamentului: ')
            producator_medicament = input('Dati numele'
                                          ' producatorului: ')
            pret_medicament = input('Dati pretul '
                                    'medicamentului: ')
            necesita_reteta = input('Specificati daca '
                                    'medicamentul necesita reteta'
                                    ' : [da/nu]: ')
            self.medicament_service.add_medicament(id_medicament,
                                                   nume_medicament,
                                                   producator_medicament,
                                                   pret_medicament,
                                                   necesita_reteta)
        except ValueError as ve:
            print('Eroare de validare :', ve)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_show_all(self, objects):
        for obj in objects:
            print(obj)

    def handle_add_card(self):
        try:
            id_card = input()
            nume_client = input('Dati numele clientului: ')
            prenume_client = input('Dati prenumele clientului: ')
            CNP = input('Dati CNP-ul clientului: ')
            d, m, y = [int(x) for x in input('Introduceti '
                                             'data nasterii : DD/MM/YYYY :'
                                             ' ').split('/')]
            data_nasterii = datetime.date(y, m, d)
            data_inregistrarii = input('Dati data '
                                       'inregistrarii clientului: ')
            self.card_service.add_card(id_card,
                                       nume_client,
                                       prenume_client,
                                       CNP, data_nasterii,
                                       data_inregistrarii)
        except ValueError as ve:
            print('Eroare de validare :', ve)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_add_tranzactie(self):
        try:
            id_tranzactie = input()
            id_medicament = input('Dati id-ul medicamentului : ')
            id_card = input('Dati id-ul cardului clientului : ')
            nr_bucati = input('Dati numarul de bucati cumparate : ')
            d, m, y = [int(x) for x in input('Introduceti '
                                             'data nasterii : DD/MM/YYYY :'
                                             ' ').split('/')]
            data = datetime.date(y, m, d)
            ora = input('Dati ora tranzactiei: ')
            valoare_tranzactie = int(nr_bucati)
            reducere = 0
            self.tranzactie_service.add_tranzactie(id_tranzactie,
                                                   id_medicament,
                                                   id_card,
                                                   nr_bucati,
                                                   data,
                                                   ora,
                                                   valoare_tranzactie,
                                                   reducere)
        except ValueError as ve:
            print('Eroare de validare :', ve)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_update_medicament(self):
        try:
            id_medicament = input('Dati id-ul medicamentului: ')
            nume_medicament = input('Dati numele medicamentului: ')
            producator_medicament = input('Dati numele producatorului: ')
            pret_medicament = input('Dati pretul medicamentului: ')
            necesita_reteta = input('Specificati daca medicamentul '
                                    'necesita reteta : [da/nu]: ')
            self.medicament_service.update_medicament(id_medicament,
                                                      nume_medicament,
                                                      producator_medicament,
                                                      pret_medicament,
                                                      necesita_reteta)
        except ValueError as ve:
            print('Eroare de validare :', ve)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_update_card(self):
        try:
            id_card = input('Dati id-ul cardului: ')
            nume_client = input('Dati numele clientului: ')
            prenume_client = input('Dati prenumele clientului: ')
            CNP = input('Dati CNP-ul clientului: ')
            data_nasterii = input('Dati data nasterii a clientului: ')
            data_inregistrarii = input('Dati data inregistrarii clientului: ')
            self.card_service.update_card(id_card,
                                          nume_client,
                                          prenume_client,
                                          CNP, data_nasterii,
                                          data_inregistrarii)
        except ValueError as ve:
            print('Eroare de validare :', ve)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_update_tranzactie(self):
        try:
            id_tranzactie = input('Dati id-ul tranzactiei : ')
            id_medicament = input('Dati id-ul medicamentului : ')
            id_card = input('Dati id-ul cardului clientului : ')
            nr_bucati = input('Dati numarul de bucati cumparate : ')
            data = input('Dati ora efectuarii tranzactiei : ')
            ora = input('Dati data efectuarii tranzactiei : ')
            pret = (int(nr_bucati) *
                    int(self.medicament_service.get_pret(id_medicament)))
            self.tranzactie_service.update_tranzactie(id_tranzactie,
                                                      id_medicament,
                                                      id_card,
                                                      nr_bucati,
                                                      ora,
                                                      data,
                                                      pret,
                                                      0)
        except ValueError as ve:
            print('Eroare de validare :', ve)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_remove_medicament(self):
        try:
            id_medicament = input('Dati id-ul '
                                  'medicamentului ce va fi sters:')
            self.medicament_service.delete_medicament(id_medicament)
        except ValueError as ve:
            print('Eroare de validare :', ve)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_remove_card(self):
        try:
            id_card = input('Dati id-ul cardului ce va fi sters:')
            self.card_service.delete_card(id_card)
        except ValueError as ve:
            print('Eroare de validare :', ve)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_remove_tranzactie(self):
        try:
            id_tranzactie = \
                input('Dati id-ul tranzactiei ce va fi stearsa:')
            self.tranzactie_service.delete_tranzactie(id_tranzactie)
        except ValueError as ve:
            print('Eroare de validare :', ve)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_full_text_search(self):
        text = input('Introduceti textul: ')
        fts1 = self.medicament_service.full_text_search_medicament(text)
        r1 = self.handle_show_all(fts1)
        fts2 = self.card_service.full_text_search_card(text)
        r2 = self.handle_show_all(fts2)
        if r1 is not None:
            print(r1)
        if r2 is not None:
            print(r2)

    def handle_generate_random_med(self):
        n = int(input('Introduceti numarul de medicamente '
                      'ce se vor genera: '))
        i = 1
        while i <= n:
            id_medicament = int(uuid.uuid4())
            nume_medicament = random.choice(['Zovirax', 'Paracetamol',
                                             'Nurofen', 'Vitamica C',
                                             'Complex de vitamine'])
            producator_medicament = random.choice(['Terapia', 'Pfizer',
                                                   'Moderna', 'Johnson',
                                                   'Roche', 'Novartis'])
            pret_medicament = random.randint(1, 500)
            necesita_reteta = random.choice(['da', 'nu'])
            self.medicament_service.add_medicament(id_medicament,
                                                   nume_medicament,
                                                   producator_medicament,
                                                   pret_medicament,
                                                   necesita_reteta)
            i = i + 1

    def handle_generate_random_card(self):
        n = int(input('Introduceti numarul de carduri ce se vor genera: '))
        for i in range(0, n):
            id_card = int(uuid.uuid4())
            nume_client = names.get_full_name()
            prenume_client = names.get_last_name()
            CNP = str(random.randint(1000000000000,
                                     9999999999999))
            d, m, y = random.randint(1, 28), \
                      random.randint(1, 12), \
                      random.randint(2000, 2021)
            data_nasterii = datetime.date(y, m, d)
            data_inregistrarii = datetime.date.today()
            self.card_service.add_card(id_card,
                                       nume_client,
                                       prenume_client,
                                       CNP,
                                       data_nasterii,
                                       data_inregistrarii)

    def handle_generate_random_tr(self):
        n = int(input('Introduceti numarul de'
                      ' tranzactii ce se vor genera: '))
        iduri_med, iduri_card = \
            self.tranzactie_service.handle_generate_random_tr()
        for i in range(0, n):
            id_tranzactie = random.randint(1, 10000)
            id_medicament = int((random.choice(iduri_med)))
            id_card = int((random.choice(iduri_card)))
            nr_bucati = random.randint(1, 100)
            d, m, y = random.randint(1, 31), \
                      random.randint(1, 12), \
                      random.randint(2000, 2021)
            data = datetime.date(y, m, d)
            ora = random.randint(0, 23)
            valoare_tranzactie = 0
            self.tranzactie_service.add_tranzactie(
                id_tranzactie,
                id_medicament,
                id_card,
                nr_bucati,
                data, ora,
                valoare_tranzactie, 0)

    def run_console(self):
        while True:
            self.show_menu()
            opt = input('Alegeti optiunea: ')
            if opt == 'amed':
                self.handle_add_medicament()
            elif opt == 'acard':
                self.handle_add_card()
            elif opt == 'atr':
                self.handle_add_tranzactie()
            elif opt == 'umed':
                self.handle_update_medicament()
            elif opt == 'ucard':
                self.handle_update_card()
            elif opt == 'utr':
                self.handle_update_tranzactie()
            elif opt == 'rmed':
                self.handle_remove_medicament()
            elif opt == 'rcard':
                self.handle_remove_card()
            elif opt == 'rtr':
                self.handle_remove_tranzactie()
            elif opt == 'smed':
                self.handle_show_all(self.medicament_service.get_all())
            elif opt == 'scard':
                self.handle_show_all(self.card_service.get_all())
            elif opt == 'str':
                self.handle_show_all(self.tranzactie_service.get_all())
            elif opt == 'bdates':
                self.handle_show_all(self.tranzactie_service.
                                     get_transactions_between_dates())
            elif opt == 'fts':
                self.handle_full_text_search()
            elif opt == 'generatemed':
                self.handle_generate_random_med()
            elif opt == 'generatecard':
                self.handle_generate_random_card()
            elif opt == 'generatetr':
                self.handle_generate_random_tr()
            elif opt == 'waterfall':
                self.tranzactie_service.waterfall_delete()
            elif opt == 'increase':
                self.handle_show_all(self.medicament_service.price_increase())
            elif opt == 'deldates':
                self.tranzactie_service.delete_transactions_b_d()
            elif opt == 'sortedbysales':
                self.handle_show_all(self.tranzactie_service.sales_each_med())
            elif opt == 'sortedbydiscount':
                self.handle_show_all(
                    self.tranzactie_service.discount_each_card())
            elif opt == 'x':
                break
            else:
                print('Optiune invalida,reincercati!')
