import yfinance as yf
import matplotlib.pyplot as plt
symbol = input("Enter Stock Symbol(e.g.,TCS.NS):")
data = yf.download(symbol, period="1mo")
if data.empty:
    print("No data found. Please check the symbol.")
else:
    print("\n  Stock Data Preview ")
    print(data.to_string())




