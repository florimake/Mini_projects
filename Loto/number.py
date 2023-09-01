from random import randint, choice


# hello = "La multi ani 2023 !"
# curs = "OOP"

class Lotto:
    def __init__(self, len_extrase, len_posibile):
        self.len_extrase = len_extrase
        self.len_posibile = len_posibile

    def extragere_v1(self):
        return [randint(1, self.len_posibile) for i in range(self.len_extrase)]

    def extragere_v2(self):
        nr_extrase = set()
        while len(nr_extrase) < self.len_extrase:
            nr_extrase.add(randint(1, self.len_posibile))
        return nr_extrase

    def extragere_v3(self):
        nr_posibile = list(range(1, self.len_posibile+1))
        nr_extrase = []
        for _ in range(self.len_extrase):
            nr_extras = choice(nr_posibile)
            nr_posibile.remove(nr_extras)
            nr_extrase.append(nr_extras)
        return nr_extrase

class LotoRomania(Lotto):
    def __init__(self):
        super().__init__(6,49)

class LotoItalia(Lotto):
    def __init__(self):
        super().__init__(6, 90)

class LotoPolonia(Lotto):
    def __init__(self):
        super().__init__(20, 80)

class Jucator:
    def __init__(self, lotto):
        self.nr_jucate = lotto.len_extrase
        self.nr_posibile = lotto.len_posibile
        self.nr_alese = set()

    def __str__(self):
        return f"Jucatorul a ales {list(self.nr_alese)} la loto {self.nr_jucate} din {self.nr_posibile}"

    def alegeNumere(self, nr):
        self.nr_alese = nr
        while len(self.nr_alese) < self.nr_jucate:
            nr_introdus = input(f"Adaugati un nou numar, ati ales deja {list(self.nr_alese)}")
            if nr_introdus.isnumeric() and 1 <= int(nr_introdus) <= self.nr_posibile:
                self.nr_alese.add(int(nr_introdus))