import argparse
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib


def train_model(model_name: str):
    # Load data
    iris = load_iris()
    X, y = iris.data, iris.target

    # Train model
    model = RandomForestClassifier(n_estimators=100, verbose=1)
    model.fit(X, y)

    # Save model
    joblib.dump(model, model_name)
    print(f"Model trained and saved as {model_name}")


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-name", type=str, default="model.pkl")
    return parser.parse_args()

if __name__ == "__main__":
    args = init_args()
    train_model(args.model_name)