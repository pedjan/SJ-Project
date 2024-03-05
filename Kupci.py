# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 20:16:16 2020

@author: Pedja
"""

def loginK(username, password):
    for k in kupci:
        if k['korIme'] == username and k['lozinka'] == password:
            return True
    return False
    
def loadKup():
    for line in open('kupci.txt', 'r').readlines():
        if len(line) > 1:
            kup = str2kup(line)
            kupci.append(kup)

def saveKup():
    fajl = open('kupci.txt', 'w')
    for k in kupci:
        fajl.write(kup2str(k))
        fajl.write('\n')
    fajl.close()

def searchKup(field, value):
    rez = []
    for k in kupci:
        if k[field].upper() == value.upper():
            rez.append(k)
    return rez

def addKup(kup):
    kupci.append(kup)

def str2kup(line):
    if line[-1] == '\n':
        line = line[:-1]
    ime, prezime, korIme, lozinka = line.split('|')
    kup = {'ime': ime, 
           'prezime': prezime, 
           'korIme': korIme, 
           'lozinka': lozinka}
    return kup

def kup2str(kup):
    return '|'.join([kup['ime'], kup['prezime'], kup['korIme'], kup['lozinka']])


def formatHeader():
    return \
      "Ime    |Prezime |korIme |Lozinka   \n" \
      "-------+--------+-------+----------"

def formatKup(kup):
    return u"{0:7}|{1:8}|{2:7}|{3:7}".format(
        kup['ime'], 
        kup['prezime'], 
        kup['korIme'], 
        kup['lozinka'])

def formatKups(kupList):
    result = ""
    for kup in kupList:
        result += formatKup(kup) + '\n'
    return result
    result = ""
    for kup in kupList:
        result += formatKup(kup) + '\n'
    return result
'''
def formatAllKups():
    result = ''
    for kup in kupci:
        result += "{0:7}|{1:8}|{2:7}|{3:7}".format(
        kup['ime'], 
        kup['prezime'], 
        kup['korIme'], 
        kup['lozinka']) + '\n'
    return result
'''
def sortirajKupce(key):
    kupci.sort(key = lambda x: x[key])

print(__name__)
kupci = []
loadKup()