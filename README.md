# CABG Readmission — Interpretable Machine Learning

**Published research · Independent R/Python computational analysis · Private research-code portfolio**

**Publication:** Manyam R, Bao C, He Y, et al. *Interpretable Machine Learning Risk Model to Predict Readmission After Coronary Artery Bypass Grafting*. *JTCVS Open* (2026). [DOI: 10.1016/j.xjon.2026.102050](https://doi.org/10.1016/j.xjon.2026.102050).

## Overview

This study investigates 30-day readmission after coronary artery bypass grafting (CABG) using tabular clinical characteristics and interpretable machine-learning methods.

**My contribution:** I independently wrote the computational analysis in R and Python, including clinical-data recoding and preparation, missingness handling, statistical comparisons, classifier/model-selection experiments, performance evaluation, SHAP interpretation, and research tables/figures. Faculty collaborators led manuscript writing.

## Start here: coding sample without patient data

- [Run the standalone synthetic-data Random Forest example](examples/synthetic_rf_demo.py) ([instructions](examples/README.md)). It demonstrates stratified splitting, five-fold cross-validation, AUROC and permutation importance.
- This **new educational demonstration** is separate from the CABG analysis; synthetic metrics must **not** be interpreted as the paper's findings.

## Research script map

| Stage | File | Purpose |
|---|---|---|
| 01 | [Data preparation (R)](analysis/01_data_preprocessing.Rmd) | Clinical variable coding, missingness checks, KNN imputation |
| 02 | [Descriptive statistics / Table 1 (Python)](analysis/02_baseline_descriptive_table.ipynb) | Baseline statistical comparisons and manuscript table |
| 03 | [Models and feature selection (Python)](analysis/03_rf_feature_selection.ipynb) | Random Forest, other classifiers, CV and feature selection |
| 04 | [SHAP and reporting (Python)](analysis/04_model_interpretation_and_reporting.ipynb) | Model interpretation, figures, tables and comparisons |

[Read the analysis instructions](analysis/README.md) · [Original filename map](docs/CODE_MAP.md) · [Privacy and publication checklist](docs/BEFORE_PUBLICATION.md)

## Reproducibility and scientific limits

No patient-level datasets, weights or saved notebook execution outputs are included. The archived research scripts retain some original dataset filenames and relative import assumptions; authorized inputs and path adaptation are needed for full execution. The archival notebooks include exploratory versions **not guaranteed to reproduce** the final paper's published results. Neither the code in this repository nor synthetic examples should be represented as a fully verified reproduction of the publication.

The repository is currently **Private** pending institutional/data-owner permission, a complete disclosure review and reproducibility checks. Do not change its visibility until these checks are completed.
