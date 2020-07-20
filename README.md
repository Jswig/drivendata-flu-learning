# Flu Shot Learning

*Anders Poirel, 16/07/2020*

Repository for my work on the [Flu Shot Learning](https://www.drivendata.org/competitions/66/flu-shot-learning/) competition on Driven Data.
Driven Data profile: [apoirel](https://www.drivendata.org/users/apoirel/)

Work in progress.

## Setup

### For running on local OS

Create a conda environment with all the required packages: 
```sh
conda env create -f environment.yml
conda activate flu-shot-learning
```

### For running on a Docker container (recommended)

```sh
docker build .
```

## Reproducing the results

TODO

## Project structure
```
├── environment.yml          <- The file defining the conda Python environment 
├── Dockerfile               <- The file definining the container environment
\├── LICENSE                                 
├── README.md                <- The top-level README
├── data
│   ├── processed            <- The final, canonical data sets for modeling.
│   └── raw                  <- The original, immutable data dump.
├── output             
|   ├── models               <- Serialized models, predictions, model summaries.
|   └── visualization        <- Graphics created during analysis.
├── reports                  <- Generated analysis as HTML, PDF, LaTeX, etc.
└── src                      <- Source code for this project.
    ├── notebooks            <- Jupyter notebooks.
    └── __init__.py          <- Makes this a python module.
```
    
## Results

0.8342 AUC on hidden test set, 181/948 on leaderboard.

## License

This project is distributed under the  MIT license.
