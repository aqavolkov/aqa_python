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

    def __init__(self, card_num, cvv, pin, name, surname, end_date, balance=0):
        """Initialize class."""
        self._card_num = card_num
        self.__cvv = cvv
        self.__pin = pin
        self._name = name
        self._surname = surname
        self._end_date = end_date
        self._lvl_card = 'Universal'
        self._balance = balance
        self._is_blocked = False

    @property
    def card_num(self):
        """Get the card number."""
        return self._card_num

    @card_num.setter
    def card_num(self, new_card_num):
        """Set the card number."""
        if self.validate_card_number(new_card_num):
            self._card_num = new_card_num
        else:
            print('Invalid card number.')

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
        if new_pin.isdigit() and len(new_pin) == MonoBankCard.PIN_MAX_SIZE:
            self.__pin = new_pin
        else:
            print(f'PIN should be {MonoBankCard.PIN_MAX_SIZE} size.')

    def block_card(self):
        """Block the card."""
        self._is_blocked = True
        print('Card is blocked.')

    def unblock_card(self):
        """Unblock the card."""
        self._is_blocked = False
        print('Card is unblocked.')

    def pay(self, amount):
        """Make a payment."""
        if not self._is_blocked and self._balance >= amount:
            self._balance -= amount
            print(f'Payment of ${amount}. Current balance: ${self._balance}')
        elif self._is_blocked:
            print('Error. Card is blocked.')
        else:
            print("Error. Don't have enough money.")

    def transfer_money(self, amount, target_card):
        """Transfer money to another card."""
        if not self._is_blocked and self._balance >= amount:
            self._balance -= amount
            target_card._balance += amount
            print(f'Transferred ${amount} to card {target_card.card_num}. '
                  f'Your balance: ${self._balance}')
        elif self._is_blocked:
            print('Error. Card is blocked.')
        else:
            print("Don't have enough money to transfer.")

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
    card1 = MonoBankCard('5375606571345678', 911, '4561', 'Daniel',
                         'Craig', '12/29', 10000)
    card2 = MonoBankCard('5375890123456789', 123, '7890', 'John',
                         'Wick', '08/25', 580)

    # Getters
    print(card1.card_num)
    print(card1.cvv)
    print(card1.pin)

    # Setters
    card1.card_num = '5375090985431209'
    card1.pin = '5178'

    print(card1.card_num)
    print(card1.pin)

    # Block the card
    card1.block_card()

    # Block the card
    card1.unblock_card()

    # Make a payment
    card1.pay(100)

    # Validate a card number
    print(MonoBankCard.validate_card_number(card1.card_num))

    # Display card information
    print(card1.__dict__)

    # Transfer money from card1 to card2
    card1.transfer_money(3002, card2)

    # Display balances
    print(f'Card 1 balance: ${card1._balance}')
    print(f'Card 2 balance: ${card2._balance}')

    # Transfer money from card2 to card1
    card2.transfer_money(888, card1)

    # Display balances
    print(f'Card 1 balance: ${card1._balance}')
    print(f'Card 2 balance: ${card2._balance}')
