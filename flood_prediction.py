import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load sample data
# Columns: rainfall_mm, river_level_m, drainage_capacity, flood (1=flood, 0=no flood)
data = pd.read_csv("../data/sample_rainfall.csv")

X = data[["rainfall_mm", "river_level_m", "drainage_capacity"]]
y = data["flood"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
sample = [[120, 3.5, 0.6]]  # Example input
prediction = model.predict(sample)
print("Flood Risk Prediction:", "Flood" if prediction[0] == 1 else "No Flood")
