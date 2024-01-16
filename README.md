# Transition rates MOMAP/QChem
To calculate the radiative and non-radiative rates of transitions we can use MOMAP (Molecular Materials Property Prediction Package) code available here: http://www.momap.net.cn/.
In the manual, the authors suggest performing the required calculations in the Gaussian package. However, sometimes, problematic system requires spin-flip procedure, which is not available in the Gaussian package.
Here is how to do it in the QChem program, along with the Python scripts to visualize and convert data properly.

1. Produce the outputs for optimization of the ground state (s0.in), a first excited state of singlet manifold (s1.in), triplet state (t1.in), and nonadiabatic couplings (nacme.in). The queuing script named qchem.sub can be invoked with:
qchem.sub *.in

2. Create the directories: evc, kic, kr  for the fluorescence spectrum and evc, kisc, kr, dalton for phosphorescence spectrum.  For the evc, you need the output file from s0,s1 and nacme QChem calculations. The input file for MOMAP (momap.inp) includes:

do_evc	= 1

&evc
 ffreq(1) = "s0.log"
 ffreq(2) = "s1.log"
 fnacme   = "nacme.log"
/
One should follow the instructions of momap package for running the calculations. In my case it is 
$MOMAP_ROOT/bin/momap.py -i momap.inp -n 4  > log 2>&1 &

3. For the kIC it is required to know delta adiabatic energy Ead which can be obtained with simple Python script ead.py:
python ./ead.py s0.log s1.log
or bash script:

a=`grep "Final" s0.log | cut -f2 -d"s"`
b=`grep "Final" s1.log | cut -f2 -d"s"`
echo $b-$a | bc -l

grep "Final" AU-s0.log
5.  
