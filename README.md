# Reminder CLI

## Description
The **Reminder CLI (Command Line Interface for reminders)** is a simple, console-based Python program that allows users to create, view, and delete reminders. It helps users set reminders with specific dates and times, including optional additional reminders before the scheduled event. The application is designed to work entirely offline and provides desktop notifications when a reminder is created.

## Features
- Add reminders with a specific **date** and **time**.
- Default reminder notification **30 minutes** before the scheduled time.
- Option to add up to **three additional reminder times**.
- View reminders in a tabular format.
- Delete reminders by name.
- Works **offline** without requiring an internet connection.
- **Desktop notifications** upon reminder creation.

## Requirements
- Python 3.6+
- Required Python packages:
  - `datetime` (Built-in)
  - `tabulate`
  - `plyer` (for desktop notifications)

## Setup and Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/Saisabari20/reminder-app.git
   cd reminder-cli
   ```
2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

## How to Use
1. **Run the application:**
   ```sh
   python reminder.py
   ```
2. **Choose an option from the menu:**
   - `1` - Create a new reminder.
   - `2` - View all reminders.
   - `3` - Delete a reminder.
   - `4` - Exit the program.

3. **Follow on-screen prompts** to enter reminder details.
4. The program will notify you **30 minutes before** the scheduled time.
5. Additional reminders (if set) will also trigger notifications at the specified times.

## Contributing
Feel free to fork this repository, make improvements, and submit a pull request. Contributions are always welcome!

## License
This project is open-source and available under the **MIT License**.

