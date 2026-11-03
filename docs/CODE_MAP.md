# Source code provenance — CABG

These four files are **present** in [analysis/](../analysis/). They were copied from the connected CABG Google Drive archive into the Private repository, renamed for sequential navigation, and their saved notebook outputs/execution counts were removed.

| Committed path | Original filename | Purpose |
|---|---|---|
| `analysis/01_data_preprocessing.Rmd` | `processing_dataset-v2.Rmd` | Clinical data recoding, missingness, KNN imputation |
| `analysis/02_baseline_descriptive_table.ipynb` | `s2_generating_table1.ipynb` | Table 1 and baseline analysis |
| `analysis/03_rf_feature_selection.ipynb` | `s3_selecting_optimal_RF_model.ipynb` | Classification, feature selection and CV |
| `analysis/04_model_interpretation_and_reporting.ipynb` | `s4_plots_table.ipynb` | SHAP, tables and figures |

The original clinical dataset, intermediate tables and saved notebook outputs were not committed. One project-root marker in the R code was updated for the new folder location; no claim is made that the archive is a fully tested reproduction of the final published paper.

**Historical experiment AUCs or feature sets may differ from the final article.** The source archive includes exploratory versions and has not been reconciled to the paper's final model. See [the publication checklist](BEFORE_PUBLICATION.md).
