# 🏧 ATM Machine System (Python - Modular Architecture)

## 🔹 Overview

This is a Command-Line Interface (CLI) based ATM Machine System built using Python.
The project follows a **modular (package-like) architecture**, where different functionalities are separated into individual files for better maintainability and scalability.

---

## 🔹 Features

* 💰 Display account balance
* ➕ Deposit money
* ➖ Withdraw money
* ⚠️ Handles invalid and insufficient balance cases
* 🔁 Menu-driven interaction system
* 🧩 Modular code structure (separate files for each functionality)

---

## 🔹 Project Structure

```
ATM-System/
│
├── main.py                # Entry point of the program
├── utils.py               # Stores balance and core logic
├── DEPOSIT_MONEY.py       # Deposit functionality
├── DISPLAY_BALANCE.py     # Display balance
├── WITHDRAW_MONEY.py      # Withdraw functionality
├── README.md
└── .gitignore
```

---

## 🔹 Technologies Used

* Python
* CLI (Command Line Interface)

---

## 🔹 How It Works

* The system maintains a global variable `balance` (stored in `utils.py`)
* Each operation (deposit, withdraw, display) is implemented in separate modules
* `main.py` acts as the controller and handles user interaction
* Functions are imported and executed based on user choice

---

## 🔹 How to Run

1. Clone the repository:
   git clone https://github.com/Tanishk479/ATM-System.git

2. Navigate to the folder:
   cd ATM-System

3. Run the program:
   python main.py

---

## 🔹 Key Learning Outcomes

* Modular programming in Python
* Function separation across multiple files
* Basic financial logic implementation
* CLI-based user interaction
* Version control using Git and GitHub

---

## 🔹 Future Improvements

* Add PIN authentication system 🔐
* Add transaction history 📜
* Support multiple users 👥
* Store data using files or database 💾

---

## 🔹 Author

Tanishk

