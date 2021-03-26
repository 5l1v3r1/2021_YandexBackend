class PearsBasket:
    """
    Класс PearsBasket, экземпляр которого при инициализации получает целое число – количество груш в корзине.
    """

    def __init__(self, pearsCount):
        self.pearsCount = pearsCount

    def __str__(self):
        """
        __str__ – возвращает количество груш в корзине
        """
        return self.pearsCount

    def __repr__(self):
        """
        __repr__ – возвращает строку в формате PearsBasket(<количество>)
        """
        return f"PearsBasket('{self.pearsCount}')"

    def __add__(self, other):
        """
        pb_1 + pb_2 – складываются две корзинки
        """
        return other + self.pearsCount

    def __sub__(self, other):
        """
        pb_1 - n – число вычитается из корзинки, если там есть такое количество груш, если нет – вычитается сколько есть, остается 0
        """
        pass

    def __floordiv__(self, other):
        """
        pb // n – деление нацело, возвращает список объектов класса со значениями количества груш в каждой корзинке,
        если есть остаток – он должен находиться в дополнительной последней корзинке.
        """
        pass

    def __mod__(self, other):
        """
        pb % n – получение остатка от деления, возвращает число: остаток от деления.
        """
        pass
