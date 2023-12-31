#Importarea modulului necesar operatiilor matematice avansate
import math
import datetime

#Bucla while pentru a executa programul fara intrerupere si a permite utilizatorului sa se intoarca in meniu si sa aleaga o alta optiune
while True:
    #Utilizatorul alege operatia matematica pe care o doreste din meniu (folosim \n pentru introducerea unui nou rand)
    print("\nSelecteaza operatia matematica dorita.\n\n0 - Adunare\n1 - Scadere\n2 - Inmultire\n3 - Impartire\n4 - Modulo\n5 - Ridicare la putere\n6 - Radical\n7 - Sinus\n8 - Cosinus\n9 - Tangenta\n10 - Logaritm in baza 2\n11 - Metri cubi\n12 - Metri patrati\n13 - Introduce Aria si afla perimetru si laturile unui patrat perfect")

    oper = input("\nOptiunea ta: ") #Variabila care stocheaza valoarea aleasa de utilizator

    #Adunare
    if oper == "0":
        val1 = float(input("\nPrima valoare: ")) #Variabila care stocheaza prima valoare introdusa, convertita din string in float
        val2 = float(input("\nA doua valoare: ")) #Variabila care stocheaza a doua valoare introdusa, convertita din string in float

        print("\nRezultatul este: " + str(val1 + val2) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')

        if inapoi == 'y':
            continue
        else:
            break

    #Scadere
    elif oper == "1":
        val1 = float(input("\nPrima valoare: "))
        val2 = float(input("\nA doua valoare: "))

        print("\nRezultatul este: " + str(val1 - val2) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')

        if inapoi == 'y':
            continue
        else:
            break

    #Inmultire
    elif oper == "2":
        val1 = float(input("\nPrima valoare: "))
        val2 = float(input("\nA doua valoare: "))

        print("\nRezultatul este: " + str(val1 * val2) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')

        if inapoi == 'y':
            continue
        else:
            break

    #Impartire
    elif oper == "3":
        val1 = float(input("\nPrima valoare: "))
        val2 = float(input("\nA doua valoare: "))

        print("\nRezultatul este: " + str(val1 / val2) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')

        if inapoi == 'y':
            continue
        else:
            break

    #Modulo
    elif oper == "4":
        val1 = float(input("\nPrima valoare: "))
        val2 = float(input("\nA doua valoare: "))

        print("\nRezultatul este: " + str(val1 % val2) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')

        if inapoi == 'y':
            continue
        else:
            break

    #Ridicare la putere
    elif oper == "5":
        val1 = float(input("\nValoarea bazei: "))
        val2 = float(input("\nValoarea exponentului: "))

        print("\nRezultatul este: " + str(math.pow(val1, val2)) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')

        if inapoi == 'y':
            continue
        else:
            break

    #Radical
    elif oper == "6":
        val1 = float(input("\nIntroduceti valoarea pentru extragerea radicalului: "))

        print("\nRezultatul este: " + str(math.sqrt(val1)) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')

        if inapoi == 'y':
            continue
        else:
            break

    #Sinus
    elif oper == "7":
        val1 = float(input("\nIntroduceti valoarea (in grade) pentru calcularea sinus: "))

        print("\nRezultatul este: " + str(math.sin(math.radians(val1))) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')

        if inapoi == 'y':
            continue
        else:
            break

    #Cosinus
    elif oper == "8":
        val1 = float(input("\nIntroduceti valoarea (in grade) pentru calcularea cosinus: "))

        print("\nRezultatul este: " + str(math.cos(math.radians(val1))) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')

        if inapoi == 'y':
            continue
        else:
            break

    #Tangenta
    elif oper == "9":
        val1 = float(input("\nIntroduceti valoarea (in grade) pentru calcularea tangentei: "))

        print("\nRezultatul este: " + str(math.tan(math.radians(val1))) + "\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')

        if inapoi == 'y':
            continue
        else:
            break

   #Logaritm in baza 2
    elif oper == "10":
        val1 = float(input("\nIntroduceti valoarea (numar) pentru calculare in baza 2: "))

        print(f"\nRezultatul este: {val1**2}\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')

        if inapoi == 'y':
            continue
        else:
            break

    # Metri cubi
    elif oper == "11":
        h = float(input("\nIntroduceti inaltimea (metri) : "))
        l = float(input("\nIntroduceti lungime (metri) :  "))
        l2 = float(input("\nIntroduceti latime (metri) : "))

        print(f"\nRezultatul este: {l*l2*h}\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')

        if inapoi == 'y':
            continue
        else:
            break
    
    # Metri patrati Aria to perimetru si laturile unui patrat
    elif oper == "12":
        l = float(input("\nIntroduceti lungime (metri) :  "))
        l2 = float(input("\nIntroduceti latime (metri) : "))

        print(f"\nRezultatul este: {l*l213}\n")

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')

        if inapoi == 'y':
            continue
        else:
            break
        
    # Aria to perimetru si laturile unui patrat
    elif oper == "13":
        aria = float(input("\nIntroduceti aria (metri) :  "))
        print("Aria Patratului:",aria,"m^2\n")
        print(f"\nPerimetrul este: {(aria ** 0.5)*4} m")
        print(f"\nlatura patratului este: {aria ** 0.5} m")
        # print(f"\nlatura patratului este: {math.sqrt(aria)} m") # varianta 2

        #Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nMergi inapoi in meniul principal? (y/n) ')

        if inapoi == 'y':
            continue
        else:
            break

	#Tratarea optiunilor invalide
    else:
        print(f"\n{datetime.datetime.now()} >>> Optiune invalida!\n")

        #utilizatorul a introdus obtiunea invalida "numar" la data si ora : "data", "ora"
        #salvare data si ora intrun fisier extern invalid input.txt
        
        # with open("input.txt", "w") as file:
        #     file.write(f" utilizatorul a introdus obtiunea invalida {oper} la data si ora : {datetime.datetime.now()}")
             

		#Intoarcere la meniul principal sau iesirea din program
        inapoi = input('\nDoresti sa continui? (y/n) ')
        if inapoi == 'y':
            continue
        else:
            break

#Finalul programului4








