def subtract(num1, num2):
    if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
        return '-' + subtract(num2, num1)

    num1, num2 = num1[::-1], num2[::-1]
    num2 = num2.ljust(len(num1), '0')

    borrow = 0
    result = []

    for i in range(len(num1)):
        digit1 = ord(num1[i]) - ord('0')
        digit2 = ord(num2[i]) - ord('0') + borrow

        if digit1 < digit2:
            digit1 += 10
            borrow = 1
        else:
            borrow = 0

        result.append(chr((digit1 - digit2) + ord('0')))

    return ''.join(result[::-1]).lstrip('0') or '0'
