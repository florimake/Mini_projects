import random
from number import Lotto, LotoRomania, LotoItalia, LotoPolonia, Jucator

'''
folder Lotto
Creati o clasa care va genera un numar random de la 1 la 49. (number.py)
folositi modulul random
'''

l = Lotto(4, 10)
r = LotoRomania()
i = LotoItalia()

lotto = LotoItalia()
j = Jucator(l)

j.alegeNumere([19,1,5,21,6,8,12])
print(j)

extragere = r.extragere_v3()
print(f"Au fost extrase {extragere}")

def nr_castigatoare(jucate, extrase):
    return set(jucate) & set(extrase)

print(f"Jucatorul a ghicit : {nr_castigatoare(j.nr_alese, extragere)}")
