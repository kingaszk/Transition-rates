# Transition rates MOMAP/QChem

To calculate the radiative and non-radiative rates of transitions we can use MOMAP (Molecular Materials Property Prediction Package) code available here: http://www.momap.net.cn/.
In the manual, the authors suggest performing the required calculations in the Gaussian package. However, sometimes, problematic system requires spin-flip procedure, which is not available in the Gaussian package.
Here is how to do it in the QChem program, along with the Python scripts to visualize and convert data properly.

1. Produce the outputs for optimization of the ground state (s0.in), a first excited state of singlet manifold (s1.in), triplet state (t1.in), and nonadiabatic couplings (nacme.in).
   When you install this package you can create your own queuing script named sub-qchem (main is attached for an example). It can be invoked with:

    sub-qchem *.in

3. Create the directories: evc, kic, kr  for the fluorescence spectrum and evc, kisc, kr, dalton for phosphorescence spectrum.
    For the evc, you need the output file from s0,s1 and nacme QChem calculations. You should follow the instructions of momap package for running the calculations. In my case it is 

$MOMAP_ROOT/bin/momap.py -i momap.inp -n 4  > log 2>&1 &

3. For the kIC it is required to know delta adiabatic energy Ead which can be obtained with simple Python script ead.py:
   
**python ead.py s0.log s1.log**

or Bash script:

**$ a=`grep "Final" s0.log | cut -f2 -d"s"` && b=`grep "Final" s1.log | cut -f2 -d"s"` && echo $b-$a | bc -l**

You can visualize the results with the Gnuplot scripts
$ gnuplot *gnu

4.  For the kr calculations one should extract the transition moments from  the output files. In the case of the QChem package it can be converted from the oscillator strength ![image](https://github.com/kingaszk/AT-AU-photodeactivation/assets/156574267/4c4146d8-e5cf-4b90-9c71-7f79fcf0b5ca)
, which is, by definition,
  ![image](https://github.com/kingaszk/AT-AU-photodeactivation/assets/156574267/6753390d-49d5-425b-b1e1-41fbba31ca71)
 where ![image](https://github.com/kingaszk/AT-AU-photodeactivation/assets/156574267/5d694aa2-b766-4cf0-a984-6f146b3d771b)
 is the mass of an electron and ![image](https://github.com/kingaszk/AT-AU-photodeactivation/assets/156574267/a403ff5f-003d-4522-9317-1a94bad96e76)
 is the reduced Planck constant.

You can use the Python script to convert needed parameters.

**python qchem_transitions.py s1.log**

IMPORTANT: one should remember to do the calculations of the excited state on the starting geometry of the optimized ground state. Otherwise, the parameters should be calculated again (just single points on the s0 and s1 molecules).


5. In the case of the phosphorescence rates it is an analogous procedure. You need the optimized  geometry of the ground state and T1  triplet state.
   However, the QChem package is not able to produce the transition dipole moments of triplet geometry while printing SOC Hamiltonian (or at least I did not find it in the manual). The Hso parameter for the kISC can be obtained from the QChem output generated from soc.in (sub-qchem soc.in). However, while the spin-flip procedure does not make sense for the triplet configuration, it is better to calculate the EDMA, EDME, and HSo parameters within Dalton package.

sub-dalton edma.dal s0.mol
sub-dalton edme.dal t1.mol
sub-dalton soc.dal t1.mol

The Python script which extracts the required parameters from the Dalton output is attached.

**python dalton_transitions.py edma.log edme.log soc.log**



If there is any trouble, the manuals can be found here:
1. https://manual.q-chem.com/5.2/Ch7.S3.SS6.html
2. http://www.momap.net.cn/archives/docs/MOMAP_Tutorial_02_Irppy3.pdf
3. https://daltonprogram.org/manuals/dalton2020manual.pdf
   
