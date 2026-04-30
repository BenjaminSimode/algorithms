def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    result = [0] * len(temperatures)
    
    for i, temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)

    return result


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # → [1, 1, 4, 2, 1, 1, 0, 0]
print(dailyTemperatures([30, 40, 50, 60]))                   # → [1, 1, 1, 0]
print(dailyTemperatures([30, 20, 10]))                       # → [0, 0, 0]
