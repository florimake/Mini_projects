import os
import rsa

class PassManager:
    def __init__(self, file, app = '', password = ''):
        self.file = file
        self.app = app
        self.password = password


        #Cu libraria os
        #verific daca fisierul care este dat ca parametru in __init__ exista, daca nu o sa creeze acest fisier, il deschidem dar nu scriem nimic in el
        if os.path.exists(self.file) == False:
            with open(self.file, 'w') as f:
                pass


    #memniu, daca nu folosesc deloc instanta self se poate scoate si folosi decoratorul @staticmethod
    @staticmethod
    def menu():
        option = ''
        while option != '1' and option != '2' and option != '3':
            option =input('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n'
                          '1. Salveaza o parola\n'
                          '2. Alege aplicatia pentru care sa vezi parola\n'
                          '3. Vezi toateparolele\n'
                          '▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n'
                          'Alege o optiune: ')
        return option

    #introduce numele aplicatiei
    def input_app(self):
        self.app = input('Introduceti aplicatia: ')

    #introducere parola
    def input_password(self):
        self.password = input('Introduceti parola: ')


    #scriere in fisier
    def write_to_file(self, mode, content):
        with open(self.file, mode) as fw:
            fw.write(content)

    # citire din fisier
    def read_from_file(self, mode, whole = False):
        if whole == False:
            with open(self.file, mode) as fr:
                file_content = fr.readlines()
                return  file_content

        with open(self.file, mode) as fr:
            file_content = fr.read()
            return file_content

    # salfarea datelor in fisier
    def save_data_to_file(self):
        file_content = self.read_from_file('r', whole=True)
        if self.app in file_content:
            print('Aplicatia exista in fisier')
        else:
            self.write_to_file('a', f"{self.app}: {self.password}\n")


    #pentru a decripta si a cripta avem nevoie de biblioteca rsa
    # criptarea fisierului presupune existenta unei chei publice
    def encrypt_file(self):
        #vom genera perechea de key cu metoda newkeys si in parantesa numarul de biti
        pubkey, privkey = rsa.newkeys(1024)
        #salvex aceste fisiere keys intr-un folder keys cu extensia .pem
        # save_pkcs1('PEM') este o metoda din rsa care salveaza un format specific
        with open('keys/public.pem', "wb") as fw:
            fw.write(pubkey.save_pkcs1("PEM"))
        with open('keys/PRIVATE.pem', "wb") as fw:
            fw.write(privkey.save_pkcs1("PEM"))

        #citim fisierul pentru al cripta
        content = self.read_from_file('r', whole=True)
        enc_content = rsa.encrypt(content.encode('utf-8'), pubkey) #utf-8 inseamna ca este codat pe 8 biti

        #salvam continutul criptat inapoi in fisier
        self.write_to_file("wb", enc_content)


    # decriptarea fisierului presupune existenta unei chei private si poate fi decriptat doar de catre cel ccare are aceasta cheie
    def decrypt_file(self):
        #verificam daca fisierul exista si are continut daca nu
        if os.path.exists(self.file) and os.path.getsize(self.file) > 0:
            with open("keys/PRIVATE.pem", "rb") as fr:
                priv_key = rsa.PrivateKey.load_pkcs1(fr.read())

            content = self.read_from_file('rb', whole=True)
            decrypted_content = rsa.decrypt(content, priv_key)

            self.write_to_file('w', decrypted_content.decode('utf-8'))



pm = PassManager('password_manager_file.txt')


option = ''

pm.decrypt_file()


pm.decrypt_file()
while option.upper() != 'Y':
    option = pm.menu()

    if option == '1':
        pm.input_app()
        pm.input_password()
        pm.save_data_to_file()
    elif option == '2':
        pm.input_app()
        file_content = pm.read_from_file('r', whole=False)
        print('▬'* 28)
        for line in file_content:
            if pm.app in line:
                print(line.strip())
        print('▬' * 28)
    elif option == '3':
        print('▬' * 28)
        file_content = pm.read_from_file('r', whole=True)
        print(file_content.strip())  #strip() sterge spatiile goale de la inceput si de la sfarsitul srtringului
        print('▬' * 28)

    option = input("Vrei sa iesi? [Y/N] : ")
    if option.upper() == "Y":
        pm.encrypt_file()















