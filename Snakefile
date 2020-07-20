container: "docker://continuumio/miniconda3:4.8.2"

rule all:
    input:
        "results/figures/reg_performance.png",
        "results/predictions/baseline_pred.csv"

rule dataset:
    output:
        "data/raw/submission_format.csv",
        "data/raw/training_set_features.csv",
        "data/raw/training_set_labels.csv",
        "data/raw/test_set_features.csv"
    conda:
        "environment.yml"
    script:
        "src/get_data.py"

rule evaluation:
    input:
        "data/raw/training_set_features.csv",
        "data/raw/training_set_labels.csv"
    output:
        "results/figures/reg_performance.png"
    conda:
        "environment.yml"
    script:
        "src/evaluate_model.py"

rule predictions:
    input:
        "data/raw/submission_format.csv",
        "data/raw/training_set_features.csv",
        "data/raw/training_set_labels.csv",
        "data/raw/test_set_features.csv"
    output:
        "results/predictions/baseline_pred.csv"
    conda:
        "environment.yml"
    script:
        "src/predict.py"