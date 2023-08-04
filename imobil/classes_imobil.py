import random


class Imobil:
    AP = 30
    LOCATARI = dict()
    APV = []

    def __init__(self, numar, ap):
        self.numar = numar
        Imobil.AP = ap

    def vanzare(self, scara, ap_no, proprietar):
        self.scara = scara
        self.ap_no = ap_no
        self.proprietar = proprietar
        if self.ap_no not in Imobil.APV and int(self.ap_no) <= Imobil.AP:
            Imobil.AP -= 1
            Imobil.LOCATARI[str(self.ap_no)] = str(self.proprietar)
            Imobil.APV.append(self.ap_no)
        elif int(self.ap_no) >= (Imobil.AP+ len(Imobil.APV)):
            print(f"\n{'*'*75}\nNu sa putut face inregistrarea!!!\nApartamentul cu numarul {self.ap_no} "
                  f"nu trebuie sa depaseasca {Imobil.AP + len(Imobil.APV)}\n{'*'*75}\n")
        else:
            print(f"\n{'*'*75}\nNu sa putut face inregistrarea!!!\nApartamentul cu numarul {self.ap_no} "
                  f"a mai fost vandut o data locatarului {Imobil.LOCATARI[str(self.ap_no)]} !!!\n{'*'*75}\n")

    # @staticmethod
    def lista_locatari(self):
        print("\n- Lista cu locatari -")
        for x, y in Imobil.LOCATARI.items():
            print(f"Scara {self.scara} - apartament: {x} - Locatar: {y}")

    @staticmethod
    def lista_apartamente():
        return f"\nLista de apartamente vandute: {Imobil.APV}"

    def cautare(self, ap_no= "",proprietar= ""):
        self.ap_no = str(ap_no)
        self.proprietar = proprietar
        c = 0
        for x, y in Imobil.LOCATARI.items():
            if x == self.ap_no:
                print(f"\nApartament: {x} are locatarul: {y}")
            elif y == self.proprietar:
                print(f"\nLocatarul: {y} mai are apartamentul: {x}")
            else:
                c += 1
                if c == len(Imobil.LOCATARI):
                    print(f"Nu sa gasit: {self.ap_no}, {self.proprietar}")

    def sterge_locatar(self, ap_no):
        self.ap_no = str(ap_no)
        if int(self.ap_no) in Imobil.APV:
            # self.proprietar = proprietar
            Imobil.LOCATARI.pop(self.ap_no)
            Imobil.APV.remove(int(self.ap_no))
            print(f"\nApartamentul {self.ap_no} a fost sters !")
            Imobil.AP += 1
            # Imobil.APV.append(int(self.ap_no))
        else:
            print(f"\nNu sa putut sterge!!!\n{self.ap_no} nu se afla in lista de apartamente !!!\nIata lista: {Imobil.APV}")

    def schimba_locatar(self, ap_no, noul_nume):
        self.ap_no = str(ap_no)
        self.noul_nume = noul_nume
        v = Imobil.LOCATARI[self.ap_no]
        Imobil.LOCATARI[self.ap_no] = noul_nume
        print(f"Locatarul: {v} de la ap.{self.ap_no} sa schimbat cu {self.noul_nume}")


    def __str__(self):
        return f"\nImobilul {self.numar} mai are {Imobil.AP} ap. disponibile din {Imobil.AP + len(Imobil.APV)} de apartamente!"


# bloc1 = Imobil("105B", 38)
# print(bloc1)
# bloc1.vanzare(20, "Claudia")
# bloc1.vanzare(12, "Florin Arpad")
# bloc1.vanzare(27, "Nicolae")
# bloc1.vanzare(6, "Gabriela")
# bloc1.vanzare(2, "Mariana")
#
#
# print(bloc1.lista_locatari())
# print(bloc1.lista_apartamente())
#
# print(bloc1)
# bloc1.sterge_locatar(6)
# print(bloc1.cautare(12))
# bloc1.schimba_locatar(12, "Arpad")
#
#
# bloc1.vanzare(16, "Andrei")
# print(bloc1.lista_locatari())
# print(bloc1)
# print(bloc1.lista_apartamente())