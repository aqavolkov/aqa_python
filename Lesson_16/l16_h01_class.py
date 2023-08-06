"""
HW:16[Volkov Anton].

# write class for bank card.
# Class should reflect card lifecycle, card operations etc.
# use CVV, PIN, Name, Surname , end date, card_num as initial params
# class should have in addition to common logic some class attributes,
# as minimum one classmethod and
# as minimum  one staticmethod, two or more getters/setters
# do not forget about block if __name__ == '__main__':
"""


class MonoBankCard:
    """Class for creating cards."""

    _lvl_card = None

    def __init__(self, card_num, cvv, pin, name, surname, end_date):
        """Initialize class."""
        self._card_num = card_num
        self._cvv = cvv
        self._pin = pin
        self._name = name
        self._surname = surname
        self._end_date = end_date
        self._lvl_card = 'Universal'

    @classmethod
    def get_lvl_card(cls):
        """Check the level of the card."""
        return cls._lvl_card

    @staticmethod
    def max_lvl_card():
        """Return the maximum level of the card."""
        return 'Platinum'

    @property
    def card_num(self):
        """Get the card number."""
        return self._card_num

    @card_num.setter
    def card_num(self, new_card_num):
        """Set the card number."""
        self._card_num = new_card_num

    @property
    def pin(self):
        """Get the PIN."""
        return self._pin

    @pin.setter
    def pin(self, new_pin):
        """Set the PIN."""
        self._pin = new_pin


if __name__ == '__main__':
    new_card = MonoBankCard('4149606571345678', 911, '4561',
                            'Daniel', 'Craig', '12/29')
    print(new_card.__dict__)

    # Max lvl of card
    print(f'Max lvl of card: {MonoBankCard.max_lvl_card()}')

    # Getters
    print(new_card.card_num)
    print(new_card.pin)

    # Setters
    new_card.card_num = '5678090985431209'
    new_card.pin = '5178'

    print(new_card.card_num)
    print(new_card.pin)
