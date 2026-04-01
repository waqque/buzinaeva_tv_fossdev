from tax.income import calculate_tax

def test_income_tax():
    assert calculate_tax(100) == 15
    print("test TAX PASSED")

if __name__ == "__main__":
    test_income_tax()