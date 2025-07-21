# Revolutionizing-Liver-Care-Predicting-Liver-Cirrhosis-using-Advanced-Machine-Learning-Techniques

##  Project Overview
This project uses machine learning to predict whether a patient is at risk of liver cirrhosis using clinical and blood test features. A Flask-based web interface is used to collect patient data and display real-time prediction results based on a trained ML model.

---

##  Objective
To build a non-invasive, fast, and accurate system to assist healthcare providers in early diagnosis of liver cirrhosis using structured medical data.

---

##  Features
- Real-time prediction using trained ML models
- Web-based input form for medical values
- Data-driven prediction output (Yes/No)
- Cleaned dataset excluding non-numeric features (except the target)
- Achieved 100% accuracy on test data (on available dataset)

---

##  Dataset Overview
The dataset includes medical features such as:
- Age, Alcohol Consumption (duration and quantity)
- Blood pressure, Hemoglobin, Cholesterol (TCH, TG, LDL, HDL)
- Red and White Blood Cell parameters (RBC, WBC, PCV, MCH, MCHC, etc.)
- Platelet Count, Bilirubin Levels, Proteins
- Liver enzymes: ALP, SGOT (AST), SGPT (ALT)
- **Target column:** `Predicted Value` (0 = Cirrhosis, 1 = No Cirrhosis)

All non-numeric features (like gender, place, alcohol type, etc.) are removed except the target variable.

---

##  Tech Stack

| Component  | Technology         |
|------------|--------------------|
| ML Model   | XGBoost            |
| Backend    | Python + Flask     |
| Frontend   | HTML (no Bootstrap)|
| Tools      | Jupyter Notebook, VS Code |
| Dataset    | CSV Format (from Kaggle) |

---

##  How to Run the Project

### Prerequisites
- Python 3.11+
- Flask
- pandas, numpy, scikit-learn, joblib

### Setup Instructions
```bash
git clone https://github.com/RAVURITEJASRI/Revolutionizing-Liver-Care-Predicting-Liver-Cirrhosis-using-Advanced-Machine-Learning-Techniques.git
cd Revolutionizing-Liver-Care-Predicting-Liver-Cirrhosis-using-Advanced-Machine-Learning-Techniques
pip install -r requirements.txt
python app.py
