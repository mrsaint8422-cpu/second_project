from decimal import Decimal, InvalidOperation
import datetime

DATE_FORMAT = '%Y-%m-%d'


goods = {
    'Яйца Фабрики №1': [{'amount': Decimal('1'),
                         'expiration_date': datetime.date(2026, 10, 14)}],
    'Фабрика №2: яйца': [{'amount': Decimal('2'),
                          'expiration_date': datetime.date(2026, 10, 10)},
                         {'amount': Decimal('3'),
                          'expiration_date': datetime.date(2026, 10, 12)}],
    'макароны': [{'amount': Decimal('100'), 'expiration_date': None}]
}


def add(items, title, amount, expiration_date=None):
    '''Добавляем информацию в словарь

    Информация включает в себя количество и срок годности (опционально).
    '''
    amount = Decimal(amount)

    if title not in items:
        items[title] = []

    expiration_date = datetime.datetime.strptime(
        expiration_date, DATE_FORMAT
    ).date() if expiration_date else expiration_date
    items[title].append({'amount': amount, 'expiration_date': expiration_date})


def add_by_note(items, note):
    '''Обрабатываем вводные данные.

    Функция делает все по порядку и по инструкции,
    сначала проверяет количество введенных данных,
    затем проверяет есть ли дата и после обрабатывает количество
    '''
    parts = note.split()

    if len(parts) < 2:  # Проверяем количество введеных данных.
        print(f'Ошибка: в заметке {note} недостаточно данных',
              '(нужны название и количество).')
        return

    last_part = parts[-1]
    expiration_date = None
    has_date = False

    try:  # Проверяем даты в конце строки.
        datetime.datetime.strptime(last_part, DATE_FORMAT)
        has_date = True
        expiration_date = last_part
    except ValueError:
        has_date = False

    if has_date:  # Определяем логику в зависимости от наличии даты.
        amount = parts[-2]
        title_parts = parts[:-2]
    else:
        amount = parts[-1]
        title_parts = parts[:-1]

    try:  # Конвертируем количество. При ошибке - "В значении нет числа".
        amount = Decimal(amount)
    except InvalidOperation:
        print(f'Ошибка: количество {amount} не является числом.')
        return

    title_parts = ' '.join(title_parts)
    add(items, title_parts, amount, expiration_date)


def find(items, needle):
    '''Ищем подстроку в элементах списка.'''
    result = []
    needle_lower = needle.lower()  # Выносим за цикл для оптимизации.

    for title in items:
        if needle_lower in title.lower():
            result.append(title)
    return result


def get_amount(items, needle):
    '''Обрабатываем количество найденых продуктов.'''
    product_amount = Decimal('0')

    for title in find(items, needle):
        for party in items[title]:
            product_amount += party['amount']
    return product_amount


def get_expired(items, in_advance_days=0):
    '''Проверяем продукты на истечение срока годности.

    Проверка происходит с учетом заданного числа  дней вперед.
    '''
    result = []
    today = datetime.date.today()
    deadline = today + datetime.timedelta(days=in_advance_days)

    for title, parts in items.items():
        amount = Decimal('0')
        for party in parts:
            exp_date = party['expiration_date']
            if exp_date is not None and exp_date <= deadline:
                amount += party['amount']
        if amount > 0:
            result.append((title, amount))
    return result


add_by_note(goods, 'Яйца Фабрики №1 4')
add_by_note(goods, 'Яйца деревенские 10 2026-09-04')
add(goods, 'Молоко', '1.5', '2026-10-13')
add(goods, 'Молоко', '2', '2026-12-16')
find(goods, 'яйца')
get_amount(goods, 'яйца')
print(get_expired(goods))
