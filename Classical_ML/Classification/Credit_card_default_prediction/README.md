## 🔍 Credit Default Risk Prediction with Explainability

Built a complete ML app to predict whether a customer will default on their credit payments — with a strong focus on **interpretability** using **SHAP** and **LIME**.


### 🚀 Key Highlights:

* 🧹 Cleaned and processed credit data (handling missing income, outliers, skewed distributions).
* ⚖️ Tackled class imbalance using **SMOTE** for fairer learning.
* 🤖 Trained multiple models and selected **XGBoost** for its performance + compatibility with SHAP. Also experimented with model stacking to improve predictions.
* 📈 Evaluated using AUC, F1, and a **threshold tuning strategy** to suit different business risk tolerances.
* 🧠 Applied **SHAP for global insights** (feature impact patterns) and **LIME for local explanations** (individual prediction reasoning).


### 📊 Learnings:

* Interpretable ML is crucial in finance — it's not just about accuracy, it's about **trust**.
* SHAP helped identify key features like:
  * High `RevolvingUtilization` ⟶ 🚩 High default risk
  * Zero delinquencies & low `DebtRatio` ⟶ ✅ Lower risk
* LIME showed how individual decisions are shaped, validating model behavior.


### 🛠 Tools:

Python, Scikit-learn, Imblearn,  XGBoost, SHAP, LIME, Matplotlib, Jupyter, Streamlit


Deployed on streamlit - <https://credit-default-prediction.streamlit.app/>