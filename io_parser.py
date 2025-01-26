import re
def parse_input(expression):
    tokens = re.findall(r'\d+|[-+*/]', expression)
    numbers = []
    operators = []

    for token in tokens:
        if token.isdigit():
            numbers.append(int(token))
        else:
            operators.append(token)

    return numbers, operators
