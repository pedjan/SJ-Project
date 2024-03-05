# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:00:59 2021

@author: Pedja
"""


def loadRacuns():
    for line in open('racuni.txt', 'r').readlines():
        if len(line) > 1:
            rac = str2racun(line)
            racuni.append(rac)
            
def saveRacuns():
    file = open('racuni.txt', 'w')
    for rac in racuni:
        file.write(racun2str(rac))
        file.write('\n')
    file.close()
    
def str2racun(line):
    if line[-1] == '\n':
        line = line[:-1]
    naziv, kolicina, cena, vrsta, datum = line.split('|')
    rac = {
        'naziv': naziv,
        'kolicina': kolicina,
        'cena': cena,
        'vrsta': vrsta,
        'datum': datum
    }
    return rac

def racun2str(rac):
    return '|'.join([rac['naziv'], rac['kolicina'], rac['cena'], rac['vrsta'], rac['datum']])

def searchRac(field, value):
    rez = []
    for rac in racuni:
        if rac[field].upper() == value.upper():
            rez.append(rac)
    return rez

def addRacun(rac):
    racuni.append(rac)

def findDatum(datum):
    for rac in racuni:
        if rac['datum'].upper() == datum.upper():
            return rac
    return None

racuni = []
loadRacuns()