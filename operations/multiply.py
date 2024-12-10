from operations.add import add

def multiply(num1, num2):
    result = "0"
    num1 = num1[::-1]

    for i, digit in enumerate(num1):
        carry = 0
        temp_result = []

        for d in num2[::-1]:
            product = (ord(digit) - ord('0')) * (ord(d) - ord('0')) + carry
            temp_result.append(chr((product % 10) + ord('0')))
            carry = product // 10

        if carry:
            temp_result.append(chr(carry + ord('0')))

        result = add(result, ''.join(temp_result[::-1]) + '0' * i)

    return result.lstrip('0') or '0'
