
# Sales Data Calculator
# Veda Technology Internship - Task 4

def analyze_sales(sales):
    """Calculate basic sales statistics."""

    if not sales:
        raise ValueError("Sales data cannot be empty.")

    for value in sales:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("All sales values must be numeric.")

        if not 0 <= value < float("inf"):
            raise ValueError(
                "Sales values must be non-negative and finite."
            )

    total_sales = sum(sales)
    average_sales = total_sales / len(sales)
    highest_sale = max(sales)
    lowest_sale = min(sales)

    return {
        "count": len(sales),
        "total": total_sales,
        "average": average_sales,
        "highest": highest_sale,
        "lowest": lowest_sale
    }


def display_results(sales, results):
    """Display sales values and calculated statistics."""

    print("\n" + "=" * 45)
    print("           SALES DATA CALCULATOR")
    print("=" * 45)

    print("\nSales Records:")
    for index, sale in enumerate(sales, start=1):
        print(f"Sale {index:02d}: Rs. {sale:,.2f}")

    print("\n" + "-" * 45)
    print("              SALES SUMMARY")
    print("-" * 45)

    print(f"Number of Sales : {results['count']}")
    print(f"Total Sales     : Rs. {results['total']:,.2f}")
    print(f"Average Sales   : Rs. {results['average']:,.2f}")
    print(f"Highest Sale    : Rs. {results['highest']:,.2f}")
    print(f"Lowest Sale     : Rs. {results['lowest']:,.2f}")

    print("=" * 45)


def main():
    # Manually created sample sales dataset
    sales = [
        12000, 15000, 18000, 10000, 22000,
        25000, 14000, 30000, 17000, 27000
    ]

    try:
        results = analyze_sales(sales)
        display_results(sales, results)

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
