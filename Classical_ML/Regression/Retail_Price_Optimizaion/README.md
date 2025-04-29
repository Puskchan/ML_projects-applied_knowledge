# 🏷️ Retail Price Optimization

## 📝 Problem Statement

Built a dynamic pricing model to optimize retail prices by analyzing historical sales data and competitive pricing. The goal is to maximize revenue while maintaining market competitiveness.

## 🔍 Data Exploration Summary

### Key Features:

* Product categories with price variations
* Sales quantity and unit prices
* Competitor pricing (comp_1, comp_2, comp_3)
* Temporal features (weekday, holiday, seasonality)
* Product attributes (weight, description length, photos)

### Key Insights:

* Total price shows strong linear correlation with quantity
* Price variations across product categories:
  * Higher prices: health_beauty, watches_gifts
  * Lower prices: consoles_games, perfumery
* Seasonal patterns and holiday effects on pricing
* Competitive price differentials vary by product category

## 🏆 Model Comparison

Three approaches were implemented:


1. **Decision Tree Regressor**
   * Basic price prediction model
   * Used as baseline
2. **Random Forest Regressor**
   * Better performance than Decision Tree
   * More robust to outliers
   * Better handles non-linear relationships
3. **Bayesian Optimization**
   * Used for finding optimal prices
   * Considers price-demand elasticity
   * Maximizes revenue potential
4. **Deep Reinforcement Learning (DDPG)**
   * Dynamic pricing strategy
   * Adapts to market conditions
   * Best for real-time price optimization

**Final Choice**: DDPG (Deep Deterministic Policy Gradient)

* Handles dynamic market conditions
* Considers long-term revenue impact
* Balances exploration and exploitation

## ⚡ How to Run the Project


1. **Setup Environment**

```bash
pip install pandas numpy scikit-learn plotly bayesian-optimization stable-baselines3 gym
```


2. **Data Preparation**

* Place `retail_price.csv` in project directory
* Ensure data contains required columns:
  * product_id
  * unit_price
  * qty
  * product_category_name
  * comp_1, comp_2, comp_3


3. **Run Notebook**

```bash
jupyter notebook optimization.ipynb
```


4. **Model Training**

* Execute cells sequentially
* Key sections:
  * Data preprocessing
  * Feature engineering
  * Model training
  * Price optimization

## 🛠️ Technologies Used

* Python
* Pandas & NumPy
* Plotly
* Scikit-learn
* Bayesian Optimization
* Stable-baselines3 (DDPG)
* Gym


