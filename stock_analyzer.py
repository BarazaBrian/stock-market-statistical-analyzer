# Stock Market Statistical Analyzer
# This program calculates daily stock returns.

# Ask user to enter stock prices
import math
import matplotlib.pyplot as plt
import numpy as np

prices = input("Enter stock prices separated by spaces: ")

# Convert input into numbersclear
prices = [float(price) for price in prices.split()]

# Check if enough prices were entered
if len(prices) < 2:
    print("Please enter at least two stock prices.")
    print("\n--- Stock Market Analysis ---")
else:
    print("\n--- Stock Market Analysis ---")
    # Create empty list for daily returns
    daily_returns = []

    # Calculate daily returns
    for i in range(1, len(prices)):

        daily_return = ((prices[i] - prices[i - 1]) / prices[i - 1]) * 100

        daily_returns.append(daily_return)

    # Display results
    print("\nDaily Returns:")
    
    for index, value in enumerate(daily_returns, start=1):
        print(f"Day {index}: {value:.2f}%")
    
        # Calculate mean daily return
    mean_return = sum(daily_returns) / len(daily_returns)

    # Display mean return
    print(f"\nAverage Daily Return: {mean_return:.2f}%")
    

        # Interpret trend
    if mean_return > 0:
        print("Trend Analysis: Overall Upward Trend")

    elif mean_return < 0:
        print("Trend Analysis: Overall Downward Trend")

    else:
        print("Trend Analysis: Stable Trend")
            # Calculate variance
    variance = sum((x - mean_return) ** 2 for x in daily_returns) / len(daily_returns)

    # Calculate standard deviation
    std_deviation = math.sqrt(variance)

    # Display standard deviation
    print(f"Volatility (Standard Deviation): {std_deviation:.2f}")
        # Interpret volatility
    if std_deviation > 5:
        print("Risk Level: High Volatility")

    elif std_deviation > 2:
        print("Risk Level: Moderate Volatility")

    else:
        print("Risk Level: Low Volatility")
            # Find highest and lowest stock prices
    highest_price = max(prices)
    lowest_price = min(prices)

    # Display highest and lowest prices
    print(f"Highest Stock Price: {highest_price}")
    print(f"Lowest Stock Price: {lowest_price}")
        # Calculate price range
    price_range = highest_price - lowest_price

    # Display price range
    print(f"Price Range: {price_range}")
        # Create stock price graph
    plt.plot(prices)

    # Add graph title and labels
    plt.title("Stock Price Trend")
    plt.xlabel("Days")
    plt.ylabel("Stock Price")

    # Display graph
    plt.show()
    # Create stock price graph
    plt.figure()

    plt.plot(prices, marker='o')

    plt.title("Stock Price Trend")
    plt.xlabel("Days")
    plt.ylabel("Stock Price")
    plt.grid(True)

# Save FIRST
    plt.savefig("results/stock_price_trend.png")

# THEN show
    plt.show()

    # Calculate Moving Average (SMA with window size 3)
    window_size = 3
    moving_averages = []

    for i in range(len(prices)):

        if i < window_size - 1:
            continue

        window = prices[i - window_size + 1:i + 1]
        sma = sum(window) / window_size
        moving_averages.append(sma)

    print("\nMoving Average (3-day):", moving_averages)
        # Moving average graph
    plt.figure()

    plt.plot(range(window_size - 1, len(prices)), moving_averages, marker='o')
    plt.plot(prices, alpha=0.5)

    plt.title("Stock Price vs Moving Average")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.grid(True)

    plt.savefig("results/moving_average.png")
    plt.show()
        # Trend prediction using linear regression
    x = np.arange(len(prices))
    y = np.array(prices)

    # Fit line (slope + intercept)
    slope, intercept = np.polyfit(x, y, 1)

    # Predict next 3 days
    future_days = np.array([len(prices), len(prices)+1, len(prices)+2])
    predictions = slope * future_days + intercept

    print("\nPredicted Future Prices:")
    for i, price in enumerate(predictions, start=1):
        print(f"Day +{i}: {price:.2f}")

            # Plot prediction graph
    plt.figure()

    plt.plot(x, y, marker='o', label="Actual Prices")
    plt.plot(future_days, predictions, marker='o', linestyle='dashed', label="Predicted Prices")

    plt.title("Stock Price Prediction (Linear Trend)")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.grid(True)
    plt.legend()

    plt.savefig("results/prediction.png")
    plt.show()
