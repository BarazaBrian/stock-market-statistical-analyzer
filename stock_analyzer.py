# Stock Market Statistical Analyzer
# This program calculates daily stock returns.

# Ask user to enter stock prices
import math

prices = input("Enter stock prices separated by spaces: ")

# Convert input into numbers
prices = [float(price) for price in prices.split()]

# Check if enough prices were entered
if len(prices) < 2:
    print("Please enter at least two stock prices.")

else:

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