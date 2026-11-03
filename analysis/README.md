# CABG research analysis code

The scripts follow the archived project workflow:

1. [01 — R preprocessing](01_data_preprocessing.Rmd): clean variables, missingness and KNN imputation.
2. [02 — Baseline table](02_baseline_descriptive_table.ipynb): compare readmission subgroups and produce Table 1.
3. [03 — Model experiments](03_rf_feature_selection.ipynb): compare classifiers, cross-validation, and feature-selection procedures.
4. [04 — Explanation and reporting](04_model_interpretation_and_reporting.ipynb): SHAP and manuscript-facing figures/tables.

**Read this first:** The notebooks' outputs were cleared before committing. They are an archive of exploratory work, not a turnkey run or a guaranteed exact replication of the final paper. Real clinical data are not distributed. For a fully runnable example requiring no restricted data, use [the synthetic coding sample](../examples/synthetic_rf_demo.py).

## Source provenance

The four source scripts were uploaded from the user's CABG research archive and renamed in sequential order. The R notebook's project-root marker was updated to match its new folder path. Original file names are mapped in [CODE_MAP.md](../docs/CODE_MAP.md). Algorithmic decision steps were not silently rewritten for publication.
