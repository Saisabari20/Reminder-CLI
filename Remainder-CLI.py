import datetime
import tabulate as tb
from plyer import notification

remainder_db = []


def create_remainder():
    current_date = datetime.datetime.now()

    while True:
        date_input = input("Enter a date (dd-mm-yyyy) or 'q' to cancel: ")
        if date_input.lower() == 'q':
            return None
        try:
            date_object = datetime.datetime.strptime(date_input, "%d-%m-%Y")
            formatted_schedule_date = date_object.strftime("%d-%b-%y")
            if current_date < date_object:
                break
            else:
                print("Enter a future date.")
        except ValueError:
            print("Invalid format. Use dd-mm-yyyy.")

    while True:
        time_input = input("Enter a time (hh:mm AM/PM) or 'q' to cancel: ")
        if time_input.lower() == 'q':
            return None
        try:
            time_object = datetime.datetime.strptime(time_input, "%I:%M %p")
            formatted_schedule_time = time_object.strftime("%I:%M %p")
            break
        except ValueError:
            print("Invalid format. Use hh:mm AM/PM.")

    remainder_name = input("Enter the remainder name: ")
    if any(rem["Remainder_Name"] == remainder_name for rem in remainder_db):
        print("Remainder with this name already exists.")
        return

    default_remainder = time_object - datetime.timedelta(minutes=30)
    formatted_default = default_remainder.strftime("%I:%M %p")

    add_remainder = input("Default is 30 minutes before. Add more? (y/n): ")
    additional_times = []

    if add_remainder.lower() == 'y':
        for i in range(3):
            while True:
                additional_time_input = input(
                    f"Enter additional remainder {i + 1} (hh:mm AM/PM) or press Enter to skip: ")
                if not additional_time_input:
                    break
                try:
                    additional_time_object = datetime.datetime.strptime(additional_time_input, "%I:%M %p")
                    formatted_additional_time = additional_time_object.strftime("%I:%M %p")
                    if formatted_additional_time not in additional_times:
                        additional_times.append(formatted_additional_time)
                        break
                    else:
                        print("This time is already added.")
                except ValueError:
                    print("Invalid format. Use hh:mm AM/PM.")

    new_remainder = {
        "Date": formatted_schedule_date,
        "Time": formatted_schedule_time,
        "Remainder_Name": remainder_name,
        "Default_time": formatted_default,
        "Additional_times": additional_times
    }

    remainder_db.append(new_remainder)
    print("Remainder created successfully!")

    notification.notify(
        title="Reminder Set",
        message=f"Your reminder '{remainder_name}' is scheduled at {formatted_schedule_time}",
        timeout=10
    )


def view_remainder():
    if not remainder_db:
        print("No remainders to display.")
        return
    header = ["Date", "Time", "Remainder_Name", "Default_time", "Additional_times"]
    table_data = [[item["Date"], item["Time"], item["Remainder_Name"], item["Default_time"],
                   ", ".join(item["Additional_times"]) if item["Additional_times"] else "N/A"] for item in remainder_db]
    print(tb.tabulate(table_data, headers=header, tablefmt="grid"))


def delete_remainder():
    global remainder_db
    if not remainder_db:
        print("No remainders to delete.")
        return

    delete_name = input("Enter the remainder name to delete: ")
    new_db = [rem for rem in remainder_db if rem["Remainder_Name"] != delete_name]
    if len(new_db) == len(remainder_db):
        print("Remainder not found.")
    else:
        remainder_db = new_db
        print(f"Remainder '{delete_name}' deleted successfully.")


print("\t\t\t **********************")
print("\t\t\t * Welcome to Reminder *")
print("\t\t\t **********************")

while True:
    print("1. Create Reminder")
    print("2. View Reminders")
    print("3. Delete Reminder")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            create_remainder()
        elif choice == 2:
            view_remainder()
        elif choice == 3:
            delete_remainder()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Choose between 1 and 4.")
    except ValueError:
        print("Invalid input. Enter a number.")
