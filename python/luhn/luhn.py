class Luhn:
    card = 0
    def __init__(self, card_num):
        self.card = card_num

    def valid(self):
        self.card = self.card.replace(" ", "")
        if len(self.card) <= 1:
            return False
        for x in self.card:
            if not x.isdigit():
                return False
        self.card = ''.join(x for x in self.card if x.isdigit())
        cleaned = list(self.card)
        i = len(cleaned)-2
        while i >= 0:
            cleaned[i] = int(cleaned[i]) * 2
            if cleaned[i] > 9:
                cleaned[i] -= 9
            i -= 2
        sum = 0
        for ind in cleaned:
            sum += int(ind)
        return sum % 10 == 0
