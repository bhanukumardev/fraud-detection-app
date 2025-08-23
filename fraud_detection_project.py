import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dummy dataset
df = pd.read_csv("dummy_creditcard_data.csv")

# Display basic info and head
print("Dataset shape:", df.shape)
print("Class distribution:\n", df['Class'].value_counts())
print("First 5 rows:")
print(df.head())

# Define features and target
features = [
    'Amount', 'Location', 'Type', 'Hour', 'Day',
    'Is_New_Location', 'Is_High_Amount'
]
target = 'Class'

X = df[features]
y = df[target]

# Categorical and numeric features
categorical = ['Location', 'Type', 'Day']
numeric = ['Amount', 'Hour', 'Is_New_Location', 'Is_High_Amount']

# Preprocessor: Scale numeric, One-Hot-Encode categorical
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric),
        ("cat", OneHotEncoder(handle_unknown='ignore'), categorical)
    ]
)

# Train/Test Split (stratify for class balance)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Train shape:", X_train.shape, "Test shape:", X_test.shape)

# Combine everything in a pipeline
pipe = Pipeline([
    ('pre', preprocessor),            # preprocessing: scaling + one-hot encoding
    ('smote', SMOTE(random_state=42)),  # oversample minority class
    ('clf', LogisticRegression(max_iter=1000, random_state=42))
])

# Fit the pipeline to training data
pipe.fit(X_train, y_train)

# Save the pipeline (contains everything: encoders, scaler, model)
joblib.dump(pipe, 'fraud_detection_pipeline.pkl')
print("Full pipeline saved as fraud_detection_pipeline.pkl")

# Predict on test set
y_pred = pipe.predict(X_test)
y_proba = pipe.predict_proba(X_test)[:, 1]

# Performance metrics
print("Classification Report:\n", classification_report(y_test, y_pred, digits=4))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))
print("AUC:", roc_auc_score(y_test, y_proba))

# Extract feature names after preprocessing
pre = pipe.named_steps['pre']
num_feats = pre.transformers_[0][2]
cat_encoder = pre.transformers_[1][1]
cat_feats = cat_encoder.get_feature_names_out(categorical)
feature_names = list(num_feats) + list(cat_feats)

coefs = pipe.named_steps['clf'].coef_[0]  # LogisticRegression coef_ is 2D (1, n_features)

# Display feature importance
coef_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': coefs
}).sort_values(by='Importance', key=lambda x: x.abs(), ascending=False)

print("\nTop 10 most influential features:\n", coef_df.head(10))

# Plot top 10 feature importances
plt.figure(figsize=(10, 5))
sns.barplot(y='Feature', x='Importance', data=coef_df.head(10), palette='viridis')
plt.title('Top 10 Most Important Features (Logistic Regression Coefficients)')
plt.xlabel('Coefficient')
plt.ylabel('Feature')
plt.tight_layout()
plt.show()


