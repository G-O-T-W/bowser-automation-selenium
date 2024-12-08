# Web Automation Tool

This project automates web interactions using Selenium. It provides both a Command Line Interface (CLI) and a Graphical User Interface (GUI) to perform tasks such as logging in, filling forms, and downloading files from a demo website.

## Features

- **CLI**: Allows automation via the command line with minimal user interaction.
- **GUI**: Provides an intuitive interface for users to interact with the tool visually.
- **Web Automation**: Handles browser interactions like form filling, file downloads, and more.
- **Cross-Platform**: Compatible with Linux, macOS, and Windows (with appropriate setup).

## Prerequisites

- **Python 3.8+**
- **Google Chrome** (latest version recommended)
- **ChromeDriver** (version must match your Google Chrome installation)

### Setting Up ChromeDriver

1. Download the appropriate version of ChromeDriver for your operating system from [here](https://chromedriver.chromium.org/downloads).
2. Place the `chromedriver` executable inside a folder named `chromedriver-linux/` (for Linux) or the equivalent folder for your operating system in the project directory.

   Example structure:
   ```plaintext
   project-directory/
   ├── chromedriver-folder/
   │   └── chromedriver
   ├── main.py
   ├── gui.py
   ├── ...
   ```
## Installation
1. Clone the repository
```bash
git clone https://github.com/your-username/web-automation-tool.git
cd web-automation-tool
```
2. Install the required Python libraries:
```bash
pip install selenium
```
3. Ensure ChromeDriver is placed correctly as described in the prerequisites.

## Usage
### CLI Mode
1. Open a terminal and navigate to the project directory.
2. Run the ```main.py``` script:
```bash
python3 main.py
```
3. The script performs the following tasks:
* Logs in with the provided credentials.
* Fills a form with user details.
* Downloads a file.

You can modify the hardcoded values (e.g., username, password, etc.) in the main.py script for custom inputs.

### GUI Mode
1. Run the ```gui.py``` script:
```bash
python3 gui.py
```
2. The GUI will open, allowing you to:
* Enter login credentials. 
* Fill out form details (Full Name, Email, Current Address, Permanent Address). 
* Submit the data to automate the browser interactions.

3. Use the "Close Browser" button to terminate the browser session.

## Troubleshooting
1. ChromeDriver Version Mismatch:
* Ensure the version of ChromeDriver matches the version of Google Chrome installed on your system.

2. Selenium Errors:
* Make sure the required Python libraries are installed and up-to-date:
```bash
pip install --upgrade selenium
```
3. GUI Issues:
* If tkinter is not installed, use the following command:
For Ubuntu/Debian:
```bash
sudo apt-get install python3-tk
```
* For macOS: Tkinter comes pre-installed with Python.
