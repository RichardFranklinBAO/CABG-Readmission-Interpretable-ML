# CABG analysis: read in order

| Stage | Script | What it does |
|---|---|---|
| 1 | [01_data_preprocessing.Rmd](01_data_preprocessing.Rmd) | Clinical variable processing, missingness checks and imputation |
| 2 | [02_baseline_descriptive_table.ipynb](02_baseline_descriptive_table.ipynb) | Statistical summaries and Table 1 |
| 3 | [03_rf_feature_selection.ipynb](03_rf_feature_selection.ipynb) | Model comparison, feature selection and cross-validation |
| 4 | [04_model_interpretation_and_reporting.ipynb](04_model_interpretation_and_reporting.ipynb) | SHAP analysis and research figure/table generation |

The scripts retain the original analytical logic and some legacy data-path assumptions. Jupyter outputs have been removed. Because clinical input datasets are not distributed, these archived scripts are a record of research programming rather than a standalone executable replication.

For runnable code without study data, start with [the synthetic RF example](../examples/synthetic_rf_demo.py). See [data availability](../docs/DATA_AVAILABILITY.md) for details.
