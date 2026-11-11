# Employee Bonus and Salary Calculator

A beginner-friendly Python program that calculates an employee's bonus and total monthly salary based on their monthly salary, years of experience, and performance rating.

## Project Overview

This program asks the user to enter an employee's name, monthly salary, years of experience, and performance rating. It checks whether the entered values are valid, then determines the bonus percentage using the employee's rating and experience.

Finally, it calculates and displays the bonus amount and total salary.

## Requirements

The program follows these input conditions:

- Monthly salary must be greater than zero.
- Years of experience cannot be negative.
- Performance rating must be between 1 and 5.

If any of these conditions is not met, the program displays an invalid-value message.

## Bonus Rules

| Performance Rating | Years of Experience | Bonus |
|---|---:|---:|
| 5 | 5 years or more | 30% |
| 5 | Less than 5 years | 20% |
| 4 | 3 years or more | 15% |
| 4 | Less than 3 years | 10% |
| 3 | Any experience | 5% |
| Below 3 | Any experience | 0% |

## Example

**Sample input:**
- Employee name: Ahmed
- Monthly salary: 1000
- Years of experience: 5
- Performance rating: 5

**Expected output:**

```text
Employee Name: Ahmed
Bonus: 30%
Bonus Amount: $300.0
Total Salary: $1300.0
```

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python employee_bonus.py
```

If your system uses the `python3` command, run:

```bash
python3 employee_bonus.py
```

## Concepts Used

- User input with `input()`
- Variables and arithmetic operations
- Conditional statements (`if`, `elif`, and `else`)
- Logical operators (`or`)
- Comparison operators
- Formatted strings (f-strings)

## Learning Purpose

This project was completed as part of a Python mentoring assignment to practise conditional statements, input validation, and basic calculations.

---
