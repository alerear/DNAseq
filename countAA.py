#!/usr/env/bin python

def aaCount(dna):
    length = len(dna)
    m_count = dna.count('M')
    r_count = dna.count('R')
    y_count = dna.count('Y')
    new = dna.replace('L','l')
    l_count = new.count('l')

    aaCount = ((m_count + r_count + y_count + l_count)/float(length)) *100
    return print(round(aaCount, 3),'%'), print(new)
