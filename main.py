import functions

def main():
    print("Welcome to the Stock Selection Tool!")
    
    # User Registration or Login
    while True:
        choice = input("Do you want to register (r) or login (l)? ").lower()
        if choice == 'r':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            functions.register_user(email, password)
            print("Registration successful!")
        elif choice == 'l':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if functions.authenticate_user(email, password):
                print("Login successful!")
                break
            else:
                print("Invalid credentials. Please try again.")
        else:
            print("Invalid choice. Please enter 'R' or 'L'.")

    # Stock Data Retrieval and Analysis
    ticker = input("Enter the stock ticker (e.g., 1155.KL for Maybank): ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    closing_prices = functions.get_closing_prices(ticker, start_date, end_date)
    if closing_prices is not None:
        print("Closing prices retrieved successfully!")
        analysis = functions.analyze_closing_prices(closing_prices)
        print("Analysis Results:")
        for key, value in analysis.items():
            print(f"{key}: {value}")
        
        # Save data to CSV
        filename = "user_data.csv"
        functions.save_to_csv (email, ticker, analysis, filename)
    
    # Option to read stored data
    choice = input("Do you want to read stored data? (yes/no): ").lower()
    if choice == 'yes':
        functions.read_from_csv(filename)

if __name__ == "__main__":
    main()