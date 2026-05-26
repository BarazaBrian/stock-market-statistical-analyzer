#  Stock Market Statistical Analyzer

A Python-based project that applies **Probability and Statistics** to real-world stock market data.  
The system analyzes stock prices, computes statistical measures, visualizes trends, and provides simple predictions using linear regression.

##  Features

-  Stock price trend analysis
-  Daily return calculations
-  Mean (average return)
-  Volatility measurement (standard deviation)
-  Price range analysis
-  Moving average (trend smoothing)
-  Linear regression-based price prediction
-  Data visualization using graphs
-  Automatic saving of graphs and reports
-  Interactive menu-driven interface

##  Mathematical Concepts Used

This project applies key Probability and Statistics concepts:

- Percentage change (returns)
- Mean (average)
- Variance
- Standard deviation
- Moving averages
- Linear regression (trend prediction)

## Key Formulas

###  Daily Return

daily_return = ((prices[i] - prices[i - 1]) / prices[i - 1]) * 100

###  Mean (Average)

mean_return = sum(daily_returns) / len(daily_returns)

###  Standard Deviation (Volatility)

std_deviation = math.sqrt(sum((x - mean_return) ** 2 for x in daily_returns) / len(daily_returns))

##  Technologies Used

- Python 3
- NumPy
- Matplotlib
- Math library
- OS module (file handling)

## Data Visualization

The system generates and saves the following graphs:

- Stock price trend graph
- Daily returns graph
- Prediction graph
- Moving average trend graph

All outputs are saved in the `results/` folder.

## Project Structure
```
stock-market-statistical-analyzer/
│
├── stock_analyzer.py
└─results/ 
  ├── daily_returns.png
  ├── moving_average.png
  ├── prediction.png
  ├── stock_price_trend.png
  └──analysis_report.txt
```

##  How to Run

### 1. Install dependencies

```
pip install numpy matplotlib
```
### 2. Run the program

```
python stock_analyzer.py
```
## Author
[Baraza Brian](https://github.com/BarazaBrian)