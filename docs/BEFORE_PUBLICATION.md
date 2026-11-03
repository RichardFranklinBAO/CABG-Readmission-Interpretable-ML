# Pre-publication review checklist

This repository is currently **PRIVATE**. Do not change its visibility until these checks are complete.

- [ ] Verify the principal investigator, institution, data provider, and relevant collaborators permit code redistribution.
- [ ] Review code cells as well as notebook outputs for person-level observations, identifiers, literal clinical rows, server paths, account names, credentials, and residual artifacts.
- [ ] Ensure no raw/derived patient-level CSV, Excel, Pickle, RDS, trained weights, or unreviewed screenshots are committed, including in Git history.
- [ ] Verify which script version generated the **published** paper's reported results; separate archived exploratory experiments from the final analytical pipeline.
- [ ] Examine KNN imputation and feature-selection timing relative to train/test splitting for potential leakage.
- [ ] Replace local absolute paths with configurable project-relative paths.
- [ ] Test a small independent demonstration on synthetic data.
- [ ] Record verified package versions and run instructions.
- [ ] Confirm paper citation and individual contribution statements.
- [ ] Decide on a code license only after rights clearance.

No permission to distribute patient records should be inferred from a private GitHub repository or the presence of a .gitignore file.
