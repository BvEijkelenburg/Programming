from tests.test_utils.test_runner import test_runner_safe


def test_code():
    from exercises.les09.pe_9_3 import code

    cases = [ [ "BartUtrecht CSAmsterdam CS", "EduwXwuhfkw#FVDpvwhugdp#FV" ],
              [ "RutteAlkmaarDen Helder", "UxwwhDonpdduGhq#Khoghu" ],
              [ "Brian123De UithofUtrecht CS", "Euldq456Gh#XlwkriXwuhfkw#FV" ] ]

    for case in cases:
        result = code(case[0])
        assert result == case[1], 'het coderen gaat niet goed! "{}" => {} ipv {}'.format(case[0], result, case[1])


if __name__ == '__main__':
    test_runner_safe(test_code, func_name="code()")