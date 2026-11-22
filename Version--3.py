from datetime import datetime

first_name = input("Enter student first name: ")
last_name = input("Enter student last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")
event_year = int(input("Enter event year (YYYY): "))
event_month = int(input("Enter event month (1-12): "))
event_day = int(input("Enter event day (1-31): "))

# Clean and format strings
full_name = f"{first_name.strip()} {last_name.strip()}".title()
name_code = full_name.upper()
clean_section = section.strip().upper()
clean_event = event_name.strip().title()

# Format date into a readable string
event_date_obj = datetime(event_year, event_month, event_day)
formatted_date = event_date_obj.strftime("%B %-d, %Y")  # Use %#d instead of %-d if on Windows

print("\nStudent Event Registration Summary")
print(f"Name: {full_name}")
print(f"Name Code: {name_code}")
print(f"Section: {clean_section}")
print(f"Event: {clean_event}")
print(f"Event Date: {formatted_date}")
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("Registration record created successfully.")