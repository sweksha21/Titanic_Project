# 🚢 Titanic Survival Prediction

This project predicts whether a passenger would survive the Titanic disaster using a **Logistic Regression model**.

---

## 📌 Project Overview

The goal of this project is to:

* Perform **Exploratory Data Analysis (EDA)**
* Preprocess the dataset
* Build a **Logistic Regression model**
* Evaluate model performance
* Deploy the model using **Streamlit**

---

## 📊 Dataset

* Dataset: Titanic Dataset
* Features include:

  * Passenger Class (Pclass)
  * Gender (Sex)
  * Age
  * Fare
  * Number of relatives (SibSp, Parch)
  * Embarked Port

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Seaborn & Matplotlib
* Scikit-learn
* Streamlit

---

## 🔍 Exploratory Data Analysis (EDA)

Key insights:

* Females had a higher survival rate than males
* Passengers in higher classes were more likely to survive
* Age had moderate impact on survival

---

## 🧹 Data Preprocessing

* Handled missing values:

  * Age → Median
  * Embarked → Mode
* Dropped unnecessary columns:

  * Name, Ticket, Cabin, PassengerId
* Encoded categorical variables:

  * Sex → Numeric
  * Embarked → One-hot encoding

---

## 🤖 Model Building

* Model: Logistic Regression
* Data split into training and testing sets
* Trained using Scikit-learn

---

## 📈 Model Evaluation

Metrics used:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

---

## 🚀 Deployment

The model is deployed using **Streamlit**.

### ▶️ Run the App

1. Install dependencies:

```
pip install streamlit
```

2. Run the app:

```
streamlit run app.py
```

3. Open in browser:

```
http://localhost:8501
```

---

## 🧠 How It Works

User inputs passenger details →
Model processes input →
Predicts survival →
Displays result with probability

---

## 📁 Project Structure

```
Titanic_Project/
│
├── app.py          # Streamlit application
├── model.pkl       # Trained model
├── README.md       # Project documentation
```

---

## 👨‍💻 Author

**SWESKHA SHARMA**

---

## ⭐ Conclusion

This project demonstrates:

* End-to-end Machine Learning workflow
* Data preprocessing and visualization
* Model building and evaluation
* Real-world deployment using Streamlit
