from tests.test_utils.test_runner import test_runner_safe
import builtins, os, random


def new_open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
    if os.path.isabs(file):
        return old_open(file, mode, closefd=closefd)
    else:
        return old_open("../../exercises/les08/{}".format(file, mode, closefd=closefd))


def test_tickers_to_dict(expected_dict):
    from exercises.les08.pe_8_4 import tickers_to_dict

    tickers = tickers_to_dict('pe_8_4_tickers.txt')
    assert tickers == expected_dict, "de dictionary met tickers komt niet overeen met de (originele) inhoud van de file!"


def test_name_to_symbol(dict_param):
    from exercises.les08.pe_8_4 import name_to_symbol

    for i in range(len(dict_param) * 40): # omslachtig om niet teveel code weg te geven!
        key, value = random.choice(list(dict_param.items()))
        result = name_to_symbol(key, dict_param)
        assert result == value, 'helaas werd het verkeerde symbool bij de naam geleverd! {} => {}'.format(key, result)


def test_symbol_to_name(dict_param):
    from exercises.les08.pe_8_4 import symbol_to_name

    for i in range(len(dict_param) * 40):  # omslachtig om niet teveel code weg te geven!
        key, value = random.choice(list(dict_param.items()))
        result = symbol_to_name(value, dict_param)
        assert result == key, 'helaas werd het verkeerde symbool bij de naam geleverd! {} => {}'.format(key, result)


if __name__ == '__main__':
    old_open = builtins.open
    builtins.open = new_open

    ticker_dict = {'YAHOO': 'YHOO', 'GOOGLE INC': 'GOOG', 'Harley-Davidson': 'HOG', 'Yamana Gold': 'AUY', 'Sothebyâ€™s': 'BID', 'inBev': 'BUD'}

    test_runner_safe(test_tickers_to_dict, func_name="tickers_to_dict", func_params=(ticker_dict,))
    test_runner_safe(test_name_to_symbol, func_name="name_to_symbol", func_params=(ticker_dict,), module_intro=False, test_intro=False)
    test_runner_safe(test_symbol_to_name, func_name="symbol_to_name", func_params=(ticker_dict,), module_intro=False, test_intro=False)