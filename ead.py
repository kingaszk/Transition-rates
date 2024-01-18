#!/usr/bin/env python3

import sys

def find_energy(file_path):
    with open(file_path,'r') as file:
            for line in file:
                if "Final energy" in line:
                    a=line.split()
            return a[-1]

s0=find_energy(sys.argv[1])
s1=find_energy(sys.argv[2])

ev=27.2114
ead=(float(s1)-float(s0)) 
print("Ead amounts to",ead, "au; which is",ev*ead,"eV")
