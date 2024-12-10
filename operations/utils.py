"""
 * ----------------------------------------------------------------------------
 *   Author         : Nancy Nabacwa
 *   Date           : December 10, 2024
 *   File           : utils.py
 *   Title          : Utility Functions
 *   Description    : This file contains helper functions, such as string
 *                    comparison, used across different arithmetic operations.
 * ----------------------------------------------------------------------------
"""


def compare_strings(num1, num2):
    if len(num1) > len(num2):
        return 1
    if len(num1) < len(num2):
        return -1
    return (num1 > num2) - (num1 < num2)
