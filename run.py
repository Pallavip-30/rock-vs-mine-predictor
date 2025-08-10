import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# 1. Load the dataset
data = pd.read_csv("sonar data.csv", header=None)

# 2. Separate features and labels
X = data.drop(columns=60, axis=1)  # First 60 columns are features
y = data[60]  # Last column is label (R or M)

# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, stratify=y, random_state=1)

# 4. Model Training
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("\n✅ Model trained successfully!")
print(f"Training Accuracy: {model.score(X_train, y_train):.2f}")
print(f"Testing Accuracy: {model.score(X_test, y_test):.2f}")

# 5. Take user input for prediction
print("\nEnter 60 sonar readings separated by spaces:")
try:
    input_data = list(map(float, input().strip().split()))
    if len(input_data) != 60:
        raise ValueError("You must enter exactly 60 values.")

    # Convert to numpy array and reshape
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    if prediction == 'R':
        print("\n🪨 Prediction: **Rock**")
    else:
        print("\n💣 Prediction: **Mine**")

except Exception as e:
    print(f"\n❌ Error: {e}")
