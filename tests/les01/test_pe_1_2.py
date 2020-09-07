from tests.test_utils.test_runner import test_runner_safe

def test_expression1():
    expression = input("Expressie voor Practice Exercise 1_2, onderdeel 1: ")
    assert 'Supercalifragilisticexpialidocious' in expression, 'de expressie bevat niet het woord "Supercalifragilisticexpialidocious"!'
    result = eval(expression)
    assert result == 34, 'helaas is de uitkomst nog niet correct! ({})'.format(result)


def test_expression2():
    expression = input("Expressie voor Practice Exercise 1_2, onderdeel 2: ")
    assert 'Supercalifragilisticexpialidocious' in expression, 'de expressie bevat niet het woord "Supercalifragilisticexpialidocious"!'
    assert 'ice' in expression, 'de expressie bevat niet het woord "ice"!'
    result = eval(expression)
    assert result == True, 'helaas is de uitkomst nog niet correct! ({})'.format(result)


def test_expression3():
    expression = input("Expressie voor Practice Exercise 1_2, onderdeel 3: ")
    assert 'Antidisestablishmentarianism' in expression, 'de expressie bevat niet het woord "Antidisestablishmentarianism"!'
    assert 'Honorificabilitudinitatibus' in expression, 'de expressie bevat niet het woord "Honorificabilitudinitatibus"!'
    result = eval(expression)
    assert result == True, 'helaas is de uitkomst nog niet correct! ({})'.format(result)


def test_expression4():
    expression = input("Expressie voor Practice Exercise 1_2, onderdeel 4: ")
    assert 'berlioz' in expression.lower(), 'de expressie bevat niet het woord "Berlioz"!'
    assert 'borodin' in expression.lower(), 'de expressie bevat niet het woord "Borodin"!'
    assert 'brian' in expression.lower(), 'de expressie bevat niet het woord "Brian"!'
    assert 'bartok' in expression.lower(), 'de expressie bevat niet het woord "Bartok"!'
    assert 'bellini' in expression.lower(), 'de expressie bevat niet het woord "Bellini"!'
    assert 'buxtehude' in expression.lower(), 'de expressie bevat niet het woord "Buxtehude"!'
    assert 'bernstein' in expression.lower(), 'de expressie bevat niet het woord "Bernstein"!'
    result = eval(expression)
    assert result == "Bartok", 'helaas is de uitkomst nog niet correct! ({})'.format(result)


def test_expression5():
    expression = input("Expressie voor Practice Exercise 1_2, onderdeel 5: ")
    assert 'berlioz' in expression.lower(), 'de expressie bevat niet het woord "Berlioz"!'
    assert 'borodin' in expression.lower(), 'de expressie bevat niet het woord "Borodin"!'
    assert 'brian' in expression.lower(), 'de expressie bevat niet het woord "Brian"!'
    assert 'bartok' in expression.lower(), 'de expressie bevat niet het woord "Bartok"!'
    assert 'bellini' in expression.lower(), 'de expressie bevat niet het woord "Bellini"!'
    assert 'buxtehude' in expression.lower(), 'de expressie bevat niet het woord "Buxtehude"!'
    assert 'bernstein' in expression.lower(), 'de expressie bevat niet het woord "Bernstein"!'
    result = eval(expression)
    assert result == "Buxtehude", 'helaas is de uitkomst nog niet correct! ({})'.format(result)


if __name__ == '__main__':
    test_runner_safe(test_expression1, module_intro=False, test_intro=False)
    test_runner_safe(test_expression2, module_intro=False, test_intro=False)
    test_runner_safe(test_expression3, module_intro=False, test_intro=False)
    test_runner_safe(test_expression4, module_intro=False, test_intro=False)
    test_runner_safe(test_expression5, module_intro=False, test_intro=False)
