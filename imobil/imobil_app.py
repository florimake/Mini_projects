from classes_imobil import Imobil

blocul1 = Imobil("B5", 33)
print(blocul1)

blocul1.vanzare(2, 12, "Florinel Huciog")
print(blocul1.lista_locatari())

blocul1.vanzare(2, 10, "Arpad florinel")
blocul1.vanzare(2, 7, "Huciog Arpad")
blocul1.vanzare(2, 5, "Nicoale Nicu")
blocul1.vanzare(2, 18, "Alexandru Catalin")
blocul1.vanzare(1, 23, "Costel Costi")
print(blocul1)

print(blocul1.lista_locatari())
blocul1.cautare(7)

blocul1.sterge_locatar(23)
blocul1.schimba_locatar(10, "Florinel Arpad")

blocul1.sterge_locatar(18)
print(blocul1.lista_locatari())
print(blocul1)
