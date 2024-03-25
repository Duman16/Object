def is_valid_sequence(sequence):
    stack = []
    brackets_map = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or brackets_map[char] != stack.pop():
                return "no"

    return "yes" if not stack else "no"

# Пример использования
print(is_valid_sequence("()[](([{}]))"))  # Должно вывести "yes"
print(is_valid_sequence("[(]]"))         # Должно вывести "no"
