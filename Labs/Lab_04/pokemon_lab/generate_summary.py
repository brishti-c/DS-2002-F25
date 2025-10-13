#!/usr/bin/env python3

import os
import sys
import pandas as pd


# -----------------------------
# Function 1: generate_summary
# -----------------------------
def generate_summary(portfolio_file):
    # Check if the portfolio file exists
    if not os.path.exists(portfolio_file):
        print(f"Error: File '{portfolio_file}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Load the CSV data
    df = pd.read_csv(portfolio_file)

    # Check if the DataFrame is empty
    if df.empty:
        print(f"The file '{portfolio_file}' is empty. No data to summarize.")
        return

    # Calculate total portfolio value
    total_portfolio_value = df["card_market_value"].sum()

    # Find the most valuable card
    most_valuable_idx = df["card_market_value"].idxmax()
    most_valuable_card = df.loc[most_valuable_idx]

    # Print the summary report
    print("===== Portfolio Summary =====")
    print(f"Total Portfolio Value: ${total_portfolio_value:,.2f}")
    print("Most Valuable Card:")
    print(f"  Name: {most_valuable_card.get('card_name', most_valuable_card.get('card_name_x', 'Unknown'))}")
    print(f"  ID: {most_valuable_card['card_id']}")
    print(f"  Market Value: ${most_valuable_card['card_market_value']:,.2f}")


# ------------------------
# Function 2: main()
# ------------------------
def main():
    generate_summary("card_portfolio.csv")


# ------------------------
# Function 3: test()
# ------------------------
def test():
    generate_summary("test_card_portfolio.csv")


# ------------------------
# Main Block
# ------------------------
if __name__ == "__main__":
    test()
