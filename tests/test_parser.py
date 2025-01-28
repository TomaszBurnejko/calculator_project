from calc.parser import tokenize, parse_expression

def test_tokenize():
    assert tokenize("3+5") == ['3', '+', '5']
    assert tokenize("10 + 20 - 30") == ['10', '+', '20', '-', '30']
    assert tokenize("(1+2)*3") == ['(', '1', '+', '2', ')', '*', '3']
    assert tokenize("4/2") == ['4', '/', '2']
    assert tokenize("3.5*2") == ['3.5', '*', '2']

def test_parse_expression():
    assert parse_expression(tokenize("3")) == 3.0
    assert parse_expression(tokenize("(1+2)")) == 3.0
    assert parse_expression(tokenize("2*(3+4)")) == 14.0
    assert parse_expression(tokenize("10/2")) == 5.0
    assert parse_expression(tokenize("3.5 * 2")) == 7.0
