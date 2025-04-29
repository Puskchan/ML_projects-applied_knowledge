## 🧠 Core Project Questions:

**1. Q: What was the goal of your project?A:** To predict whether a customer will default on credit payments using historical financial and credit behavior data, with model interpretability baked in via SHAP and LIME.



**2. Q: How did you handle missing values in the dataset?A:** I imputed missing `MonthlyIncome` using median values grouped by `NumberOfDependents` — a domain-aware choice that preserves distribution without overfitting.



**3. Q: What preprocessing steps did you take?A:** Outlier removal using IQR, skew correction with log transform (for income and utilization), and normalization for model compatibility.



**4. Q: Which models did you try and why?A:** I compared Logistic Regression, Random Forest, and XGBoost — XGBoost won due to high AUC and SHAP compatibility. It handled class imbalance + missing values well.



**5. Q: How did you evaluate your model's performance?A:** Used precision, recall, F1-score, and AUC-ROC. I also tuned the decision threshold based on business use-case — prioritizing recall for risk mitigation.



**6. Q: How did you handle class imbalance?A:** Applied **SMOTE** (Synthetic Minority Oversampling Technique) to generate synthetic samples for the minority class — balanced the dataset for fair learning.



**7. Q: What’s the importance of SHAP in your model?A:** SHAP provides both **global** and **local** interpretability — quantifies feature contributions consistently using Shapley values from game theory.



**8. Q: What did SHAP reveal about important features?A:** High `RevolvingUtilizationOfUnsecuredLines`, high `DebtRatio`, and multiple delinquencies had strong positive SHAP values — i.e., they increase default risk.



**9. Q: Why did you use LIME along with SHAP?A:** SHAP gives global + per-sample insights, but LIME offers instance-based, perturbation-based local reasoning — good for real-time decisions & user explanations.



**10. Q: What’s the difference between SHAP and LIME?A:** SHAP uses a model-consistent additive explanation method (Shapley values); LIME builds a surrogate linear model around a prediction to locally explain it.



**11. Q: Why is interpretability important in credit scoring?A:** Regulatory compliance (like GDPR) requires explainability. Stakeholders (banks, customers) need to understand why a decision was made — for fairness & trust.



**12. Q: How did you choose the decision threshold?A:** I analyzed the precision-recall tradeoff, then chose a threshold that minimized false negatives (defaults predicted as non-defaults) — critical in finance.



**13. Q: What feature engineering did you do?A:** Binned features like `age` and `DebtRatio`, created interaction terms for combined delinquencies, and filtered irrelevant or constant columns.



**14. Q: How did you validate your model?A:** Stratified K-Fold Cross-Validation ensured balanced class representation in each fold — especially crucial due to original class imbalance.



**15. Q: What does a SHAP value of -1.5 mean for a feature?A:** It means the feature **reduced** the model’s prediction log-odds (or raw score) by 1.5 — i.e., it pushed the prediction toward the “No Default” class.



**16. Q: What challenges did you face and how did you solve them?A:** Handling missing values and class imbalance was tricky — I iterated through visual EDA + domain-driven imputation and chose SMOTE with caution (to avoid overfitting).


### 🧠 Bonus: Critical Thinking / System Design:


**17. Q: How would you make this model production-ready?A:** I'd wrap it with a REST API (FastAPI), track input distributions over time for drift, add explanation endpoints, and integrate CI/CD with model versioning.



**18. Q: What fairness checks would you add?A:** Check for disparate impact by `age`, `gender`, or `income` groups — using metrics like equal opportunity and demographic parity.



**19. Q: How would you explain a rejection to a customer using LIME?A:** Use the LIME output to highlight top 2-3 factors that drove the decision (e.g. high utilization, past delinquencies) with suggestions to improve their score.



**20. Q: If this model started performing poorly in production, what would you check?A:** First check for **concept drift** — if user behavior has changed. Then validate feature distributions, SHAP shifts, and model retraining pipelines.


---

**Q1:** How would you detect and respond to concept drift in a deployed credit scoring model?

**Q2:** Can SHAP be misleading if features are highly correlated? How do you handle that?

**Q3:** What would change in your pipeline if this were a real-time credit approval system instead of batch predictions?