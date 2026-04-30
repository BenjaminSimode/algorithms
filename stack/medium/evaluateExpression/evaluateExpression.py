def evaluate(expression: str) -> int:
    operator = '+'
    number = 0
    stack = []

    for i, char in enumerate(expression):
        if char.isdigit():
           number = number * 10 + int(char) # 1 -> 14 -> 143
        
        if not char.isdigit() or i == len(expression) - 1:
            if operator == '+':
                stack.append(number)
            elif operator == '-':
                stack.append(-number)
            elif operator == '*':
                stack.append(stack.pop() * number)
            elif operator == '/':
                stack.append(stack.pop() / number)
            operator = char
            number = 0

    return sum(stack)

print(evaluate("3+2*2"))    # → 7
print(evaluate("10/2+3"))   # → 8
print(evaluate("2*3+4*2"))  # → 14
print(evaluate("14-3*2"))   # → 8
print(evaluate("6/2+1"))    # → 4
