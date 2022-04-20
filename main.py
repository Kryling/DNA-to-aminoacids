from translation_transription import *

strandtype = input('What kind of string do you have: ')
startCodon = input('Does the DNA string have a Start Codon? ')

if strandtype == 'mRNA':
    print('mRNA')
    mRNA = input('Enter mRNA: ')

    print(translation_mRNA(mRNA, startCodon))

elif strandtype == 'Coding DNA':
    print('Coding DNA')
    DNA = input('Enter coding DNA string: ')

    # Turns DNA into mRNA
    mRNA = transcription_coding_DNA(DNA)
    # mRNA to protein string
    print(translation_mRNA(mRNA, startCodon))

elif strandtype == 'template DNA':
    print('template DNA')
    DNA = input('Enter template DNA string: ')

    mRNA = transcription_template_DNA(DNA)

    # mRNA to protein string
    print(translation_mRNA(mRNA, startCodon))
