import pandas as pd
import yfinance as yf
import csv

user_data = {}

def register_user(email, password):
    
    if '@' not in email:
        print("Invalid email address. Please include '@' in the email.")
        return False
    if email in user_data:
        print("User already exists.")
        return False
    user_data[email] = password
    return True

def authenticate_user(email, password):
    return user_data.get(email) == password
    
def get_closing_prices(ticker, start_date, end_date):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)
        if data.empty:
            print(f"No data found for {ticker} in the specified period.")
            return None
        return data['Close']
    except Exception as e:
        print(f"Error retrieving data for {ticker}: {e}")
        return None

def analyze_closing_prices(data):
    average_price = data.mean()
    percentage_change = ((data.iloc[-1] - data.iloc[0]) / data.iloc[0]) * 100
    highest_price = data.max()
    lowest_price = data.min()
    
    return {
        "Average Closing Price": average_price,
        "Percentage Change": percentage_change,
        "Highest Price": highest_price,
        "Lowest Price": lowest_price
    }

def save_to_csv (email, ticker, analysis, filename):
    try:
        data = analysis.copy() 
        data["Email"] = email
        data["Ticker"] = ticker

        file_exists = False
        try:
            pd.read_csv(filename)
            file_exists = True
        except FileNotFoundError:
            pass

        with open(filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)
        print(f"Data saved to {filename}.")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def read_from_csv(filename):
    try:
        data = pd.read_csv(filename)
        print(data)
    except FileNotFoundError:
        print("No data found. Please save some analysis results first.")
    except Exception as e:
        print(f"Error reading from CSV: {e}")