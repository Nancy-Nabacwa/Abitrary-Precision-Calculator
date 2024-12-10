# from operations.add import add
# from operations.subtract import subtract
# from operations.multiply import multiply
# from operations.divide import divide
# from operations.exponentiate import exponentiate


# class ArbitraryPrecisionCalculator:
#     def __init__(self):
#         print("Welcome to the Arbitrary Precision Calculator!")
#         print("You can perform addition (+), subtraction (-), multiplication (*), division (/), and exponentiation (^).")
#         print("Type 'exit' to quit.\n")

#     def parse_and_calculate(self, expression):
#         try:
#             # Split the input into components
#             parts = expression.split()
#             if len(parts) != 3:
#                 return "Invalid input format. Use: <number1> <operator> <number2>"

#             num1, operator, num2 = parts
#             if operator == '+':
#                 return add(num1, num2)
#             elif operator == '-':
#                 return subtract(num1, num2)
#             elif operator == '*':
#                 return multiply(num1, num2)
#             elif operator == '/':
#                 return divide(num1, num2)
#             elif operator == '^':
#                 return exponentiate(num1, num2)
#             else:
#                 return f"Unsupported operator: {operator}"
#         except ValueError:
#             return "Invalid numbers. Please enter valid integers."
#         except Exception as e:
#             return f"Error: {e}"

#     def run(self):
#         while True:
#             expression = input("Enter a calculation (or type 'exit' to quit): ").strip()
#             if expression.lower() == 'exit':
#                 print("Goodbye!")
#                 break

#             result = self.parse_and_calculate(expression)
#             print(f"Result: {result}\n")


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
