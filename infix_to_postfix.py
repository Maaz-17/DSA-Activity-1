import re

# ---------- Stack data structure ----------
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.items.pop()

    def peek(self):
        return self.items[-1]          # top element (stack must not be empty)

    def is_empty(self):
        return len(self.items) == 0

    def show(self):
        return " ".join(self.items)    # bottom -> top


# ---------- Operator rules ----------  
PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

def should_pop(top, current):
    """Should the operator on top of the stack go to the output first?"""
    if top == "(":
        return False
    if PRECEDENCE[top] > PRECEDENCE[current]:
        return True
    # equal precedence: pop only if left-associative ( ^ is right-associative )
    if PRECEDENCE[top] == PRECEDENCE[current] and current != "^":
        return True
    return False


# ---------- Step 1: tokenization ----------
def tokenize(expression):
    """Split the expression into operands, operators and parentheses."""
    tokens = re.findall(r"[A-Za-z_]\w*|\d+(?:\.\d+)?|[-+*/^()]", expression)
    if "".join(tokens) != expression.replace(" ", ""):
        raise ValueError("Invalid character in expression")
    return tokens


# ---------- Step 2: conversion ----------
def infix_to_postfix(expression, show_steps=False):
    tokens = tokenize(expression)
    stack = Stack()
    output = []

    if show_steps:
        print("Tokens:", tokens)
        print(f"\n{'Step':<6}{'Token':<10}{'Stack':<16}Output")
        print("-" * 50)

    for step, token in enumerate(tokens, start=1):
        if token == "(":
            stack.push(token)

        elif token == ")":
            while not stack.is_empty() and stack.peek() != "(":
                output.append(stack.pop())
            if stack.is_empty():
                raise ValueError("Mismatched parentheses")
            stack.pop()                          # remove "("

        elif token in PRECEDENCE:                # operator
            while not stack.is_empty() and should_pop(stack.peek(), token):
                output.append(stack.pop())
            stack.push(token)

        else:                                    # operand
            output.append(token)

        if show_steps:
            print(f"{step:<6}{token:<10}{stack.show():<16}{' '.join(output)}")

    while not stack.is_empty():                  # pop what is left
        top = stack.pop()
        if top == "(":
            raise ValueError("Mismatched parentheses")
        output.append(top)

    if show_steps:
        print(f"{'end':<16}{'':<16}{' '.join(output)}\n")

    return " ".join(output)


# ---------- Step 3: verification ----------
def evaluate_postfix(postfix, values):
    stack = Stack()
    for token in postfix.split():
        if token in PRECEDENCE:
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.push(left + right)
            elif token == "-":
                stack.push(left - right)
            elif token == "*":
                stack.push(left * right)
            elif token == "/":
                stack.push(left / right)
            else:
                stack.push(left ** right)
        else:
            stack.push(values[token])
    return stack.pop()


def verify(infix, postfix):
    """Evaluate the postfix and the original infix with the same values."""
    values = {}
    for token in tokenize(infix):
        if token not in PRECEDENCE and token not in ("(", ")") and token not in values:
            try:
                values[token] = float(token)                    # a number like 2
            except ValueError:
                values[token] = float(input(f"Enter value of {token}: "))

    postfix_result = evaluate_postfix(postfix, values)

    # Python understands ** for power, so convert ^ and put values in
    parts = []
    for token in tokenize(infix):
        parts.append(str(values[token]) if token in values else token.replace("^", "**"))
    infix_result = eval(" ".join(parts))

    print("Postfix result:", postfix_result)
    print("Infix result  :", infix_result)
    print("Verified!" if abs(postfix_result - infix_result) < 1e-9 else "Mismatch!")


# ---------- Main ----------
def main():
    try:
        infix = input("Enter infix expression: ")
        if not infix.strip():
            raise ValueError("Expression cannot be empty")

        postfix = infix_to_postfix(infix, show_steps=True)
        print("Postfix expression:", postfix)

        print("\n--- Verification ---")
        verify(infix, postfix)

    except (ValueError, ZeroDivisionError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
