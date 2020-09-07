from tests.test_utils.test_runner import test_runner_safe

def test_expression():
    default_list = [3, 7, -2, 12]
    answer = 14

    listname = input("Geef de naam van de lijst die je in je expressie gebruikt: ")
    expression = input("De expressie om het bereik van de lijst te bepalen: ")

    assert len(listname) > 0, "helaas geen lijstnaam opgegeven!"

    exec('{} = default_list'.format(listname))

    result =  eval(expression)
    assert result == answer, 'helaas is de uitkomst nog niet correct! ({} => {})'.format(default_list, result)


if __name__ == '__main__':
    test_runner_safe(test_expression, module_intro=False)