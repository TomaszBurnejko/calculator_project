import re
import math

def tokenize(expression: str) -> list[str]:
    expression = re.sub(r'(\d)\s*\(', r'\1*(', expression)
    expression = re.sub(r'\√', 'sqrt', expression)
    tokens = re.findall(r'sqrt|\d+\.?\d*|[()+\-*/^]', expression)
    return tokens

def parse_expression(tokens: list[str]) -> float:
    if not tokens:
        return 0

    def parse_factor(tokens: list[str]) -> float:
        token = tokens.pop(0)
        if token.replace('.','',1).isnumeric():
            return float(token)
        if token == 'sqrt':
            return math.sqrt(parse_factor(tokens))
        if token == '(':
            result = parse_expression(tokens)
            tokens.pop(0)
            return result
        raise ValueError(f"Unexpected token: {token}")

    def parse_term(tokens: list[str]) -> float:
        result = parse_factor(tokens)

        while tokens and tokens[0] in ['*', '/', '^']:
            operator = tokens.pop(0)
            if operator == '*':
                result *= parse_factor(tokens)
            elif operator == '/':
                result /= parse_factor(tokens)
            elif operator == '^':
                result = math.pow(result, parse_factor(tokens))

        return result

    result = parse_term(tokens)

    while tokens and tokens[0] in ['+', '-']:
        operator = tokens.pop(0)
        if operator == '+':
            result += parse_term(tokens)
        else:
            result -= parse_term(tokens)

    return result
