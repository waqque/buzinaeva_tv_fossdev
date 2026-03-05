import sys 
sys.path.append("../src")

#TODO make it with 'pip insfall -e.'

from math_demo import add
def test_addition():
    assert 2 + 2 == 4
    print("test ADDIOTION PASSED")


if __name__ == "__main__":
    test_addition()