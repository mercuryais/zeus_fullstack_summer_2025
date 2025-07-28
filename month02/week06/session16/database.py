entries = []

def add_entry(entry_content, entry_date):
    entry = {"content" : entry_content, "date" : entry_date}    
    entries.append(entry)

def get_entries():
    for entry in entries:
        print(f"{entry["date"]}\n{entry["content"]}\n\n")