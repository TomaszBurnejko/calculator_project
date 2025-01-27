import re

def tokenize(expression: list) -> list:
    tokens = re.findall(r'\d+\.?\d*|[()+\-*/]', expression)
    return tokens

def parse_expression(tokens: list) -> float:
    if not tokens:
        return 0

    def parse_factor(tokens: list):
        token = tokens.pop(0)
        if token.isdigit():
            return float(token)
        elif token == '(':
            result = parse_expression(tokens)
            tokens.pop(0)  # remove closing parenthesis
            return result
        else:
            raise ValueError(f"Unexpected token: {token}")

    def parse_term(tokens):
        result = parse_factor(tokens)

        while tokens and tokens[0] in ['*', '/']:
            operator = tokens.pop(0)
            if operator == '*':
                result *= parse_factor(tokens)
            else:
                result /= parse_factor(tokens)

        return result

    result = parse_term(tokens)

    while tokens and tokens[0] in ['+', '-']:
        operator = tokens.pop(0)
        if operator == '+':
            result += parse_term(tokens)
        else:
            result -= parse_term(tokens)

    return result
