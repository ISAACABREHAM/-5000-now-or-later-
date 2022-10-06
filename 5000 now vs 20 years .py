Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def invest(amount, rate, years):
    """Display year on year growth of an initial investment"""
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {year}: ${amount:,.2f}")

        
amount = float(input("Enter a principal amount: "))
Enter a principal amount: 5000
rate = float(input("Enter an annual rate of return: "))
Enter an annual rate of return: 0.1
years = int(input("Enter a number of years: "))
Enter a number of years: 20

invest (amount, rate, years)
year 1: $5,500.00
year 2: $6,050.00
year 3: $6,655.00
year 4: $7,320.50
year 5: $8,052.55
year 6: $8,857.81
year 7: $9,743.59
year 8: $10,717.94
year 9: $11,789.74
year 10: $12,968.71
year 11: $14,265.58
year 12: $15,692.14
year 13: $17,261.36
year 14: $18,987.49
year 15: $20,886.24
year 16: $22,974.86
year 17: $25,272.35
year 18: $27,799.59
year 19: $30,579.55
year 20: $33,637.50
