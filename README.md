Taubin-Weingarten algorithm paper
======================================

This repository contains the files necessary to reproduce the experiments.




VL3D++ framework
-------------------

First, the VL3D++ framework is necessary to run the algorithms, train the models, and evaluate them. It is an open-source software that can be downloaded from [its official repository](https://github.com/catallactical/vl3d).



Shapenet scripts
--------------------

***shapenet/data*** :
The scripts to transform the the shapenet datasets to LAS format


***shapenet/experiments*** :
The scripts to run the stratified k-folding experiments on the airplane, car, chair, guitar, knife, lamp, motorbike, and pistol datasets.



DALES scripts
----------------

*dales* :
The scripts to run the first-order, second-order, and hybrid model experiments on the DALES dataset.



HPC scripts
----------------

*hpc* :
The scripts to run the experiments of the scalability analysis from 1 to 32 cores using the FinisTerrae-III with SLURM.



Theoretical validation
------------------------

*theoretical* :
The script to run the theoretical experiments and the Jupyter notebook for Sagemath used to generate the analyitical references.

*theoretical/data* :
The point clouds corresponding to the theoretical experiments.





Cite
------
**DOI**:

**Bibtex**:
```
```

