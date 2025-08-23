<<<<<<< HEAD
import pandas as pd
import numpy as np

np.random.seed(42)  # For reproducible results

num_samples = 10000

data = pd.DataFrame({
    "Amount": np.random.exponential(scale=200, size=num_samples).round(2),
    "Location": np.random.choice(
        ['Mumbai', 'Delhi', 'Bangalore', 'Pune', 'Hyderabad', 'Other'],
        size=num_samples
    ),
    "Type": np.random.choice(
        ['E-Commerce', 'UPI', 'ATM Withdrawal', 'POS Swipe', 'Bank Transfer'],
        size=num_samples
    ),
    "Hour": np.random.randint(0, 24, size=num_samples),
    "Day": np.random.choice(
        ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        size=num_samples
    ),
    "Is_New_Location": np.random.choice([0, 1], size=num_samples, p=[0.85, 0.15]),
    "Is_High_Amount": np.random.choice([0, 1], size=num_samples, p=[0.92, 0.08]),
})

# Add a simple fraud label: fraud if at least two "flags" are present: high amount, new location, UPI transaction, or transaction at night
def fraud_label(row):
    score = 0
    if row["Amount"] > 500:
        score += 1
    if row["Is_New_Location"] == 1:
        score += 1
    if row["Type"] == "UPI":
        score += 1
    if row["Hour"] >= 22 or row["Hour"] <= 5:
        score += 1
    return 1 if score >= 2 else 0

data["Class"] = data.apply(fraud_label, axis=1)

# Save to CSV
data.to_csv("dummy_creditcard_data.csv", index=False)
print("Dummy dataset saved as dummy_creditcard_data.csv")
print(data.head())
=======
import pandas as pd
import numpy as np

np.random.seed(42)  # For reproducible results

num_samples = 10000

data = pd.DataFrame({
    "Amount": np.random.exponential(scale=200, size=num_samples).round(2),
    "Location": np.random.choice(
        ['Mumbai', 'Delhi', 'Bangalore', 'Pune', 'Hyderabad', 'Other'],
        size=num_samples
    ),
    "Type": np.random.choice(
        ['E-Commerce', 'UPI', 'ATM Withdrawal', 'POS Swipe', 'Bank Transfer'],
        size=num_samples
    ),
    "Hour": np.random.randint(0, 24, size=num_samples),
    "Day": np.random.choice(
        ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        size=num_samples
    ),
    "Is_New_Location": np.random.choice([0, 1], size=num_samples, p=[0.85, 0.15]),
    "Is_High_Amount": np.random.choice([0, 1], size=num_samples, p=[0.92, 0.08]),
})

# Add a simple fraud label: fraud if at least two "flags" are present: high amount, new location, UPI transaction, or transaction at night
def fraud_label(row):
    score = 0
    if row["Amount"] > 500:
        score += 1
    if row["Is_New_Location"] == 1:
        score += 1
    if row["Type"] == "UPI":
        score += 1
    if row["Hour"] >= 22 or row["Hour"] <= 5:
        score += 1
    return 1 if score >= 2 else 0

data["Class"] = data.apply(fraud_label, axis=1)

# Save to CSV
data.to_csv("dummy_creditcard_data.csv", index=False)
print("Dummy dataset saved as dummy_creditcard_data.csv")
print(data.head())
>>>>>>> a26f2a4fcd7532a16612f2f904608ed868c378d6
