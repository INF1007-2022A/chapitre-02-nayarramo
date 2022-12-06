#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    
    newWord = ""

    # Pour chaque lettre du mot, trouver le caractère ascii et soustraire 32
    # puis ajouter cette lettre au nouveau mot
    for letter in mot:
        newWord += chr(ord(letter)-32)
    return newWord


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
