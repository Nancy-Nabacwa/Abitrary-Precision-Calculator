"""
 * ----------------------------------------------------------------------------
 *   Author         : Nancy Nabacwa
 *   Date           : December 10, 2024
 *   File           : main.py
 *   Title          : Entry Point for Arbitrary Precision Calculator
 *   Description    : This file contains the REPL loop, handles user inputs,
 *                    sanitizes inputs, and calls the main calculator logic.
 * ----------------------------------------------------------------------------
"""


from calculator import ArbitraryPrecisionCalculator

def sanitize_input(expression):
    try:

        parts = expression.split()
        if len(parts) != 3:
            return None, None, None

        num1, operator, num2 = parts

        
        if not num1.isdigit() or not num2.isdigit():
            return None, None, None

        return num1, operator, num2  
    except Exception:
        return None, None, None


if __name__ == "__main__":
    calc = ArbitraryPrecisionCalculator()

    print("Welcome to the Arbitrary Precision Calculator!")
    print("You can perform addition (+), subtraction (-), multiplication (*), division (/), exponentiation (^), etc.")
    print("Type 'exit' to quit.\n")

    while True:
       
        expression = input("Enter a calculation (e.g., 12345 + 67890): ").strip()
        if expression.lower() == 'exit':
            print("Goodbye!")
            break

      
        num1, operator, num2 = sanitize_input(expression)

        if num1 is None:
            print("Invalid input. Please enter a valid calculation.")
            continue

      
        result = calc.parse_and_calculate(f"{num1} {operator} {num2}")
        print(f"Result: {result}\n")
