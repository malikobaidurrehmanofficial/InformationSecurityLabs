def main():
    # Initialize dictionary with tuple keys (first_name, last_name)
    phone_book = {
        ('John', 'Doe'): '555-1234',
        ('Jane', 'Smith'): '555-5678',
        ('Bob', 'Johnson'): '555-9012',
        ('Alice', 'Williams'): '555-3456'
    }
    
    print("Phone Number Search")
    print("-------------------")
    
    while True:
        # Get user input
        first_name = input("\nEnter first name (or 'quit' to exit): ").strip()
        
        # Check if user wants to quit
        if first_name.lower() == 'quit':
            print("Goodbye!")
            break
            
        last_name = input("Enter last name: ").strip()
        
        # Create the search key
        search_key = (first_name, last_name)
        
        # Search for the phone number
        if search_key in phone_book:
            print(f"Phone number for {first_name} {last_name}: {phone_book[search_key]}")
        else:
            print(f"Sorry, no phone number found for {first_name} {last_name}.")
            
        # Option to continue or quit
        continue_search = input("\nWould you like to search again? (yes/no): ").strip().lower()
        if continue_search != 'yes':
            print("Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()


    