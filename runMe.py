#!/usr/bin/env python
from countAA import aaCount



f = open("aaInput.faa")
lines = f.readlines()
seq = []
for i in range(0, len(lines)):
    seq.append(lines[i].rstrip("\n"))

amino = seq[1:len(seq)]
amino = "".join(amino)

#print(amino)

aaCount(amino)
