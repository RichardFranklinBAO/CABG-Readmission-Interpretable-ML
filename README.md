# Predicting CABG Readmission with Interpretable Machine Learning

**Research code | Python + R | JTCVS Open (2026)**

This repository documents the computational work for *Interpretable Machine Learning Risk Model to Predict Readmission After Coronary Artery Bypass Grafting* ([DOI: 10.1016/j.xjon.2026.102050](https://doi.org/10.1016/j.xjon.2026.102050)).

## Research question

Can clinical characteristics help identify patients at risk of readmission after CABG, and which variables are most important in an interpretable machine-learning analysis?

## My contribution

I independently implemented the computational analysis in Python and R: data preparation and recoding, missingness handling, descriptive comparisons, classifier and feature-selection experiments, performance assessment, SHAP interpretation, and preparation of research tables and figures. Faculty collaborators led the manuscript-writing process.

## Quick start — standalone example

The self-contained [synthetic Random Forest demonstration](examples/synthetic_rf_demo.py) does **not** require patient records.

```bash
pip install -r requirements.txt
python examples/synthetic_rf_demo.py
```

This example illustrates train/test splitting, cross-validation, AUROC, and permutation feature importance. Its results are **synthetic examples**, not reported paper results.

## Research workflow

| Stage | Research script | Contents |
|---|---|---|
| 1 | [Clinical preprocessing (R)](analysis/01_data_preprocessing.Rmd) | Variable coding, missingness checks and KNN imputation |
| 2 | [Baseline statistical tables](analysis/02_baseline_descriptive_table.ipynb) | Descriptive comparisons and Table 1 |
| 3 | [Model training and feature selection](analysis/03_rf_feature_selection.ipynb) | Random Forest, classifier comparisons, CV and feature selection |
| 4 | [Interpretation and reporting](analysis/04_model_interpretation_and_reporting.ipynb) | SHAP, performance plots and manuscript-facing tables |

See the [analysis guide](analysis/README.md) and [original-file mapping](docs/CODE_MAP.md) for the archived workflow.

## Data availability and reproducibility

This repository contains research code and a synthetic demonstration, **not patient-level clinical data, model weights or subject-level prediction files**. Original scripts reference restricted study inputs by filename; an authorized copy of those inputs and their original directory assumptions would be needed to run the full pipeline.

The analysis folder preserves original research and exploratory versions, not a verified one-command reproduction of every final published result. Saved Jupyter output cells and execution counters have been cleared. See [Data and reproducibility notes](docs/DATA_AVAILABILITY.md).

## Citation

Please cite the published article when referring to the clinical study. The synthetic demonstration is separate from the published empirical analysis.
