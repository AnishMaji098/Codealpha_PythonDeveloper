# Stock Portfolio Tracker
# Sample hardcoded prices only; these are not live market prices.

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 175
}


def show_available_stocks():
    print("\nAvailable stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol}: ${price:.2f}")


def get_portfolio():
    portfolio = {}
    print("\nEnter stock symbols and quantities.")
    print("Type 'done' when you have finished.\n")

    while True:
        symbol = input("Stock symbol: ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print("Invalid stock symbol. Please choose from the available stocks.\n")
            continue

        try:
            quantity = int(input(f"Quantity of {symbol}: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.\n")
                continue
        except ValueError:
            print("Please enter a valid whole number.\n")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.\n")

    return portfolio


def calculate_total(portfolio):
    total = 0
    for symbol, quantity in portfolio.items():
        total += STOCK_PRICES[symbol] * quantity
    return total


def display_summary(portfolio):
    print("\n========== PORTFOLIO SUMMARY ==========")

    if not portfolio:
        print("No stocks were added.")
        print("Total investment: $0.00")
        return 0

    print(f"{'STOCK':<10}{'QUANTITY':>10}{'PRICE':>12}{'VALUE':>14}")
    print("-" * 46)

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        print(f"{symbol:<10}{quantity:>10}{price:>12.2f}{value:>14.2f}")

    total = calculate_total(portfolio)
    print("-" * 46)
    print(f"TOTAL INVESTMENT: ${total:,.2f}")
    return total


def save_report(portfolio, total):
    filename = "portfolio_report.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 46 + "\n")
        file.write(f"{'STOCK':<10}{'QUANTITY':>10}{'PRICE':>12}{'VALUE':>14}\n")
        file.write("-" * 46 + "\n")

        for symbol, quantity in portfolio.items():
            price = STOCK_PRICES[symbol]
            value = price * quantity
            file.write(
                f"{symbol:<10}{quantity:>10}{price:>12.2f}{value:>14.2f}\n"
            )

        file.write("-" * 46 + "\n")
        file.write(f"TOTAL INVESTMENT: ${total:,.2f}\n")

    print(f"Report saved successfully as {filename}.")


def main():
    print("===================================")
    print("       STOCK PORTFOLIO TRACKER")
    print("===================================")

    show_available_stocks()
    portfolio = get_portfolio()
    total = display_summary(portfolio)

    if portfolio:
        choice = input("\nWould you like to save the report? (y/n): ").strip().lower()
        if choice == "y":
            save_report(portfolio, total)

    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
