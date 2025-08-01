from database_sqlite import add_entry, get_entries, create_table
menu = """Please select one of the following options:
1. Add a new entry for today
2. View all entries
3. Exit

Your selection:
"""
welcome_message = "Welcome to the Programming Diary!"
print(welcome_message)  

create_table()

while (user_input := input(menu)) != "3":
    if user_input == '1':
        print("Adding...")
        entry_content = input("What did you learn today? ")
        entry_date = input("Enter the date : YYYY/MM/DD ")
        add_entry(entry_content, entry_date)
    elif user_input == '2':
        print("Viewing...")
        print(get_entries())
    else:
        print("Invalid selection. Please try again!")