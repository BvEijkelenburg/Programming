from tests.test_utils.test_runner import test_runner_safe
import random

def test_kwadraten_som():
    from exercises.les05.pe_5_5 import kwadraten_som

    for i in range(0, 100):
        param = random.sample(range(-1000, 1000), k=10)
        squared_positives = sum([x**2 for x in param if x > 0])

        result = kwadraten_som(param)
        assert squared_positives == result, 'helaas is de uitkomst nog niet correct! ({} => {})'.format(param, result)


if __name__ == '__main__':
    test_runner_safe(test_kwadraten_som, func_name="kwadraten_som")