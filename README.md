# **Arbitrary Precision Integer Calculator**
In fields like cryptography, scientific research, and financial modelling, precision and scalability are vital. The **Arbitrary Precision Integer Calculator** addresses this need by performing calculations on numbers of virtually unlimited size.

This project is designed to simulate manual arithmetic using **string-based operations**, even in environments without native arbitrary precision capabilities (like C). It adheres to strict constraints while maintaining user-friendly functionality.

---

## **Features**

- **Core Arithmetic Operations**:
  - **Addition (`+`)**: Digit-by-digit summation with carry.
  - **Subtraction (`-`)**: Borrow-based subtraction.
  - **Multiplication (`*`)**: Repeated addition for partial products.
  - **Division (`/`)**: Digit-by-digit long division.
  - **Exponentiation (`^`)**: Repeated multiplication.

- **Arbitrary Precision**:
  - Handles numbers as large as the user can input, without truncation or overflow.

- **Interactive REPL**:
  - Provides a user-friendly interface for performing calculations interactively.

- **Robust Input Validation**:
  - Detects invalid inputs and handles edge cases (e.g., division by zero) gracefully.



## **Setup**

1. Clone the repository:
```
   git clone https://github.com/your-username/arbitrary-calculator.git
   cd arbitrary-calculator
```

2. Run the program:
```
   python3 main.py
```
## **Usage**

1. Start the calculator by running main.py.
2. Enter calculations naturally. For example:
```
12345 + 67890
987654321 * 123456789
2 ^ 10
```
Type ```exit``` to quit the program.

## **Examples**
Here are some sample calculations to showcase the capabilities of the calculator:

**Addition**
```
Input:  987654321987654321 + 123456789123456789
Output: 1111111111111111110
```
**Subtraction**
```
Input:  987654321987654321 - 123456789123456789
Output: 864197532864197532
```
**Multiplication**
```
Input:  123456789 * 987654321
Output: 121932631112635269
```
**Division**
```
Input:  987654321987654321 / 123456789123456789
Output: 8
```
**Exponentiation**
```
Input:  2 ^ 100
Output: 1267650600228229401496703205376
```
## **Detailed Documentation**

For a comprehensive overview of the project, including:
- **How it works**: Detailed explanations of operations.
- **Design decisions**: Why certain approaches were taken.

Please visit the detailed documentation [here](https://docs.google.com/document/d/109p8wuUDaO2Gi2b7d00ftEiG_f4VgNubo8a3OiAaXW0/edit?usp=sharing).

---
