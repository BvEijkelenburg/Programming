from tests.test_utils.test_runner import test_runner_safe
import random, string, builtins


def input_simulator(*args, **kwargs):
    letters = string.ascii_lowercase

    result_str = ""
    for i in range(1, random.randint(1, 15)):
        length = random.randint(1, 15)
        result_str += ''.join(random.choice(letters) for i in range(length)) + " "

    generated_strings.append(result_str)
    return result_str


def test_gemiddelde():
    from exercises.les06.pe_6_5 import gemiddelde
    output = ""

    for i in range(10):
        result = gemiddelde()

        words_in_sentence_count = generated_strings[-1].strip().count(" ") + 1
        chars_in_sentence_count = len(generated_strings[-1].strip().replace(" ", ""))
        chars_based_on_result = int(round(words_in_sentence_count * result, 0))

        assert chars_based_on_result == chars_in_sentence_count, 'helaas is de uitkomst nog niet correct! ({} => {})'.format(generated_strings[-1], result)
        output += "{} => {}\n".format(generated_strings[-1], result)

    return output


if __name__ == '__main__':
    generated_strings = []
    builtins.input = input_simulator # to bypass the original input-function

    test_runner_safe(test_gemiddelde, func_name="gemiddelde")