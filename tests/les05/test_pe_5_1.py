from tests.test_utils.test_runner import test_runner_safe

def test_som():
    from exercises.les05.pe_5_1 import som

    for i in range(-10, 10):
        for j in range(0, 10):
            for k in range(20, 30):
                assert i+j+k == som(i, j, k)
                params = (i, j, k)
                result = som(*params)

                assert i + j + k == result, 'helaas is de uitkomst nog niet correct! ({} => {})'.format(params, result)


if __name__ == '__main__':
    test_runner_safe(test_som, func_name="som")