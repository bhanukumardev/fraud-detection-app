import joblib
import pandas as pd

# Load the pipeline
pipe = joblib.load('fraud_detection_pipeline.pkl')

# Example: new transaction(s) as a DataFrame
new_data = pd.DataFrame([{
    'Amount': 5000,
    'Location': 'Other',
    'Type': 'UPI',
    'Hour': 16,
    'Day': 'Thu',
    'Is_New_Location': 1,
    'Is_High_Amount': 1
}])

# Predict
pred_class = pipe.predict(new_data)
pred_proba = pipe.predict_proba(new_data)[:, 1]

print(f"Fraud prediction: {pred_class[0]} (probability: {float(pred_proba):.2f})")
