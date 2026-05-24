import math
import os
import numpy as np
import matplotlib.pyplot as plt


# =========================
# STATISTICAL ANALYSIS
# =========================
def calculate_analysis(prices):

    daily_returns = []

    for i in range(1, len(prices)):
        daily_return = ((prices[i] - prices[i - 1]) / prices[i - 1]) * 100
        daily_returns.append(daily_return)

    mean_return = sum(daily_returns) / len(daily_returns)

    variance = sum((x - mean_return) ** 2 for x in daily_returns) / len(daily_returns)
    std_deviation = math.sqrt(variance)

    highest_price = max(prices)
    lowest_price = min(prices)
    price_range = highest_price - lowest_price

    return daily_returns, mean_return, std_deviation, highest_price, lowest_price, price_range


# =========================
# PREDICTION MODEL
# =========================
def predict_prices(prices):

    x = np.arange(len(prices))
    y = np.array(prices)

    slope, intercept = np.polyfit(x, y, 1)

    future_days = np.array([len(prices), len(prices)+1, len(prices)+2])
    predictions = slope * future_days + intercept

    return x, y, future_days, predictions


# =========================
# MAIN PROGRAM
# =========================

prices = input("Enter stock prices separated by spaces: ")
prices = [float(price) for price in prices.split()]

os.makedirs("results", exist_ok=True)

while True:

    print("\n--- STOCK ANALYZER MENU ---")
    print("1. Show Statistical Analysis")
    print("2. Show Graphs")
    print("3. Show Prediction")
    print("4. Exit")

    choice = input("Enter choice: ")

    # =========================
    # OPTION 1 - ANALYSIS
    # =========================
    if choice == "1":

        daily_returns, mean_return, std_deviation, highest_price, lowest_price, price_range = calculate_analysis(prices)

        print("\n--- ANALYSIS ---")
        print("Daily Returns:", daily_returns)
        print(f"Mean Return: {mean_return:.2f}%")
        print(f"Volatility: {std_deviation:.2f}")
        print(f"Highest Price: {highest_price}")
        print(f"Lowest Price: {lowest_price}")
        print(f"Price Range: {price_range}")

        if mean_return > 0:
            print("Trend: Upward")
        elif mean_return < 0:
            print("Trend: Downward")
        else:
            print("Trend: Stable")


    # =========================
    # OPTION 2 - GRAPHS
    # =========================
    elif choice == "2":

        daily_returns, _, _, _, _, _ = calculate_analysis(prices)

        # Stock price graph
        plt.figure()
        plt.plot(prices, marker='o')
        plt.title("Stock Price Trend")
        plt.xlabel("Days")
        plt.ylabel("Price")
        plt.grid(True)
        plt.savefig("results/stock_price_trend.png")
        plt.show()

        # Daily returns graph
        plt.figure()
        plt.plot(daily_returns, marker='o')
        plt.title("Daily Returns")
        plt.xlabel("Days")
        plt.ylabel("Return (%)")
        plt.grid(True)
        plt.savefig("results/daily_returns.png")
        plt.show()


    # =========================
    # OPTION 3 - PREDICTION
    # =========================
    elif choice == "3":

        x, y, future_days, predictions = predict_prices(prices)

        plt.figure()
        plt.plot(x, y, marker='o', label="Actual Prices")
        plt.plot(future_days, predictions, marker='o', linestyle='dashed', label="Predicted Prices")
        plt.title("Stock Price Prediction")
        plt.xlabel("Days")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)
        plt.savefig("results/prediction.png")
        plt.show()

        print("\nPredicted Prices:")
        for i, p in enumerate(predictions, 1):
            print(f"Day +{i}: {p:.2f}")


    # =========================
    # OPTION 4 - EXIT
    # =========================
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")