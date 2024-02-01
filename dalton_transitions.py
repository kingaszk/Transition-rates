import sys
import math

doc='''Usage: python dalton_par.py edma_s0.out edme_t1.out soc_t1.out'''

def find_transition_moment(file_path):
	moments=[]
	with open(file_path, 'r') as file:
        # Iterate over each line in the file
            for line in file:
            # Check if the current line contains the excited state phrase
                if "Transition moment" in line:
                    moment = line.split()
	   	    if len(moment) > 1:
                    # Try to convert the following string into a float
                        try:
                            moment1 = float(moment[-1])
                            moments.append(moment1)
                        except ValueError:
                        # If conversion fails, take another value (sometimes au at the end)
                            moment1 = float(moment[-2])
                            moments.append(moment1)

                            continue  # Continue looking for more transition moments values

	return moments

def find_spinorbit_coupling(file_path):
    socs=[]
    with open(file_path, 'r') as file:
        # Iterate over each line in the file           
           for line in file:
            # Check if the current line contains the excited state phrase
               if "Spin-orbit" in line:
                    soc = line.split()[-4]
                    try:
                        soc=float(soc)
                        socs.append(soc)
                    except ValueError:
                        print("Try another position!")
                        continue
    return socs


def print_parameter(filename):
    debye=2.5417
    parameters=[]
    for i in range(3):
	log=find_transition_moment(filename)
	parameter=math.sqrt(log[0]**2+log[1]**2+log[2]**2)*debye
    	return parameter


print("Parameters in Debye: ","edma: ",print_parameter(sys.argv[1]),"edme: ",print_parameter(sys.argv[2]), "hso: ",print_parameter(sys.argv[3]))

log=find_spinorbit_coupling(sys.argv[3])
hso=math.sqrt((log[0]**2+log[1]**2+log[2]**2)/3.)  
print("HSO w cm-1: ",hso)
