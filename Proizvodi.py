# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 12:50:57 2020

@author: Pedja
"""

def loadProizvods():
    for line in open('proizvodi.txt', 'r').readlines():
        if len(line) > 1:
            pro = str2proizvod(line)
            proizvodi.append(pro)
            
def saveProizvods():
    file = open('proizvodi.txt', 'w')
    for pro in proizvodi:
        file.write(proizvod2str(pro))
        file.write('\n')
    file.close()
    
def str2proizvod(line):
    if line[-1] == '\n':
        line = line[:-1]
    kod, naziv, vrsta, kolicina, cena = line.split('|')
    pro = {
        'kod': kod,
        'naziv': naziv,
        'vrsta': vrsta,
        'kolicina': kolicina,
        'cena': cena
    }
    return pro

def proizvod2str(pro):
    return '|'.join([pro['kod'], pro['naziv'], pro['vrsta'], pro['kolicina'], pro['cena']])

def formatHeader():
    return \
      "Kod|Naziv                  |Vrsta           |Kol|Cena \n" \
      "---+-----------------------+----------------+---+-----"

def formatAllProizvods():
    result = ''
    for pro in proizvodi:
        result += "{0:2}|{1:23}|{2:16}|{3:2}|{4:2}".format(
        pro['kod'], 
        pro['naziv'], 
        pro['vrsta'], 
        pro['kolicina'], 
        pro['cena']) + '\n'
    return result

def sortirajProizvode(key):
    proizvodi.sort(key = lambda x: x[key])

def addProizvod(pro):
    proizvodi.append(pro)

def searchProizvodNaziv(naziv):
    result = []
    for pro in proizvodi:
        if pro['naziv'].upper() == naziv.upper():
            result.append(pro)
    return result


def findProizvod(naziv):
    for pro in proizvodi:
        if pro['naziv'].upper() == naziv.upper():
            return pro
    return None

proizvodi = []
loadProizvods()