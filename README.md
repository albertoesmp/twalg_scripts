Taubin-Weingarten algorithm paper
======================================

This repository contains the files necessary to reproduce the experiments.




VL3D++ framework
-------------------

First, the VL3D++ framework is necessary to run the algorithms, train the models, and evaluate them. It is an open-source software that can be downloaded from [its official repository](https://gitlab.com/catallactical/vl3dpp).



Shapenet scripts
--------------------

***shapenet/data*** :
The scripts to transform the the shapenet datasets to LAS format


***shapenet/experiments/kfold*** :
The scripts to run the stratified k-folding experiments on the airplane, car, chair, guitar, knife, lamp, motorbike, and pistol datasets.

***shapenet/experiments/fixed*** :
The scripts to run the ablation study on the chair, pistol, motorbike, and car datasets.


DALES scripts
----------------

*dales* :
The scripts to run the first-order, second-order, and hybrid model experiments on the DALES dataset. It also contains the bash scripts to generate the SLURM scripts to run the sensitivity analysis in the FinisTerrae-III supercomputer.



HPC scripts
----------------

*hpc* :
The scripts to run the experiments of the scalability analysis from 1 to 32 cores using the FinisTerrae-III with SLURM.



Theoretical validation
------------------------

*theoretical* :
The script to run the theoretical experiments and the Jupyter notebook for Sagemath used to generate the analyitical references. It also contains an alternative version of the notebook where normal noise along the gradient direction can be modelled through its standard deviation.

*theoretical/data* :
The point clouds corresponding to the theoretical experiments.





Cite
------
**DOI**:

**Bibtex**:
```
```

