# Synthetic Random Forest coding demonstration

Install `numpy` and `scikit-learn`, then run:

```bash
python examples/synthetic_rf_demo.py
```

Uses an entirely synthetic imbalanced binary-classification dataset. It demonstrates stratified train/test splitting, 5-fold cross-validation, Random Forest, AUROC and permutation importance. **The synthetic numerical results are not CABG paper results**, and the script is not a reconstruction of the final published model.

The script was tested locally with synthetic data before upload.
