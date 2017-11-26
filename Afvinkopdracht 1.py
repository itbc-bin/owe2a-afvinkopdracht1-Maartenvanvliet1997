##################################################################################
#Auteur: Maarten van Vliet
#Datum: 22-11-2017
#Versie: 2.0

#Beschrijving:
"""
Dit script opent een betand in fasta format. Het verwerkt het bestand in een 2D-lijst.
Deze 2D-lijst wordt hierna opgesplitst in 'headers' en 'sequenties'. Deze sequenties worden daarna gescant
"""
##################################################################################

import os

def main():
    bestand = 'alpaca.fasta'

    zoekwoord = input('Geef het zoekwoord op: ')
    file = open_bestand(bestand)
    headers, seqs = lees_inhoud(zoekwoord, file)

    for i in range(len(seqs)):
        if is_dna(seqs[i]): #Test of seq[i] een DNA-sequentie is
            print('*' * 80,
                  '\n' + headers[i])
            knipt(seqs[i]) #Test of er van een bepaalde reeks enzymen, enzymen knippen in seq[i]

def p():
    b = input('- Press Enter to continue -')
    os.system('CLS')

#Input: bestandsnaam
#Output: 2D-lijst van het bestand
#Beschrijving: Op het moment dat het bestand niet gevonden wordt, zoekt de functie zelf naar een bestand in fasta format in de working directory.

def open_bestand(bestand):
    fa = []
    
    try:
        file = open(bestand, 'r').readlines()
    except FileNotFoundError:
        print('Error: There is no such file or directory:', bestand)

        for name in os.listdir('.'):
            if name.endswith('.fasta') or name.endswith('.fna') or name.endswith('.faa'):
                fa.append(name)

        if fa != []:
            print('Some usable files have been found:\n')
            
            for i in range(len(fa)):
                print('[' + str(i + 1) + '] -',fa[i])
                
            try:
                b = int(input('\nEnter the number of the file you would like to use: '))
            except ValueError:
                print('Wrong Input, please try again!')
                p()
                open_bestand(bestand)  

            bestand = fa[b-1]

            file = open(bestand, 'r').readlines()
        else:
            print('No usable files have been found. Make sure to add a fasta file to the working directory')
            p()
            open_bestand(bestand)

    if file:
        return file

#Input: Het 'zoekwoord' en de 2D-lijst van het bestand (file)
#Output: Alle headers van het bestand in een 2D-lijst + Alle losse sequenties in een 2D-lijst
#Beschrijving: De functie splitst headers en sequenties en zoekt naar het zoekwoord.

def lees_inhoud(zoekwoord, file):
    headers = []
    seqs = []
    seq = []

    for line in file:
        line.rstrip()
        if '>' in line:
            headers.append(line)
            if seq != []:
                seqs.append(seq)
        else:
            seq.append(line)
        if zoekwoord in line:
            pos = file.index(line)
            lpos = line.index(zoekwoord)
            print('Het zoekwoord is gevonden in line:',pos,
                  '\n' + '*' * 80,
                  '\n' + line,
                  '\n' + ' ' * lpos + zoekwoord)
            
    return headers, seqs

#Input: Een sequentie
#Output: Boolean
#Beschrijving: De functie checkt of de sequentie een DNA-sequentie is.
       
def is_dna(seq):
    
    for line in seq:
        line = line.rstrip()        
        for char in line:
            if char not in 'ATGCN':
                return False
    return True

#Input: Een sequentie
#Output: De functie print of een enzym knipt en waar.
#Beschrijving: ''
    
def knipt(seq):
    fa = []
    bestand = 'enzymen.txt'
    
    try:
        file = open(bestand,'r').readlines()
    except FileNotFoundError:
        print('Error: There is no such file or directory:', bestand)

        for name in os.listdir('.'):
            if name.endswith('.txt'):
                fa.append(name)

        if fa != []:
            print('Some usable files have been found:\n')
            
            for i in range(len(fa)):
                print('[' + str(i + 1) + '] -',fa[i])

            try:
                b = int(input('\nEnter the number of the file you would like to use: '))
            except ValueError:
                print('Wrong Input, please try again!')
                p()
                knipt(seq)

            bestand = fa[b-1]

            file = open(bestand, 'r').readlines()
        else:
            print('No usable files have been found. Make sure to add an enzym textfile to the working directory')
            p()
            knipt(seq)
            
    
    seq = ''.join(seq).replace('\n','')

    for line in file:
        line = line.rstrip()
        enzym, codon = line.split(' ')
        codon = codon.replace('^','')
        
        if codon in seq:
            pos = seq.index(codon)
            print('-'*80,
                  '\nmatcht met',enzym,'op positie',pos)
            
try:
    main()
except:
    print("Error found: Unknown Error. Contact your nearest bioinformatician!")
