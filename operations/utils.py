def compare_strings(num1, num2):
    if len(num1) > len(num2):
        return 1
    if len(num1) < len(num2):
        return -1
    return (num1 > num2) - (num1 < num2)
