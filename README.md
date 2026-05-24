# 📊 Stock Market Statistical Analyzer

A Python-based project that applies **Probability and Statistics** to real-world stock market data.  
The system analyzes stock prices, computes statistical measures, visualizes trends, and provides simple predictions using linear regression.

---

## 🚀 Features

- 📈 Stock price trend analysis
- 🔢 Daily return calculations
- 📊 Mean (average return)
- ⚖️ Volatility measurement (standard deviation)
- 📉 Price range analysis
- 📊 Moving average (trend smoothing)
- 🔮 Linear regression-based price prediction
- 📊 Data visualization using graphs
- 💾 Automatic saving of graphs and reports
- 🧭 Interactive menu-driven interface

---

## 🧠 Mathematical Concepts Used

This project applies key Probability and Statistics concepts:

- Percentage change (returns)
- Mean (average)
- Variance
- Standard deviation
- Moving averages
- Linear regression (trend prediction)

---

## 📌 Key Formulas

### 📈 Daily Return

:contentReference[oaicite:0]{index=0}

---

### 📊 Mean (Average)

:contentReference[oaicite:1]{index=1}

---

### ⚖️ Standard Deviation (Volatility)

:contentReference[oaicite:2]{index=2}

---

## 🛠️ Technologies Used

- Python 3
- NumPy
- Matplotlib
- Math library
- OS module (file handling)

---

## 📊 Data Visualization

The system generates and saves the following graphs:

- Stock price trend graph
- Daily returns graph
- Prediction graph
- Moving average trend graph

All outputs are saved in the `results/` folder.

---

## 📁 Project Structure

stock-market-statistical-analyzer/
│
├── stock_analyzer.py
├── README.md
├── results/
│ ├── stock_price_trend.png
│ ├── daily_returns.png
│ ├── prediction.png
│ ├── moving_average.png
│ ├── analysis_report.txt

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install numpy matplotlib

Run the program
python stock_analyzer.py

Enter stock prices when prompted

Example:

100 102 101 105 110
