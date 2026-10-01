# Pattern Generator and Number Analyzer

## 📌 Project Description

**Pattern Generator and Number Analyzer** is a simple Python console-based program that allows users to:

1. Generate a star (`*`) pattern based on the number of rows.
2. Analyze a range of numbers to determine whether each number is **Even** or **Odd**.
3. Calculate the **sum of all numbers** within a given range.
4. Exit the program when the user is finished.

The program uses basic Python concepts such as **loops, conditional statements, user input, and arithmetic operations**.

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Interface:** Command Line / Console
* **Python Version:** Python 3.x

---

## ✨ Features

### 1. Generate a Pattern

The user enters the number of rows, and the program generates a right-angled star pattern.

**Example:**

```text
Enter the number of rows for the pattern: 5

Pattern:
*
**
***
****
*****
```

### 2. Analyze a Range of Numbers

The user enters a starting and ending number. The program:

* Checks every number in the range.
* Identifies whether the number is **Even** or **Odd**.
* Calculates the sum of all numbers in the range.

**Example:**

```text
Enter the start of the range: 1
Enter the end of the range: 5

Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
Number 5 is Odd

Sum of all numbers from 1 to 5 is: 15
```

### 3. Exit

Selecting option `3` terminates the program.

```text
Exiting the program. Goodbye!
```
https://drive.google.com/file/d/1pWezyuj3_ULuO7xBN_d3SPQqXEPlZ0Y1/view?usp=sharing
---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3.x is installed on your computer.

You can check the Python installation using:

```bash
python --version
```

### Step 2: Save the Program

Save the Python code in a file, for example:

```text
pattern_generator.py
```

### Step 3: Run the Program

Open Command Prompt or Terminal in the project folder and run:

```bash
python pattern_generator.py
```

---

## 📋 Program Menu

When the program starts, the following menu is displayed:

```text
Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
```

The user can select an option by entering `1`, `2`, or `3`.

---

## 🧠 Concepts Used

This project demonstrates the following Python concepts:

* `print()` function
* `input()` function
* Variables
* `if`, `elif`, and `else`
* `while` loop
* `for` loop
* `range()`
* Modulus operator `%`
* Arithmetic operations
* String multiplication
* `break` statement
* User input and menu-driven programming

---

## 📂 Project Structure

```text
Pattern-Generator-and-Number-Analyzer/
│
├── pattern_generator.py
└── README.md
```

---

## 🔢 Example Output

```text
Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit

Enter your choice: 2

Enter the start of the range: 1
Enter the end of the range: 10

Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
Number 5 is Odd
Number 6 is Even
Number 7 is Odd
Number 8 is Even
Number 9 is Odd
Number 10 is Even

Sum of all numbers from 1 to 10 is: 55
```

---

## 🎯 Purpose of the Project

The purpose of this project is to practice fundamental Python programming concepts by creating a simple interactive, menu-driven application.

