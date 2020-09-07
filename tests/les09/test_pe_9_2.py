from tests.test_utils.test_runner import test_runner_safe


def test_monopolyworp():
    from exercises.les09.pe_9_2 import monopolyworp

    for i in range(100):
        result = monopolyworp()

        assert len(result) > 0, 'er moet minstens één keer een worp plaatsvinden! {}'.format(result)
        check_dices(result[0])

        if result[0][0] == result[0][1]:
            assert len(result) > 1, 'na de eerste keer dubbelgooien, moet nog een keer gegooid worden! {}'.format(result)
            check_dices(result[1])

            if result[1][0] == result[1][1]:
                assert len(result) == 3, 'na de tweede keer dubbelgooien, mag niet nog een keer gegooid worden! {}'.format(result)
                check_dices(result[2])


def check_dices(dices):
    assert len(dices) == 2, 'per worp moeten twee dobbelstenen gegooid worden!'
    assert 0 < dices[0] <= 6, 'dobbelsteen heeft een ongeldige waarde ({})!'.format(dices[0])
    assert 0 < dices[1] <= 6, 'dobbelsteen heeft een ongeldige waarde ({})!'.format(dices[1])


if __name__ == '__main__':
    test_runner_safe(test_monopolyworp, func_name="monopolyworp")