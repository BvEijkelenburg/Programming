from tests.test_utils.test_runner import test_runner_safe

def test_expression(expression):
    type_mappings = {
        "<class 'int'>": ["integer", "Integer", "int"],
        "<class 'float'>": ["float"],
        "<class 'bool'>": ["Bool", "bool", "Boolean", 'boolean'],
        "<class 'str'>": ["string", "str", "String"]
    }

    expr_result = eval(expression)
    expr_type = type(expr_result)

    assert eval(input("Expressie: {}, uitkomst: ".format(expression))) == expr_result, "Dat is helaas niet de correct uitkomst voor deze expressie!\n"
    assert input("\tvan type: ") in type_mappings[str(expr_type)], "Dat type is helaas niet correct!\n"


if __name__ == '__main__':
    expressions = ["5", "5.0", "5%2", "5 > 1", "'5'", "5 * 2"]

    for expression in expressions:
        test_runner_safe(test_expression, func_params=(expression,), module_intro=False, test_intro=False)