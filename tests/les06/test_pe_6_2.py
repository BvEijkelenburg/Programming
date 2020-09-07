from tests.test_utils.test_runner import test_runner_safe
import builtins, os


def new_open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
    if os.path.isabs(file):
        return old_open(file, mode, closefd=closefd)
    else:
        return old_open("../../exercises/les06/{}".format(file, mode, closefd=closefd))


def test_pretty_print():
    from exercises.les06.pe_6_2 import pretty_print

    result = pretty_print()

    cards = { 325255: "Jan Jansen",
              334343: "Erik Materus",
              235434: "Ali Ahson",
              645345: "Eva Versteeg",
              534545: "Jan de Wilde",
              345355: "Henk de Vries" }

    for key, value in cards.items():
        expected = "{} heeft kaartnummer: {}".format(value, key)
        assert expected in result, 'helaas is de uitkomst nog niet correct! ("tekst {}" niet aangetroffen)'.format(expected)


if __name__ == '__main__':
    old_open = builtins.open
    builtins.open = new_open

    test_runner_safe(test_pretty_print, func_name="pretty_print")