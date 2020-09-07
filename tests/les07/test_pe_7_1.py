from tests.test_utils.test_runner import test_runner_safe


def test_seizoen():
    from exercises.les07.pe_7_1 import seizoen

    for param in range(1, 13):
        result = seizoen(param)
        if param < 3 or param == 12:
            assert result == "winter", 'helaas is de uitkomst nog niet correct! ({} => {})'.format(param, result)
        elif param < 6:
            assert result == "lente", 'helaas is de uitkomst nog niet correct! ({} => {})'.format(param, result)
        elif param < 9:
            assert result == "zomer", 'helaas is de uitkomst nog niet correct! ({} => {})'.format(param, result)
        elif param < 12:
            assert result == "herfst", 'helaas is de uitkomst nog niet correct! ({} => {})'.format(param, result)

    invalid = [ -10, -1, 0, 13, 14, 100 ]
    for param in invalid:
        result = seizoen(param)
        assert  result == "ongeldig", 'helaas is de uitkomst nog niet correct! ({} => {})'.format(param, result)


if __name__ == '__main__':
    test_runner_safe(test_seizoen, func_name="seizoen")