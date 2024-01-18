#!/usr/bin/env python

import sys

def find_all_strength_values(file_path):
    # List to hold all the strength values
    strength_values = []
    energy_values = []
    # Flag to indicate if the excited state has been found
    excited_state_found = False

    # Open the file for reading
    with open(file_path, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Check if the current line contains the excited state phrase
            if "Excited state   1:" in line:
                excited_state_found = True
                parts = line.split('=')
                if len(parts) > 1:
                    # Try to convert the following string into a float
                    try:
                        energy_value = float(parts[1].strip())
                        energy_values.append(energy_value)
                    except ValueError:
                        # If conversion fails, print an error message
                        print("Could not convert strength value to float.")
                        continue  # Continue looking for more strength values
            # If excited state was found, look for the strength line
            if excited_state_found and "Strength   :" in line:
                # Split the line by colon to extract the strength value
                parts = line.split(':')
                if len(parts) > 1:
                    # Try to convert the following string into a float
                    try:
                        strength_value = float(parts[1].strip())
                        strength_values.append(strength_value)
                    except ValueError:
                        # If conversion fails, print an error message
                        print("Could not convert strength value to float.")
                        continue  # Continue looking for more strength values
                # Flag to indicate if the excited state has been found
                excited_state_found = False

    # Return all found strength values
    return strength_values,energy_values

# Give the parameter 1 as your s1.out
filename=sys.argv[1]
strength_values,energy_values = find_all_strength_values(filename)

def DipoleStrength(f,dE):
    hbar=1.0
    me=1.0
    au2ev = 27.211324570273
    dE = dE/au2ev
    return (3.*f*(hbar**2))/(2.*me*dE)

if strength_values:
    au2ev = 27.211324570273
    fo_1 = strength_values[0] 
    dE_1 = energy_values[0]
    fo_l = strength_values[-1] 
    dE_l = energy_values[-1]
    print("The first and the last extracted strength values are:")
    print("first ={:10.7f}, last={:10.7f}".format(fo_1,fo_l))
    print("The first and the last extracted energy values are:")
    print("first ={:10.5f}, last={:10.5f} eV".format(dE_1,dE_l))
    print("first ={:10.5f}, last={:10.5f} au".format(dE_1/au2ev,dE_l/au2ev))
    print("The first and the last dipole strength values are:")
    d_1 = DipoleStrength(fo_1,dE_1)
    d_l = DipoleStrength(fo_l,dE_l)
    au2deb = 2.5417
    print("first ={:10.7f}, last={:10.7f} au".format(d_1,d_l))
    print("first ={:10.7f}, last={:10.7f} Deb".format(d_1*au2deb,d_l*au2deb))
else:
    print("No strength values extracted.")
