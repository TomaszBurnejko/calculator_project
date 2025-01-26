from io_parser import parse_input
import arithmetic_actions as actions

class Calculator:
    def calculate(self, expression):
        numbers, operators = parse_input(expression)

        if not numbers or len(operators) != len(numbers) - 1:
            raise ValueError("Invalid expression.")

        result = numbers[0]

        for i, operator in enumerate(operators):
            if operator == '+':
                result = actions.add(result, numbers[i + 1])
            elif operator == '-':
                result = actions.subtract(result, numbers[i + 1])
            elif operator == '*':
                result = actions.multiply(result, numbers[i + 1])
            elif operator == '/':
                result = actions.divide(result, numbers[i + 1])

        return result
