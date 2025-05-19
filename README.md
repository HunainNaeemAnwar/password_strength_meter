# Password Strength Meter

**Description:**  
This is a simple and interactive web application built with Streamlit that evaluates the strength of user passwords. It checks for length, presence of uppercase and lowercase letters, digits, special characters, and verifies if the password is among commonly used weak passwords. The app provides clear feedback to help users improve their passwords and even suggests a strong, randomly generated password if theirs is weak.

---

## Features

- Checks if the password is too common  
- Validates minimum length (8 characters)  
- Ensures inclusion of uppercase and lowercase letters  
- Checks for numeric digits  
- Verifies presence of special characters (`!@#$^&*`)  
- Provides user-friendly feedback for weak or moderate passwords  
- Generates a strong, randomized password suggestion

## Technologies Used

- Python 3.x  
- Streamlit  
- Regular Expressions (`re`)  
- Random module

## Installation

1. Clone the repository:  
   ```bash
   git clone <repository-url>
   cd <repository-folder>

