from tests.test_utils.test_runner import test_runner_safe


def test_sets():
    from exercises.les09.pe_9_1 import overeenkomst, verschil, totaal

    overeenkomst_exp = {'Best', 'Eindhoven', 'Boxtel'}
    verschil_exp = {'Deurne', 'Helmond', "Helmond 't Hout", 'Helmond Brouwhuis'}
    totaal_exp = {'Geldrop', 'Weert', 'Heeze', 'Best', 'Deurne', "Helmond 't Hout", 'Boxtel', 'Eindhoven', 'Helmond', 'Helmond Brouwhuis'}

    assert overeenkomst == overeenkomst_exp, 'variabele overeenkomst heeft niet de juiste waarde! ({} ipv {})'.format(overeenkomst_exp, overeenkomst)
    assert verschil == verschil_exp, 'variabele overeenkomst heeft niet de juiste waarde! ({} ipv {})'.format(verschil_exp, verschil)
    assert totaal == totaal_exp, 'variabele overeenkomst heeft niet de juiste waarde! ({} ipv {})'.format(totaal_exp, totaal)


if __name__ == '__main__':
    test_runner_safe(test_sets, func_name="de gevraagde sets")