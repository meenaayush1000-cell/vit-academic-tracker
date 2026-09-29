# VIT Academic & Habit Tracker

## Overview
A lightweight, modular Command-Line Interface (CLI) application built in Python. Designed to help students organize assignment deadlines, log daily study hours, and monitor their overall productivity through a clean, interactive console dashboard.

## Features
- **Dashboard Analytics:** View real-time progress bars, completion percentages, and average study times.
- **Task Management:** Add, view, and mark academic tasks as completed.
- **Habit Tracking:** Log daily focused study or coding hours.
- **Data Persistence:** Automatically saves and loads user data using local JSON storage.
- **Modular Design:** Built using Object-Oriented Programming (OOP) principles and distinct package modules.

## Technologies Used
- Python 3.x
- Standard Python Libraries: `os`, `sys`, `json`, `datetime`, `array`

## How to Install and Run
1. Ensure Python 3 is installed on your system.
2. Clone this repository or download the project folder.
3. Open a terminal and navigate to the project directory:
   ```bash
   cd vit_tracker_project
4. Run the main application script:
   ```bash
   python3 main.py
## Testing Instructions
1. Launch the application and enter your name and registration number.
2. **Test Input Validation:** Select option 2 and try entering letters when prompted for a date or priority number. The system should catch the error and prompt you again.
3. **Test Core Logic:** Add a task, log 2.5 hours of study, and check the Dashboard (Option 1) to ensure the progress bar and averages calculate correctly.
4. **Test Persistence:** Select option 7 to save and exit. Relaunch the app using `python3 main.py` and check the Dashboard to verify your previous data loaded successfully.

## Screenshots