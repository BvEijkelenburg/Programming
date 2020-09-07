from tests.test_utils.test_runner import test_runner_safe


def test_convert():
    from exercises.les06.pe_6_1 import convert

    for param in range(-100, 100):
        result = round(convert(param), 1)
        correct = round(param * 1.8 + 32, 1)

        assert correct == result, 'helaas is de uitkomst nog niet correct! ({} => {})'.format(param, result)


if __name__ == '__main__':
    test_runner_safe(test_convert, func_name="convert")