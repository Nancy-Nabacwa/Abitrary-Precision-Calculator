"""
 * ----------------------------------------------------------------------------
 *   Author         : Nancy Nabacwa
 *   Date           : December 10, 2024
 *   File           : add.py
 *   Title          : Addition Functionality
 *   Description    : This file implements string-based addition for arbitrary
 *                    precision integers by processing numbers digit by digit.
 * ----------------------------------------------------------------------------
"""


def add(num1, num2):
    num1, num2 = num1[::-1], num2[::-1]
    max_len = max(len(num1), len(num2))
    num1 = num1.ljust(max_len, '0')
    num2 = num2.ljust(max_len, '0')

    carry = 0
    result = []

    for i in range(max_len):
        digit_sum = (ord(num1[i]) - ord('0')) + (ord(num2[i]) - ord('0')) + carry
        result.append(chr((digit_sum % 10) + ord('0')))
        carry = digit_sum // 10

    if carry:
        result.append(chr(carry + ord('0')))

    return ''.join(result[::-1])
