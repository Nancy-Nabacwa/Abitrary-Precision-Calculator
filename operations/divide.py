"""
 * ----------------------------------------------------------------------------
 *   Author         : Nancy Nabacwa
 *   Date           : December 10, 2024
 *   File           : divide.py
 *   Title          : Division Functionality
 *   Description    : This file implements string-based division for arbitrary
 *                    precision integers, simulating long division logic.
 * ----------------------------------------------------------------------------
"""


from operations.subtract import subtract
from operations.add import add
from operations.utils import compare_strings

def divide(num1, num2):
    if num2 == "0":
        return "Error: Division by zero is not allowed."

    quotient = []
    remainder = "0"

    for digit in num1:
        remainder = add(remainder, digit)
        count = "0"

        while compare_strings(remainder, num2) >= 0:
            remainder = subtract(remainder, num2)
            count = add(count, "1")

        quotient.append(count)

    return ''.join(quotient).lstrip('0') or '0'
