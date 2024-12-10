"""
 * ----------------------------------------------------------------------------
 *   Author         : Nancy Nabacwa
 *   Date           : December 10, 2024
 *   File           : calculator.py
 *   Title          : Calculator Logic
 *   Description    : This file contains the core logic for parsing user input
 *                    and routing it to the appropriate arithmetic operations.
 * ----------------------------------------------------------------------------
"""


from operations.add import add
from operations.subtract import subtract
from operations.multiply import multiply
from operations.divide import divide
from operations.exponentiate import exponentiate


class ArbitraryPrecisionCalculator:
    def parse_and_calculate(self, expression):
        try:
          
            parts = expression.split()
            if len(parts) != 3:
                return "Invalid input format. Use: <number1> <operator> <number2>"

            num1, operator, num2 = parts

            if operator == '+':
                return add(num1, num2)
            elif operator == '-':
                return subtract(num1, num2)
            elif operator == '*':
                return multiply(num1, num2)
            elif operator == '/':
                return divide(num1, num2)
            elif operator == '^':
                return exponentiate(num1, num2)
            else:
                return f"Unsupported operator: {operator}"
        except Exception as e:
            return f"Error: {e}"
