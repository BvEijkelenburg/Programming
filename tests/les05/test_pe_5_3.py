from tests.test_utils.test_runner import test_runner_safe

def test_lang_genoeg():
    from exercises.les05.pe_5_3 import lang_genoeg

    txt_succes = "Je bent lang genoeg voor de attractie!"
    txt_failed = "Sorry, je bent te klein!"

    for lengte_test in [(-1, False), (0, False), (119, False), (120, True), (121, True), (190, True)]:
        result = lang_genoeg(lengte_test[0])
        if lengte_test[1]:
            assert txt_succes == result, 'helaas is de uitkomst nog niet correct! ({} => {})'.format(lengte_test[0], result)
        else:
            assert txt_failed == result, 'helaas is de uitkomst nog niet correct! ({} => {})'.format(lengte_test[0], result)


if __name__ == '__main__':
    test_runner_safe(test_lang_genoeg, func_name="lang_genoeg")