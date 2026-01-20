Phone Number Normalization

This project provides a Python utility to normalize Nepali phone numbers into a standard international format (+977).  
It removes spaces and dashes, validates supported number formats, and raises errors for invalid inputs.  
Automated unit tests are implemented using Pytest to ensure correctness and reliability.

---
 Features
     - Remove spaces and dashes.
    - If number starts with "+977" and has 10 digits after it → valid.
    - If number starts with "0" and has total length 11 → convert to +977 format.
    - If number has exactly 10 digits and starts with 98 or 97 → add +977.
    - Anything else is invalid.
    - Raises `ValueError` for invalid phone numbers.
 
Technologies Used

- Python
- Pytest
- Visual Studio Code




