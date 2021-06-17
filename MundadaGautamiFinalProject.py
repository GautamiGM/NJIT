from urllib.request import urlopen

def rna2comp(seq):
    ret = ''
    for ch in seq:
        if ch == 'a':
            ret += 'u'
        elif ch == 'u':
            ret += 'a'
        elif ch == 'g':
            ret += 'c'
        elif ch == 'c':
            ret += 'g'
    return ret
        
def dna2rna(seq):
    ''' The dna2rna function converts a sequence of DNA, given as a
        parameter and returns an RNA sequence.
    '''
    ret = ''
    for ch in seq:
        if ch == 't':
            ret += 'u'
        else:
            ret += ch
    return ret

codon2aa = {'aaa': 'K', 'aac': 'N', 'aag': 'K', 'aau': 'N',
            'aca': 'T', 'acc': 'T', 'acg': 'T', 'acu': 'T',
            'aga': 'R', 'agc': 'S', 'agg': 'R', 'agu': 'S',
            'aua': 'I', 'auc': 'I', 'aug': 'M', 'auu': 'I',

            'caa': 'Q', 'cac': 'H', 'cag': 'Q', 'cau': 'H',
            'cca': 'P', 'ccc': 'P', 'ccg': 'P', 'ccu': 'P',
            'cga': 'R', 'cgc': 'R', 'cgg': 'R', 'cgu': 'R',
            'cua': 'L', 'cuc': 'L', 'cug': 'L', 'cuu': 'L',

            'gaa': 'E', 'gac': 'D', 'gag': 'E', 'gau': 'D',
            'gca': 'A', 'gcc': 'A', 'gcg': 'A', 'gcu': 'A',
            'gga': 'G', 'ggc': 'G', 'ggg': 'G', 'ggu': 'G',
            'gua': 'V', 'guc': 'V', 'gug': 'V', 'guu': 'V',

            'uaa': '_', 'uac': 'Y', 'uag': '_', 'uau': 'Y',
            'uca': 'S', 'ucc': 'S', 'ucg': 'S', 'ucu': 'S',
            'uga': '_', 'ugc': 'C', 'ugg': 'W', 'ugu': 'C',
            'uua': 'L', 'uuc': 'F', 'uug': 'L', 'uuu': 'F'}

if __name__ == '__main__':
    with urlopen('http://web.njit.edu/~kapleau/teach/current/bnfo135/sequence.gb') as conn:
        data = conn.readlines()

    lines = [line.strip() for line in [datum.decode() for datum in data]]
    flag = False
    dna = ''

    for line in lines:
        if flag:
            dna += line.strip('\n')
        if (line.strip('\n') == 'ORIGIN':
            flag = True
        pass

    dna = dna.translate(str.maketrans('acgt', 'acgt', '0123456789 /'))

    rna = dna2rna(dna)

    for i in range(3):
        seq = rna[i:]
        amino = ''
        while len(seq) >= 3:
            amino = amino + codon2aa[seq[0:3]]
            seq = seq[3:]
            pass
        print('--- Reading Frame %i ---' % (i+1), amino, sep='\n')

    rna = rna2comp(rna)
    rna = rna[::-1]

    for i in range(3):
        seq = rna[i:]
        amino = ''
        while len(seq) >= 3:
            amino = amino +codon2aa[seq[0:3]]
            seq = seq[3:]
            pass
        print('--- Reading Frame %i ---' % (i+4), amino, sep='\n')
