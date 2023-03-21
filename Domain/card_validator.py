from Domain.card_client import Card


class CardValidator:

    def validate(self, card: Card):
        if len(card.CNP) != 13:
            raise ValueError('CNP-ul nu are lungimea corecta')
