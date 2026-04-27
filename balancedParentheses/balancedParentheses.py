def isBalanced(string: str) -> bool:
    if not string:
        return True
    
    mapping = { '(': ')', '{': '}', '[': ']'}
    stack = []

    for char in string:
        if char in mapping:
            stack.append(char)
        else:
            if not stack:
                return False
            
            if mapping[stack[-1]] == char:
                stack.pop()
            else:
                return False

    return len(stack) == 0

print(isBalanced(")]"))
