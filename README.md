# Flu Shot Learning

Repository for my work on the [Flu Shot Learning](https://www.drivendata.org/competitions/66/flu-shot-learning/) competition on Driven Data.
Driven Data profile: [apoirel](https://www.drivendata.org/users/apoirel/)

Work in progress.

## Setup

This is only necessary if you intend to experiment with or modify
the code

### For experimenting on local OS

Create a conda environment with all the required packages: 
```sh
conda env create -f environment.yml
```

## Reproducing the results

### On local OS
In this directory
```sh
snakemake --use-conda all
```

### On Singularity (recommended)
```
snakemake --use-singularity --use-conda all
```

## Project structure
```
├── environment.yml          <- The file defining the conda Python environmnet. 
├── Snakefile                <- Definition of the full workflow for reproducing the analysis.
├── LICENSE                                 
├── README.md                <- The top-level README.
├── data
│   ├── processed            <- The final, canonical data sets for modeling.
│   └── raw                  <- The original, immutable data dump.
├── output             
|   ├── models               <- Serialized models, predictions, model summaries.
|   └── figures              <- Graphics created during analysis.
├── paper                    <- Generated analysis as PDF, LaTeX.
└── src                      <- Source code for this project.
    ├── notebooks            <- Jupyter notebooks.
    └── __init__.py          <- Makes this a python module.
```
    
## Results

0.8342 AUC on hidden test set, 181/948 on leaderboard.

## License

This project is distributed under the  MIT license.
