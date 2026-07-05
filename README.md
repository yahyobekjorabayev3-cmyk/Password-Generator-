# Secure Password Generator

A lightweight, highly secure, and customizable Command Line Interface (CLI) password generator written in Python. This tool is designed with cybersecurity best practices in mind, ensuring generated passwords are cryptographically secure and resistant to brute-force attacks.

##  Features

* **Cryptographically Secure:** Powered by Python's `secrets` module instead of the standard `random` module to ensure true randomness suitable for security purposes.
* **Smart Complexity:** Automatically guarantees that every generated password contains at least one lowercase letter, one uppercase letter, one digit, and one special character.
* **Customizable Length:** Allows users to easily specify the desired length of the password (minimum 8 characters for optimal security).
* **No Dependencies:** Built entirely using Python's standard library—no external packages required.

## 🛠️ How It Works

Unlike standard pseudorandom generators, this script leverages standard security protocols to create unpredictable tokens. The process ensures:
1. Dynamic selection based on character pools (`string.ascii_letters`, `string.digits`, `string.punctuation`).
2. Immediate structural verification to enforce password strength policies.
3. Final array shuffling using a system-level randomizer to prevent pattern identification.

## Installation & Usage

### Prerequisites
Make sure you have **Python 3.x** installed on your system (or use mobile environments like **Pydroid 3** or **Pythonista**).

### Running the Script
1. Clone the repository or download the `password_generator.py` file.
2. Open your terminal or mobile IDE and run the following command:
   ```bash
   python password_generator.py
