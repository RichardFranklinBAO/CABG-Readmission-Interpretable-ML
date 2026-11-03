# CABG Readmission — Interpretable Machine Learning

**Research code portfolio (private review draft)**

**Publication:** Manyam R, Bao C, He Y, et al. *Interpretable Machine Learning Risk Model to Predict Readmission After Coronary Artery Bypass Grafting.* JTCVS Open (2026). [DOI: 10.1016/j.xjon.2026.102050](https://doi.org/10.1016/j.xjon.2026.102050).

## Research question

How can clinical and preoperative variables help predict readmission after coronary artery bypass grafting (CABG), and how can an interpretable machine-learning workflow help researchers investigate the associated predictors?

## My contribution

I independently implemented the computational analysis in R and Python: data preparation, clinical variable coding, missing-data processing, baseline comparisons, model training and feature-selection experiments, performance evaluation, SHAP explanations, and figure/table generation. The faculty collaborator led manuscript writing.

## Archived computational workflow

1. **R data preparation:** clinical-variable recoding, missingness checks, KNN imputation.
2. **Baseline statistics:** descriptive comparisons and manuscript tables.
3. **Machine learning:** random-forest experiments, comparative classifiers, cross-validation and feature selection.
4. **Interpretability and reporting:** SHAP explanations, model-comparison figures and tables.

## Important distinctions

The archived scripts include **intermediate and exploratory versions**. The archived training/test splits and candidate feature sets are not necessarily identical to those used for the final published results. The paper is the authoritative source for the published findings. This repository must not be described as a verified end-to-end reproduction until the version and results have been reconciled.

## Data access and reproducibility

**No patient-level data are included in this repository.** The original clinical dataset is not publicly redistributable through this portfolio. A future independently runnable example will use **synthetic data only** and will be labeled as a coding demonstration, not a validation of the published estimates.

Please consult [the code review checklist](docs/BEFORE_PUBLICATION.md) before public redistribution.

**Current status:** Repository scaffold for private review. Source scripts will be added only after privacy, rights, and technical review.
