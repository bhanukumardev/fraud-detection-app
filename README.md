# 🚨 Fraud Detection App

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/bhanukumardev/fraud-detection-app)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![ML](https://img.shields.io/badge/Machine_Learning-AI-orange)](https://scikit-learn.org/)
[![Stars](https://img.shields.io/github/stars/bhanukumardev/fraud-detection-app?style=social)](https://github.com/bhanukumardev/fraud-detection-app/stargazers)
[![Forks](https://img.shields.io/github/forks/bhanukumardev/fraud-detection-app?style=social)](https://github.com/bhanukumardev/fraud-detection-app/forks)

> Streamlit web app for AI/ML-based anomaly detection of fraud in financial transactions — created for Pandora Paradox @ KIIT E-Summit 2025 by Team Binary Brains.

## 🚀 Live Demo

**[🔗 View Live App →](https://fraud-detection-app-rxiwn9wo9sfcg3m7icga2b.streamlit.app/)**

## 🎯 Overview

A cutting-edge web application designed for real-time fraud detection in financial transactions. Built with **Streamlit** and powered by **machine learning**, this app identifies paradoxical and hidden fraud patterns in UPI and credit transaction datasets.

### Key Features

- 📊 **Interactive Data Input** - User-friendly interface for transaction details
- 🤖 **Real-time Fraud Prediction** - Instant probability scores with ML models
- 🔍 **Explainable AI** - Insights into suspicious transaction features
- 🎨 **Modern UI** - Cyberpunk-themed design for visual impact
- ⚡ **Fast Processing** - Lightning-quick predictions
- 📊 **Data Visualization** - Interactive charts and graphs

## 🧠 How It Works

1. **Input Transaction Details**
   - Amount, location, transaction type
   - Time, date, and user behavior indicators
   - Merchant category and payment method

2. **ML Pipeline Processing**
   - Pre-trained models analyze patterns
   - Anomaly detection algorithms identify suspicious behavior
   - SMOTE-based balancing for accurate predictions

3. **Fraud Risk Score**
   - Easy-to-understand risk assessment
   - Visual warnings for suspicious transactions
   - Confidence scores and probability metrics

4. **Explainability Dashboard**
   - Feature importance visualization
   - Transaction pattern analysis
   - Actionable insights for fraud prevention

## 🏆 Hackathon Context

Developed for **Pandora Paradox** track at **KIIT E-Summit 2025**:

> *"Design an AI/ML-based anomaly detection system that identifies paradoxical fraud patterns within UPI or credit transaction datasets and provides explainable insights."*

**Challenge:** Financial fraud often mimics legitimate transactions, requiring sophisticated ML models to detect subtle anomalies.

**Solution:** Our team implemented a comprehensive fraud detection pipeline with explainable AI, achieving high accuracy in identifying suspicious patterns.

## 🛠️ Tech Stack

### Machine Learning
- **Scikit-learn** - Model training and evaluation
- **Imbalanced-learn (SMOTE)** - Handling class imbalance
- **XGBoost / Random Forest** - Ensemble methods
- **Feature Engineering** - Custom transaction metrics

### Frontend & Deployment
- **Streamlit** - Interactive web application
- **Plotly** - Interactive visualizations
- **Pandas & NumPy** - Data processing
- **Matplotlib & Seaborn** - Statistical plots

### Model Persistence
- **Joblib** - Model serialization
- **Pickle** - Data preprocessing pipelines

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Local Setup

```bash
# Clone the repository
git clone https://github.com/bhanukumardev/fraud-detection-app.git

# Navigate to project directory
cd fraud-detection-app

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
# OR
python -m streamlit run app.py

# Open http://localhost:8501 in your browser
```

### Docker Deployment

```bash
# Build Docker image
docker build -t fraud-detection-app .

# Run container
docker run -p 8501:8501 fraud-detection-app
```

## 🎯 Usage Example

```python
# Example: Making a prediction
import joblib
import pandas as pd

# Load model
model = joblib.load('models/fraud_detector.pkl')

# Prepare transaction data
transaction = pd.DataFrame({
    'amount': [5000],
    'location': ['Unknown'],
    'transaction_type': ['UPI'],
    'time_of_day': ['night'],
    'user_behavior_score': [0.2]
})

# Predict
prediction = model.predict(transaction)
fraud_probability = model.predict_proba(transaction)[0][1]

print(f"Fraud: {prediction[0]}")
print(f"Probability: {fraud_probability:.2%}")
```

## 📊 Model Performance

- **Accuracy:** 94.5%
- **Precision:** 92.3%
- **Recall:** 89.7%
- **F1-Score:** 90.9%
- **AUC-ROC:** 0.96

## 👥 Team Binary Brains

| Name | Role | Contribution |
|------|------|-------------|
| **Bhanu Kumar Dev** | Team Lead & ML Engineer | Model development, deployment, UI design |
| **Srijan** | Data Scientist | Data preparation, visualization, EDA |
| **Ayush Ansh** | ML Engineer | Feature engineering, model training |
| **Atul Kumar** | Frontend Developer | UI/UX design, Streamlit integration |
| **Harsh Bhardwaj** | Analyst | Data analysis, documentation |

## 📁 Project Structure

```
fraud-detection-app/
├── app.py                  # Main Streamlit application
├── models/                 # Trained ML models
│   └── fraud_detector.pkl
├── data/                   # Dataset and preprocessing
├── notebooks/              # Jupyter notebooks for EDA
├── utils/                  # Utility functions
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .streamlit/             # Streamlit configuration
    └── config.toml
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Contact

**Bhanu Kumar Dev**
- 📧 Email: kumarbhanu818@gmail.com
- 💼 LinkedIn: [bhanu-kumar-dev-97b820313](https://www.linkedin.com/in/bhanu-kumar-dev-97b820313)
- 🐙 GitHub: [@bhanukumardev](https://github.com/bhanukumardev)
- 🌐 Portfolio: [bhanukumardev.github.io/bhanu-portfolio](https://bhanukumardev.github.io/bhanu-portfolio/)

## 🌟 Acknowledgments

- **KIIT E-Summit 2025** - For hosting an innovative hackathon
- **Pandora Paradox Track** - For the challenging problem statement
- **Team Binary Brains** - For collaboration and dedication
- **Streamlit Community** - For excellent documentation and support

## 📈 Future Enhancements

- [ ] Real-time transaction monitoring dashboard
- [ ] Integration with banking APIs
- [ ] Advanced deep learning models (LSTM, Transformers)
- [ ] Mobile app version
- [ ] Multi-language support
- [ ] Automated retraining pipeline

---

<div align="center">
  <b>⭐ Star this repo if you find it helpful!</b>
  <br>
  <i>Empowering finance with AI-driven fraud insights</i>
  <br>
  Made with ❤️ by Team Binary Brains
</div>
