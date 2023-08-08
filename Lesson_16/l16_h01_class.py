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

    PIN_MAX_SIZE = 4
    BANK_ID = 5375

    def __init__(self, card_num, cvv, pin, name, surname, end_date):
        """Initialize class."""
        self._card_num = card_num
        self.__cvv = cvv
        self.__pin = pin
        self._name = name
        self._surname = surname
        self._end_date = end_date
        self._lvl_card = 'Universal'

    @property
    def card_num(self):
        """Get the card number."""
        return self._card_num

    @card_num.setter
    def card_num(self, new_card_num):
        """Set the card number."""
        self._card_num = new_card_num

    @property
    def cvv(self):
        """Get the CVV."""
        return self.__cvv

    @property
    def pin(self):
        """Get the PIN."""
        return self.__pin

    @pin.setter
    def pin(self, new_pin):
        """Set the PIN."""
        if len(new_pin) == MonoBankCard.PIN_MAX_SIZE:
            self.__pin = new_pin
        else:
            print(f'PIN should be {MonoBankCard.PIN_MAX_SIZE} size.')

    def block_card(self):
        """Block the card."""
        print('Card is blocked.')

    def pay(self, amount):
        """Make a payment."""
        print(f'Payment of ${amount}.')

    @classmethod
    def get_bank_id(cls):
        """Get the bank ID."""
        return cls.BANK_ID

    @staticmethod
    def validate_card_number(card_num):
        """Validate the card number."""
        if len(card_num) == 16 and card_num.isnumeric():
            return True
        return False


if __name__ == '__main__':
    new_card = MonoBankCard('5678606571345678', 911, '4561',
                            'Daniel', 'Craig', '12/29')

    # Getters
    print(new_card.card_num)
    print(new_card.cvv)
    print(new_card.pin)

    # Setters
    new_card.card_num = '5678090985431209'
    new_card.pin = '5178'

    print(new_card.card_num)
    print(new_card.pin)

    # Block the card
    new_card.block_card()

    # Make a payment
    new_card.pay(100)

    # Validate a card number
    print(MonoBankCard.
          validate_card_number(new_card.card_num))  # Should print False

    # Display card information
    print(new_card.__dict__)
