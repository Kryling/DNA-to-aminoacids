amino_acids = {'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu', 'UCU': 'Ser', 'UCC': 'Ser',
               'UCA': 'Ser', 'UCG': 'Ser', 'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
               'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp', 'CUU': 'Leu', 'CUC': 'Leu',
               'CUA': 'Leu', 'CUG': 'Leu', 'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
               'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln', 'CGU': 'Arg', 'CGC': 'Arg',
               'CGA': 'Arg', 'CGG': 'Arg', 'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
               'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr', 'AAU': 'Asn', 'AAC': 'Asn',
               'AAA': 'Lys', 'AAG': 'Lys', 'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
               'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val', 'GCU': 'Ala', 'GCC': 'Ala',
               'GCA': 'Ala', 'GCG': 'Ala', 'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
               'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'}


def transcription_coding_DNA(string):
    mRNA = ''
    for base in string:
        if base == 'T':
            mRNA += 'A'

        elif base == 'A':
            mRNA += 'U'

        elif base == 'C':
            mRNA += 'G'

        elif base == 'G':
            mRNA += 'C'
    return mRNA


def transcription_template_DNA(string):
    DNA = ''
    for base in string:
        if base == 'T':
            DNA += 'A'
        elif base == 'A':
            DNA += 'T'
        elif base == 'C':
            DNA += 'G'
        elif base == 'G':
            DNA += 'C'

    print(f'This is the coding DNA Strand {DNA}')

    return transcription_coding_DNA(DNA)


def translation_mRNA(mRNA, startCodon):
    mRNAlst = []
    protein = list()
    lownum = 0
    highnum = 3
    while highnum <= len(mRNA):
        mRNAlst.append(mRNA[lownum:highnum])
        highnum += 3
        lownum += 3
    if startCodon:
        start = (mRNAlst.index('AUG'))
        del mRNAlst[:start]
    else:
        for codon in mRNAlst:
            protein.append(amino_acids.get(codon))
            if 'Stop' in protein:
                break
            else:
                continue
    return protein
