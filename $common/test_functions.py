import Misconceptions
import pytest

def test_1():
    assert 1==1

def test_assignCompares():
    # Exemples d'utilisation
    code_exemple1 = """
    if x = 4:
        pass
    """

    code_exemple2 = """
    if (x = 4):
        pass
    """

    code_exemple3 = """
    if (y == 5):
        pass
    """

    code_exemple4 = """
    if x == 4:
        pass
    """

    assert assignCompares(code_exemple1) == True
    assert assignCompares(code_exemple2) == True
    assert assignCompares(code_exemple3) == False
    assert assignCompares(code_exemple4) == False