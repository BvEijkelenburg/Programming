from tests.test_utils.test_runner import test_runner_safe


def test_analyzer():
    from exercises.les07.pe_7_2 import analyzer

    cases = [ [ "9-9-6-1-6-9-6-5-9-6-3-3", [1, 3, 3, 5, 6, 6, 6, 6, 9, 9, 9, 9], 9, 1, 12, 72, 6.0 ],
              [ "6-4-0-8-0-6-2-7-5-8", [0, 0, 2, 4, 5, 6, 6, 7, 8, 8], 8, 0, 10, 46, 4.6 ],
              [ "1-4-6-6-2-5", [1, 2, 4, 5, 6, 6], 6, 1, 6, 24, 4.0 ],
              [ "3-1", [1, 3], 3, 1, 2, 4, 2.0 ],
              [ "3-2-1-4-7", [1, 2, 3, 4, 7], 7, 1, 5, 17, 3.4 ],
              [ "4-3-2-7", [2, 3, 4, 7], 7, 2, 4, 16, 4.0 ],
              [ "6-4-2-0-7-6-7-4-6-2-0-4-4", [0, 0, 2, 2, 4, 4, 4, 4, 6, 6, 6, 7, 7], 7, 0, 13, 52, 4.0 ],
              [ "3-1-0-5-9-4-1-9-2-0-3-5", [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 9, 9], 9, 0, 12, 42, 3.5 ],
              [ "9-0-1-0-0-9-8-4", [0, 0, 0, 1, 4, 8, 9, 9], 9, 0, 8, 31, 3.875 ],
              [ "5-9", [5, 9], 9, 5, 2, 14, 7.0 ] ]

    for case in cases:
        result = analyzer(case[0])

        assert type(result) == tuple, 'helaas levert jouw functie nog geen tuple op!'
        assert len(result) == 6, 'helaas heeft jouw tuple niet de juiste lengte! ({} ipv {})'.format(len(result), 6)
        assert result[0] == case[1], 'helaas is de lijst nog niet correct gesorteerd! ({} ipv {})'.format(result[0], case[1])
        assert result[1] == case[2], 'helaas is de grootste waarde nog niet correct! ({} ipv {})'.format(result[1], case[2])
        assert result[2] == case[3], 'helaas is de kleinste waarde nog niet correct! ({} ipv {})'.format(result[2], case[3])
        assert result[3] == case[4], 'helaas is het aantal getallen nog niet correct! ({} ipv {})'.format(result[3], case[4])
        assert result[4] == case[5], 'helaas is de som van de getallen nog niet correct! ({} ipv {})'.format(result[4], case[5])
        assert result[5] == case[6], 'helaas is het gemiddelde van de getallen nog niet correct! ({} ipv {})'.format(result[5], case[6])


if __name__ == '__main__':
    test_runner_safe(test_analyzer, func_name="analyzer")
