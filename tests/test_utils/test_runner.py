import traceback

def test_runner_safe(test_func, func_name = "<no name>", func_params = tuple(), module_intro=True, test_intro=True):
    start_module = "====== Module output ======"
    start_tests = "\n======= Test output =======\n"

    try:
        if not test_intro:
            start_tests = ""

        if module_intro:
            print(start_module)

        test_output = test_func(*func_params)

        if test_intro:
            print(start_tests, end="")

        if test_output != None:
            print("{}".format(test_output))

        if func_name == "<no name>":
            print("Antwoord correct!")
        else:
            print("Je uitwerking voor {} lijkt correct!".format(func_name))

    except ImportError as ie:
        print("{}Foutmelding: de functie {} kon niet geïmporteerd worden. Heb je de functienaam correct geprogrammeerd?".format(start_tests, func_name))
    except NameError as e:
        print("{}Test gefaald: {}. Ben je misschien quotes om een string vergeten? Of heb je een naam verkeerd gespeld?".format(start_tests, e.args[0]))
    except AssertionError as e:
        print("{}Test gefaald: {}".format(start_tests, e.args[0]))
    except Exception as e:
        print("{}Je functie {} klopt nog niet, want er ging er iets mis! Python-error: \"{}\"".format(start_tests, func_name, e))
        print(traceback.format_exc())
