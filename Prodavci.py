# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 19:39:05 2020

@author: Pedja
"""

def loginP(username, password):
    for p in prodavci:
        if p['korIme'] == username and p['lozinka'] == password:
            return True
    return False
    
def loadProd():
    for line in open('prodavci.txt', 'r').readlines():
        if len(line) > 1:
            prod = str2prod(line)
            prodavci.append(prod)

def str2prod(line):
    if line[-1] == '\n':
        line = line[:-1]
    ime, prezime, korIme, lozinka = line.split('|')
    prod = {'ime': ime, 
           'prezime': prezime, 
           'korIme': korIme, 
           'lozinka': lozinka}
    return prod

def prod2str(prod):
    return '|'.join([prod['ime'], prod['prezime'], prod['korIme'], prod['lozinka']])

print(__name__)
prodavci = []
loadProd()