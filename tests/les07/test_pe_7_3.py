from tests.test_utils.test_runner import test_runner_safe


def test_gemiddelde_per_student(cases):
    from exercises.les07.pe_7_3 import gemiddelde_per_student

    for case in cases:
        print(len(case[0]), end=": ")
        result = gemiddelde_per_student(case[0])

        assert len(result) == len(case[2]), 'het aantal gemiddelden is niet gelijk aan het aantal studenten! {} => {}'.format(case[2], result)

        for average_index in range(len(result)):
            average = round(result[average_index], 2)
            expected = round(case[2][average_index], 2)
            assert round(average, 2) == round(expected, 2), 'helaas is het gemiddelde per student nog niet correct! ({} => {} ipv {})'.format(case[0][average_index], average, expected)


def test_gemiddelde_van_alle_studenten(cases):
    from exercises.les07.pe_7_3 import gemiddelde_van_alle_studenten

    for case in cases:
        result = round(gemiddelde_van_alle_studenten(case[0]), 2)
        expected = round(case[1], 2)
        assert result == expected, 'helaas is het gemiddelde van alle student nog niet correct! ({} => {} ipv {})'.format(case[0], result, expected)


if __name__ == '__main__':
    cases = [ [[[17, 15, 30], [19, 46, 75]], 33.666666666666664, [20.666666666666668, 46.666666666666664]],
              [[[31, 96, 54], [16, 37, 56], [94, 64, 55], [41, 36, 66], [51, 16, 28], [99, 96, 45], [69, 38, 63], [52, 73, 72]], 56.16666666666667, [60.333333333333336, 36.333333333333336, 71.0, 47.666666666666664, 31.666666666666668, 80.0, 56.666666666666664, 65.66666666666667]],
              [[[93, 48, 36]], 59.0, [59.0]],
              [[[33, 60, 17], [84, 12, 50], [34, 77, 94], [88, 72, 24]], 53.75, [36.666666666666664, 48.666666666666664, 68.33333333333333, 61.333333333333336]],
              [[[71, 29, 77], [17, 32, 82], [83, 14, 90], [31, 58, 66], [14, 39, 72], [53, 53, 41], [19, 84, 67], [66, 77, 81], [46, 32, 65]], 54.03703703703704, [59.0, 43.666666666666664, 62.333333333333336, 51.666666666666664, 41.666666666666664, 49.0, 56.666666666666664, 74.66666666666667, 47.666666666666664]],
              [[[99, 46, 74], [44, 35, 27], [100, 17, 41], [24, 71, 48], [12, 41, 87], [31, 59, 56], [80, 32, 20]], 49.714285714285715, [73.0, 35.333333333333336, 52.666666666666664, 47.666666666666664, 46.666666666666664, 48.666666666666664, 44.0]],
              [[[35, 52, 64], [40, 48, 42], [62, 22, 17], [42, 16, 78], [82, 85, 14], [23, 54, 43], [49, 32, 13], [96, 71, 95], [80, 25, 54]], 49.407407407407405, [50.333333333333336, 43.333333333333336, 33.666666666666664, 45.333333333333336, 60.333333333333336, 40.0, 31.333333333333332, 87.33333333333333, 53.0]],
              [[[80, 55, 45], [25, 36, 39], [84, 69, 94], [60, 63, 66], [31, 61, 34], [33, 30, 51]], 53.111111111111114, [60.0, 33.333333333333336, 82.33333333333333, 63.0, 42.0, 38.0]],
              [[[71, 91, 42], [41, 14, 39], [41, 72, 70], [30, 14, 58], [20, 15, 57], [46, 24, 85], [74, 92, 61], [36, 27, 30]], 47.916666666666664, [68.0, 31.333333333333332, 61.0, 34.0, 30.666666666666668, 51.666666666666664, 75.66666666666667, 31.0]],
              [[[11, 74, 84], [35, 66, 26], [23, 90, 46], [10, 21, 81], [79, 51, 12], [44, 23, 38]], 45.22222222222223, [56.333333333333336, 42.333333333333336, 53.0, 37.333333333333336, 47.333333333333336, 35.0] ]]

    test_runner_safe(test_gemiddelde_per_student, func_name="gemiddelde_per_student", func_params=(cases,))
    test_runner_safe(test_gemiddelde_van_alle_studenten, func_name="gemiddelde_van_alle_studenten", func_params=(cases,), module_intro=False, test_intro=False)