# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 19:39:17 2020

@author: Pedja
"""

import Prodavci
import Kupci
import Proizvodi
import Racuni
import datetime
import matplotlib.pyplot as plt

def main():
    print()
    print("Prodavnica mesovite robe")
    print("========================")
    print()

    cmdkp = printKP()
    if cmdkp == '1':
        if not loginP():
            print("\nNiste uneli postojece ime i lozinku!")
            return
        else:
            cmdp='0'
            while cmdp != 'X':
                if cmdkp == '1':    
                    cmdp=pcmd()
                    if cmdp == '1':
                        prodaja()
                    elif cmdp=='2':
                        pretragaKupaca()
                    elif cmdp=='3':
                        noviKupac()
                    elif cmdp=='4':
                        noviProizvod()
                    elif cmdp=='5':
                        spisakProizvoda()
                    elif cmdp=='6':
                        promenaCene()
                    elif cmdp=='7':
                        novaKolicina()
                    elif cmdp=='8':
                        prodato()
                    elif cmdp=='9':
                        zarade()
                    elif cmdp=='10':
                        poVrsti()
    if cmdkp == '2':
        if not loginK():
            print("\nNiste uneli postojece ime i lozinku!")
            return
        else:
            cmdk='0'
            while cmdk != 'X':
                if cmdkp == '2':    
                    cmdk=kcmd()
                    if cmdk == '1':
                        kupovina()
                    elif cmdk=='2':
                        spisakProizvoda()
    print("Dovidjenja.")

def printKP():
    print("\nIzaberite opciju:")
    print(" 1 - Prodavac") 
    print(" 2 - Kupac")
    cmdkp = input(">> ")
    while cmdkp.upper() not in ('1', '2'):
        print("\nUneli ste pogresnu komandu.\n")
        print("\nIzaberite opciju:")
        print(" 1 - Prodavac") 
        print(" 2 - Kupac")
        cmdkp = input(">> ")
    return cmdkp.upper() 

'''
===============================================================================
                                PRODAVAC
===============================================================================
'''
def loginP():
    korIme = input("[PRODAVAC] Unesite korisnicko ime: ")
    lozinka = input("[PRODAVAC] Unesite lozinku: ")
    return Prodavci.loginP(korIme, lozinka)

def printMenuP():
    print("\n[PRODAVAC] Izaberite opciju:")
    print(" 1 - prodaja proizvoda") 
    print(" 2 - pretraga kupaca") 
    print(" 3 - unosenje novog kupca") 
    print(" 4 - unosenje novog proizvoda")
    print(" 5 - spisak proizvoda") 
    print(" 6 - promena cene proizvoda") 
    print(" 7 - dodavanje kolicine proizvoda") 
    print(" 8 - kolicina prodatih proizvoda za dan") 
    print(" 9 - zarada po danu") 
    print(" 10 - zarada po vrsti proizvoda po danu")
    print("  x - izlaz iz programa")    

def pcmd():
    printMenuP()
    cmdp = input(">> ")
    while cmdp.upper() not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'X'):
        print("\nUneli ste pogresnu komandu.\n")
        printMenuP()
        cmdp = input(">> ")
    return cmdp.upper() 

def prodaja():
    print("[PRODAVAC] - Prodaja proizvoda")
    spisakProizvoda()
    rac = {}
    rac['naziv'] = input("Unesite ime proizvoda kojeg zelite da prodate(x za kraj): ")
    while rac['naziv'] not in ('x'):
        pro = Proizvodi.findProizvod(rac['naziv'])
        if rac['naziv'] == pro['naziv']:
            rac['kolicina'] = input("Unesite kolicinu: ")
            if int(rac['kolicina']) > int(pro['kolicina']):
                print("Nema toliko proizvoda na lageru")
                print("Na lageru je dostupno", pro['kolicina'], "a vi zelite", rac['kolicina'])
            else:
                pro['kolicina'] = str(int(pro['kolicina']) - int(rac['kolicina']))
                Proizvodi.saveProizvods()
                rac['cena'] = str(int(rac['kolicina']) * int(pro['cena']))
                rac['vrsta'] = pro['vrsta']
                x = datetime.datetime.now()
                rac['datum'] = x.strftime("%x")
                Racuni.addRacun(rac)
                Racuni.saveRacuns()
                print("Uspesno ste prodali proizvod: ", rac['naziv'], "u kolicini:", rac['kolicina'])
        spisakProizvoda()
        rac = {}
        rac['naziv'] = input("Unesite ime proizvoda kojeg zelite da prodate(x za kraj): ")
    
def pretragaKupaca():
    print("[PRODAVAC] - Pretraga kupca")
    ime = input("Unesite ime >> ")
    kupList = Kupci.searchKup('ime', ime)
    if len(kupList) == 0:
        print("\nNema trazenih kupaca.")
    else:
        print('\n')
        print(Kupci.formatHeader())
        print(Kupci.formatKups(kupList))
    
def noviKupac():
    print("[PRODAVAC] - Unos novog kupca")
    kup = {}
    kup['ime'] = input("Unesite ime >> ")
    kup['prezime'] = input("Unesite prezime >> ")
    kup['korIme'] = input("Unesite korisnico ime >> ")
    kup['lozinka'] = input("Unesite lozinka >> ")
    Kupci.addKup(kup)
    Kupci.saveKup()
    print("[PRODAVAC] Novi kupac je upisan u sistem.")
    
def noviProizvod():
    print("[PRODAVAC] - Unos novog proizvoda")
    pro = {}
    pro['kod'] = input("Unesite sifru proizvoda >> ")
    pro['naziv'] = input("Unesite ime >> ")
    pro['vrsta'] = input("Unesite vrstu >> ")
    pro['kolicina'] = input("Unesite kolicinu >> ")
    pro['cena'] = input("Unesite cenu >> ")
    Proizvodi.addProizvod(pro)
    Proizvodi.saveProizvods()
    print("[PRODAVAC] Novi proizvod je upisan u sistem.")
    
def spisakProizvoda():
    Proizvodi.sortirajProizvode('naziv')
    print(Proizvodi.formatHeader())
    print(Proizvodi.formatAllProizvods())

def promenaCene():
    print("[PRODAVAC] - Promena cene proizvoda")
    naziv = input(" Unesite naziv proizvoda >> ")
    pro = Proizvodi.findProizvod(naziv)
    if pro == None:
        print("Ne postoji proizvod pod tim imenom")
    else:
        pro['cena'] = input("Dodatu cena >> ")
        print("Nova cena proizvoda je: ", pro['cena'])
    Proizvodi.saveProizvods()
    
def novaKolicina():
    print("[PRODAVAC] - Dodavanje kolicine proizvoda")
    naziv = input("Unesite naziv proizvoda >> ")
    pro = Proizvodi.findProizvod(naziv)
    if pro == None:
        print("Ne postoji proizvod pod tim imenom")
    else:
        pro['kolicina'] = str(int(pro['kolicina']) + int(input("Unesite >> ")))
        print("Nova kolicina proizvoda je", pro['kolicina'] )
    Proizvodi.saveProizvods()    

def prodato():
    print("[PRODAVAC] - Kolicina prodatih proizvoda za dan")  
    datum = input("Unesi datum(mm/dd/yy): ")
    dat = Racuni.searchRac('datum', datum)
    rac = Racuni.findDatum(datum)
    if len(dat) == 0:
        print("Pogresan datum")
    else:
        x_podaci = []
        y_podaci = []
        for rac in dat:
            x_podaci.append(rac['naziv'])
            y_podaci.append(int(rac['kolicina']))
        plt.bar(x_podaci, y_podaci)
        plt.xlabel('proizvodi')
        plt.ylabel('kolicina')
        plt.ylim(ymin=0, ymax=11)
        plt.show()

def zarade():
    print("[PRODAVAC] - Zarada po danu")
    datum = input("Unesi datum(mm/dd/yy): ")
    dat = Racuni.searchRac('datum', datum)
    rac = Racuni.findDatum(datum)
    if len(dat) == 0:
        print("Pogresan datum")
    else:
        x_podaci = []
        y_podaci = []
        for rac in dat:
            x_podaci.append(rac['naziv'])
            y_podaci.append(int(rac['cena']))
        plt.bar(x_podaci, y_podaci)
        plt.xlabel('proizvodi')
        plt.ylabel('zarada')
        plt.ylim(ymin=0, ymax=1000)
        plt.show()
        
def poVrsti():
    print("[PRODAVAC] - Zarada po vrsti proizvoda po danu")
    datum = input("Unesi datum(mm/dd/yy): ")
    dat = Racuni.searchRac('datum', datum)
    rac = Racuni.findDatum(datum)
    if len(dat) == 0:
        print("Pogresan datum")
    else:
        x_podaci = []
        y_podaci = []
        for rac in dat:
            x_podaci.append(rac['vrsta'])
            y_podaci.append(int(rac['cena']))
        plt.bar(x_podaci, y_podaci)
        plt.xlabel('vrsta')
        plt.ylabel('zarada')
        plt.ylim(ymin=0, ymax=1000)
        plt.show()

'''
===============================================================================
                                    KUPAC
===============================================================================
'''

def loginK():
    korIme = input("[KUPAC] Unesite korisnicko ime: ")
    lozinka = input("[KUPAC] Unesite lozinku: ")
    return Kupci.loginK(korIme, lozinka)

def printMenuK():
    print("\n[KUPAC] Izaberite opciju:")
    print(" 1 - kupovina") 
    print(" 2 - spisak proizvoda") 
    print(" x - izlaz iz programa")    

def kcmd():
    printMenuK()
    cmdk = input(">> ")
    while cmdk.upper() not in ('1', '2', 'X'):
        print("\nUneli ste pogresnu komandu.\n")
        printMenuK()
        cmdk = input(">> ")
    return cmdk.upper() 

def kupovina():
    print("[KUPAC] Kupovina")
    spisakProizvoda()
    rac = {}
    rac['naziv'] = input("Unesite ime proizvoda kojeg zelite da kupite(x za kraj): ")
    while rac['naziv'] not in ('x'):
        pro = Proizvodi.findProizvod(rac['naziv'])
        print(pro['vrsta'])
        if rac['naziv'] == pro['naziv']:
            rac['kolicina'] = input("Unesite kolicinu: ")
            if int(rac['kolicina']) > int(pro['kolicina']):
                print("Nema toliko proizvoda na lageru")
                print("Na lageru je dostupno", pro['kolicina'], "a vi zelite", rac['kolicina'])
            else:
                pro['kolicina'] = str(int(pro['kolicina']) - int(rac['kolicina']))
                Proizvodi.saveProizvods()
                rac['cena'] = str(int(rac['kolicina']) * int(pro['cena']))
                rac['vrsta'] = pro['vrsta']
                x = datetime.datetime.now()
                rac['datum'] = x.strftime("%x")
                Racuni.addRacun(rac)
                Racuni.saveRacuns()
                print("Uspesno ste kupili proizvod: ", rac['naziv'], "u kolicini:", rac['kolicina'])
        spisakProizvoda()
        rac = {}
        rac['naziv'] = input("Unesite ime proizvoda kojeg zelite da kupite(x za kraj): ")

print(__name__)
if __name__ == '__main__':
    main()