from operations.multiply import multiply
from operations.add import add
from operations.utils import compare_strings

def exponentiate(base, exp):
    result = "1"
    current = "0"

    while compare_strings(current, exp) < 0:
        result = multiply(result, base)
        current = add(current, "1")

    return result
