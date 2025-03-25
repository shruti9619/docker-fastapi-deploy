from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Train model
model = RandomForestClassifier(n_estimators=100, verbose=1)
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")
print("Model trained and saved as model.pkl")