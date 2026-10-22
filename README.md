# DSA Activity 1: Arithmetic Expression Parser for a Compiler

## Project Overview

This project demonstrates stack-based infix-to-postfix expression conversion using tokenization. It illustrates how arithmetic expressions are processed according to operator precedence, associativity, and parentheses rules.

The project contains two implementations: an interactive HTML visualizer and a Python program that performs the conversion and verifies the result by evaluating the postfix expression.

## Project Files

| File                  | Description                                                                                                      |
| --------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `visualizer.html`     | Interactive visualization of tokens, stack operations, and postfix output.                                       |
| `infix_to_postfix.py` | Python implementation of infix-to-postfix conversion with console-based execution steps and result verification. |
| `README.md`           | Project documentation and instructions.                                                                          |

## Algorithm

**Stack-Based Infix-to-Postfix Conversion Using Tokenization**

1. Tokenize the input expression into operands, operators, and parentheses.
2. Send operands directly to the output.
3. Push opening parentheses onto the stack.
4. For a closing parenthesis, pop operators until the matching opening parenthesis is found.
5. Compare operator precedence and associativity before pushing an operator.
6. Pop the remaining operators after processing all tokens.
7. Produce the final postfix expression.

## Example

**Infix Expression**

```text
A + B * (C - D)^E / F
```

**Postfix Expression**

```text
A B C D - E ^ * F / +
```

## Data Structure Used

**Stack:** Follows the Last In, First Out (LIFO) principle. It temporarily stores operators and parentheses during conversion.

The Python implementation uses a stack built with a Python list. The HTML implementation uses a JavaScript array for stack operations.

## Operator Precedence

| Operator | Precedence | Associativity     |
| -------- | ---------: | ----------------- |
| `^`      |          3 | Right-associative |
| `*`, `/` |          2 | Left-associative  |
| `+`, `-` |          1 | Left-associative  |

## Features

* Interactive HTML-based visualization.
* Token highlighting and stack visualization.
* Step-by-step execution.
* Previous, Next, and Show All controls.
* Python implementation with console-based execution steps.
* Postfix evaluation and comparison with the original infix expression.
* Basic handling of invalid characters and mismatched parentheses.

## Technologies Used

* HTML
* CSS
* JavaScript
* Python

## How to Run

### HTML Visualizer

1. Open `visualizer.html` in a web browser.
2. Enter an infix expression.
3. Click **Convert**.
4. Use the navigation buttons to explore the algorithm.

### Python Program

1. Install Python if it is not already installed.
2. Open a terminal in the project folder.
3. Run:

```bash
python infix_to_postfix.py
```

4. Enter an infix expression when prompted.
5. Provide values for variables when requested to verify the result.

## Complexity Analysis

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

Here, `n` is the number of tokens in the expression.

## Applications

* Compiler design and expression parsing.
* Arithmetic expression processing.
* Calculator implementation.
* Understanding stack-based algorithms.
* Learning operator precedence and associativity.

## Conclusion

This project demonstrates how stacks support infix-to-postfix conversion and expression evaluation. The HTML visualizer provides a graphical explanation, while the Python program demonstrates the algorithm and result verification through console output.
