import os

# Naam: Maarten van Vliet
# Datum: 10-10-2017
# Versie: 1.1

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.
def p():
    b = input('\n- Press Enter to continue -')
    os.system('CLS')
    
def main():
    bestand = "banaan.fasta" # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
    """
    Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
    De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
    """
    zoekwoord = input("Geef een zoekwoord op: ")
    headers, seqs = lees_inhoud(bestand, zoekwoord) 
        
    # schrijf hier de rest van de code nodig om de aanroepen te doen
    
    
def lees_inhoud(file_name, zoekwoord):
    fa = []
    
    try:
        file = open(file_name).readlines()
    except FileNotFoundError:
        print('Error: There is no such file or directory:', file_name)

        for name in os.listdir('.'):
            if name.endswith('.fasta') or name.endswith('.fna') or name.endswith('.faa'):
                fa.append(name)

        if fa != []:
            print('In the current working directory some useable files have been found.')

            for i in range(len(fa)):
                print('[' + str(i + 1) + '] - ' + fa[i])

            try:
                b = int(input('\nWhat file would you like to use: '))
            except ValueError:
                lees_inhoud(file_name, zoekwoord)

            file_name = fa[(b-1)]
            lees_inhoud(file_name, zoekwoord)
            
        else:
            print('No usable files have been found in the current working directory.\n',
                  'To use this program, add a fasta file to the working directory.\n')

            b = input("- Press Enter to try again - ")
            lees_inhoud(file_name, zoekwoord)    
        
    headers = []
    seqs = []
    seq = []

    for line in file:
        line.rstrip()
        if '>' in line:
            headers.append(line)
            print("-" * 80,
                  "\n" + str(line))
            if seq != []:
                isDNA = is_dna(seq)
                if isDNA:
                    knipt(seq)
                    seqs.append(seq)
                    seq = []
                else:
                    seq = []
        else:
            seq.append(line)
        if zoekwoord in line:
            print(line)
     
    return headers, seqs
    
def is_dna(seq):
    nuc = 'ATCGN'
    isDNA = True
    seq = ''.join(seq).replace('\n','')
   
    for char in seq:
        if char not in nuc:
            isDNA = False

    return isDNA
            
def knipt(seq):
    file = open('enzymen.txt','r').readlines()
    seq = ''.join(seq).replace('\n','')

    for line in file:
        line = line.rstrip()
        enzym, codon = line.split(' ')
        codon = codon.replace('^','')
        
        if codon in seq:
            pos = seq.index(codon)
            print('-'*80,
                  '\nmatcht met',enzym,'op positie',pos)    
       
    
main()
