# Simple Keylogger with GUI

Welcome to the **Simple Keylogger with GUI**! This is a basic keylogger tool that allows you to log key presses and save them to a file in a directory of your choice, all through a user-friendly graphical interface.

## Features

- **Start Keylogger**: Begin logging keystrokes and save them to a text file.
- **Stop Keylogger**: Stop the logging process when you're done.
- **View Logs**: Open and view the captured keystrokes in a scrollable window.
- **Select Directory**: Choose the directory where you want to save the log file.

This project is built using Python's `pynput` library for capturing keystrokes and `tkinter` for the GUI components.

## How to Run

1. **Clone the repository**:
    ```
    git clone https://github.com/your-username/simple-keylogger-with-gui.git
    cd simple-keylogger-with-gui
    ```

2. **Install the required libraries**:
    ```
    pip install pynput
    ```

3. **Run the program**:
    ```
    python keylogger.py
    ```

4. **Select a directory**: Use the "Select Directory" button to choose where the keylogs should be saved.

5. **Start the keylogger**: Hit "Start Keylogger" to begin capturing keystrokes.

6. **Stop the keylogger**: Use "Stop Keylogger" to stop the capture at any time.

7. **View logs**: You can check what has been logged by clicking "View Logs."

## How It Works

This keylogger works by using the `pynput` library to listen for keypresses in the background. Each keypress is written to a log file, and when the `Enter` key is pressed, it adds a new line to the log.

The GUI is powered by `tkinter`, making it easy to start, stop, and view logs directly from the interface without needing to interact with the console.

## Notes

- This tool is intended for educational purposes. Please respect privacy and only use this keylogger on systems you have permission to monitor.
- Ensure that you select a directory before starting the keylogger to avoid any issues with log saving.

## Future Improvements

- Add encryption for log files to protect sensitive data.
- Improve log formatting for better readability.
- Implement more advanced filtering options (e.g., excluding specific key sequences).

## Contributing

Feel free to fork this repository and submit pull requests with improvements or bug fixes. All contributions are welcome!

## License

This project is licensed under the MIT License.

---

Thanks for checking out this simple keylogger project! If you have any questions or feedback, feel free to open an issue or reach out.

Happy coding! 😊

