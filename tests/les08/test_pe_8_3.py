from tests.test_utils.test_runner import test_runner_safe


def test_hoogvliegers():
    from exercises.les08.pe_8_3 import hoogvliegers

    cases = [ [{"Gerald": 9.5, "Berend": 4.5, "Bart": 1.0, "Leo": 2.5, "Martin": 8.0, "Gera": 7.5, "Jan": 9.2, "David": 9.0, "Sanne": 8.2, "Brian": 10.0 }, {'Gerald': 9.5, 'Jan': 9.2, 'Brian': 10.0}],
              [{"Gerald": 1.0, "Berend": 3.5, "Bart": 2.0, "Leo": 3.5, "Martin": 7.0, "Gera": 4.5, "Jan": 8.2, "David": 8.1, "Sanne": 9.2, "Brian": 6.9}, {'Sanne': 9.2}],
              [{"Gerald": 9.4, "Berend": 8.5, "Bart": 4.0, "Leo": 9.5, "Martin": 5.0, "Gera": 3.5, "Jan": 6.2, "David": 4.8, "Sanne": 4.2, "Brian": 7.7}, {'Gerald': 9.4, 'Leo': 9.5}],
              [{"Gerald": 8.7, "Berend": 9.6, "Bart": 9.0, "Leo": 8.5, "Martin": 8.9, "Gera": 9.9, "Jan": 2.2, "David": 3.2, "Sanne": 5.2, "Brian": 4.5}, {'Berend': 9.6, 'Gera': 9.9}] ]

    for case in cases:
        result = hoogvliegers(case[0])
        assert result == case[1], 'helaas is het aantal hoogvliegers nog niet correct! ({} => {})'.format(case[0], result)


if __name__ == '__main__':
    test_runner_safe(test_hoogvliegers, func_name="hoogvliegers")