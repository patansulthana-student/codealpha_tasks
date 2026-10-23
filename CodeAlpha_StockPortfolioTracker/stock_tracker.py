
import csv

# Store predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

# Display welcome message
print("=" * 40)
print("   STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Store portfolio details
portfolio = []
total_portfolio_value = 0

# Get the number of stocks
while True:
    try:
        number_of_stocks = int(
            input("\nHow many different stocks do you want to add? ")
        )

        if number_of_stocks > 0:
            break
        else:
            print("Please enter a number greater than zero.")

    except ValueError:
        print("Invalid input! Please enter a whole number.")

# Enter stock details
for i in range(number_of_stocks):
    print(f"\nStock {i + 1}")

    stock_name = input("Enter stock name: ").strip().upper()

    if stock_name not in stock_prices:
        print("Sorry, this stock is not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity! Please enter a whole number.")
        continue

    if quantity <= 0:
        print("Please enter a quantity greater than zero.")
        continue

    # Calculate stock value
    stock_price = stock_prices[stock_name]
    stock_value = stock_price * quantity

    total_portfolio_value += stock_value

    # Save stock details in the portfolio list
    portfolio.append({
        "Stock": stock_name,
        "Price": stock_price,
        "Quantity": quantity,
        "Total Value": stock_value
    })

    print(f"Stock price: ${stock_price}")
    print(f"Quantity: {quantity}")
    print(f"Stock value: ${stock_value}")

# Display portfolio summary
print("\n" + "=" * 40)
print("        PORTFOLIO SUMMARY")
print("=" * 40)

if portfolio:
    for item in portfolio:
        print(
            f"{item['Stock']} - "
            f"Quantity: {item['Quantity']} - "
            f"Value: ${item['Total Value']}"
        )

    print(f"\nTotal portfolio value: ${total_portfolio_value}")

    # Save portfolio to CSV
    with open("portfolio.csv", "w", newline="") as file:
        fieldnames = ["Stock", "Price", "Quantity", "Total Value"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(portfolio)

    print("Portfolio saved successfully to portfolio.csv")

else:
    print("No valid stocks were added.")
    print("No portfolio file was created.")

print("\nThank you for using Stock Portfolio Tracker!")
