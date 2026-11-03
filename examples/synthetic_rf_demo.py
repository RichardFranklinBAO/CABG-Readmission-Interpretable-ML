"""Standalone synthetic-data RF coding sample; not the published CABG analysis."""
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split


def run_demo(random_state=42):
    x, y = make_classification(
        n_samples=500,
        n_features=12,
        n_informative=5,
        n_redundant=2,
        weights=[0.9, 0.1],
        flip_y=0.02,
        random_state=random_state,
    )
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, stratify=y, random_state=random_state
    )
    model = RandomForestClassifier(
        n_estimators=100, min_samples_leaf=3, random_state=random_state, n_jobs=1
    )
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=random_state)
    cv_auc = cross_val_score(
        model, x_train, y_train, cv=cv, scoring="roc_auc", n_jobs=1
    )
    model.fit(x_train, y_train)
    auc = roc_auc_score(y_test, model.predict_proba(x_test)[:, 1])
    importance = permutation_importance(
        model, x_test, y_test, n_repeats=3, random_state=random_state,
        scoring="roc_auc", n_jobs=1
    )
    print(f"Synthetic-data CV AUROC: {cv_auc.mean():.3f}")
    print(f"Synthetic-data held-out AUROC: {auc:.3f}")
    print("Top 3 synthetic feature indices:",
          importance.importances_mean.argsort()[-3:][::-1].tolist())
    return auc


if __name__ == "__main__":
    run_demo()
