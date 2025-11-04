from hw5 import Patient
from math import isclose


def test_init_creates_patient_correctly():
    p = Patient("Misha", ["fever", "cough"])
    assert p.name == "Misha"
    assert p.symptoms == ["fever", "cough"]
    assert isinstance(p.tests, dict)
    assert p.tests == {}


def test_add_test_adds_result():
    p = Patient("Kitty", [])
    p.add_test("covid", True)
    assert "covid" in p.tests
    assert p.tests["covid"] is True


def test_has_covid_with_positive_test():
    p = Patient("Misha", ["fever"])
    p.add_test("covid", True)
    assert p.has_covid() == 0.99


def test_has_covid_with_negative_test():
    p = Patient("Kitty", ["cough"])
    p.add_test("covid", False)
    assert p.has_covid() == 0.01


def test_has_covid_without_test_no_symptoms():
    p = Patient("Misha", [])
    assert p.has_covid() == 0.05

def test_has_covid_with_one_symptom():
    p = Patient("Kitty", ["fever"])
    assert isclose(p.has_covid(), 0.15, rel_tol=1e-9)

def test_has_covid_with_two_symptoms():
    p = Patient("Misha", ["fever", "cough"])
    assert p.has_covid() == 0.25


def test_has_covid_with_three_symptoms():
    p = Patient("Kitty", ["fever", "cough", "anosmia"])
    assert p.has_covid() == 0.35


def test_probability_does_not_exceed_one():
    p = Patient("Misha", ["fever", "cough", "anosmia", "new_symptom"])
    # should not exceed 1.0
    assert p.has_covid() <= 1.0

def test_has_covid_true_branch():
    p = Patient("Misha", ["fever"])
    p.add_test("covid", True)
    assert p.has_covid() == 0.99

def test_has_covid_false_branch():
    p = Patient("Kitty", ["cough"])
    p.add_test("covid", False)
    assert p.has_covid() == 0.01

def test_has_covid_no_test_branch():
    p = Patient("Misha", ["fever", "anosmia"])
    result = p.has_covid()
    assert 0.05 < result < 1.0