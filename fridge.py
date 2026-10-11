from decimal import Decimal
from datetime import datetime


goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal(
            '0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}


def add(items, title, amount, expiration_date=None):


def add_by_note(items, note):


def finde(items, needle):


def amount(items, needle):


def expire(items, in_advance_days=0):

