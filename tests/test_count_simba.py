from hw4 import count_simba


def test_basic_case():
    strings = [
        "Simba and Nala are lions.",
        "I laugh in the face of danger.",
        "Hakuna matata",
        "Timon, Pumba and Simba are friends, but Simba could eat the other two."
    ]
    assert count_simba(strings) == 3


def test_single_occurrence():
    assert count_simba(["Simba"]) == 1


def test_multiple_occurrences_in_one_string():
    assert count_simba(["Simba Simba Simba"]) == 3


def test_no_occurrence():
    assert count_simba(["random text", "more random text"]) == 0


def test_mixed_case():
    strings = ["simba", "SIMBA", "SiMbA", "Simba"]
    assert count_simba(strings) == 1


def test_empty_list():
    assert count_simba([]) == 0


def test_empty_string():
    assert count_simba([""]) == 0


def test_with_special_characters():
    strings = ["Simba!", "(Simba)", "!SimbaSimba!", "Si)mba", "S!mba"]
    assert count_simba(strings) == 4


def test_with_numbers():
    strings = ["123Simba123", "11 Simba 11", "S1imba2"]
    assert count_simba(strings) == 2


def test_long_input():
    strings = ["Simba " * 100]
    assert count_simba(strings) == 100