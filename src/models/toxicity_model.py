import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/processed/toxicity_dataset.csv")

def load_data():
    df = pd.read_csv(DATA_PATH)
    print("Dataset shape:", df.shape)
    return df

# prepping features and labels and dropping compound names,
# since it's not a predictive biological feature
def prepare_features(df):
    y = df["toxicity_label"]
    X = df.drop(columns=["toxicity_label", "compound"])
    return X, y

# train/test split data
from sklearn.model_selection import train_test_split

def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
    return X_train, X_test, y_train, y_test

# train the Model (Random Forest works well for omics-style biological datasets)
from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model

# model evaluation using AUC (important in drug safety modeling)
from sklearn.metrics import accuracy_score, roc_auc_score

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    prob = model.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, preds)
    auc = roc_auc_score(y_test, prob)

    print("Accuracy:", acc)
    print("ROC AUC:", auc)

# Identify Important Genes/Biomarkers
def feature_importance(model, X):
    importance = model.feature_importances_

    feature_df = pd.DataFrame({
        "gene": X.columns,
        "importance": importance
    }).sort_values(by="importance", ascending=False)

    print("\nTop predictive genes:")
    print(feature_df.head(10))

    return feature_df

# Creating the Pipeline Runner
def main():
    df = load_data()
    X, y = prepare_features(df)
    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    feature_importance(model, X)

if __name__ == "__main__":
    main()
