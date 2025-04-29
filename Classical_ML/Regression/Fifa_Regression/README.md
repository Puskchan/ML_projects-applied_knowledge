# 🎮 FIFA Player Rating Prediction

## 📌 Problem Statement
Built a regression model to predict FIFA player overall ratings based on various player attributes and statistics. The goal was to understand what factors contribute most to a player's overall rating and create an accurate prediction model.

## 🔍 Data Exploration Summary

### Initial Data Challenges
- Complex currency formats (€, M, K) in Value, Wage columns
- Mixed data types (numerical, categorical, datetime)
- Missing values in multiple columns
- Irrelevant columns like URLs and logos

### Key Preprocessing Steps
1. **Data Cleaning**
   - Converted currency values to numerical format
   - Standardized height/weight measurements
   - Handled missing values using mode/median
   - Removed irrelevant URL columns

2. **Feature Engineering**
   - Created BMI from height/weight
   - Added Wage-to-Value ratio
   - Calculated contract-related features (Years_since_joined, Remaining_Contract_Years)

3. **Outlier Treatment**
   ```python
   # Used IQR method for specific columns
   ['Value', 'Wage', 'Release_Clause', 'Weight']
   ```
   - Kept age outliers as they represent valid veteran players
   - Removed extreme weight outliers as they likely represented errors

4. **Feature Selection**
   - Used Mutual Information and Random Forest importance scores
   - Key predictive features included:
     - Potential
     - Value
     - Wage
     - Age
     - Position-related features

## 🏆 Model Comparison

Tested three different models:

1. **Linear Regression (Base Model)**
   - R² Score: ~0.85
   - Simple but showed heteroscedasticity in residuals

2. **Polynomial Regression (Degree 2)**
   - R² Score: ~0.89
   - Better fit but risk of overfitting

3. **Decision Tree (Final Choice)**
   - R² Score: ~0.87
   - Chosen because:
     - Good balance of accuracy and interpretability
     - Better handling of non-linear relationships
     - More robust to outliers
     - Less prone to overfitting (with max_depth=5)

## ⚡ How to Run the Project

1. **Setup Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Required Libraries**
   ```python
   pandas
   numpy
   scikit-learn
   seaborn
   matplotlib
   statsmodels
   ```

3. **Run the Notebook**
   - Open `multiple_regression.ipynb` in Jupyter Notebook
   - Run all cells sequentially
   - Key outputs:
     - Feature importance plots
     - Model comparison metrics
     - Residual plots

4. **Data Requirements**
   - Ensure `FIFA.csv` is in the same directory
   - File should contain player attributes and statistics

## 📈 Model Performance Metrics
- MAE: Shows average prediction error in overall rating
- RMSE: Indicates prediction accuracy
- R²: Explains variance in player ratings
