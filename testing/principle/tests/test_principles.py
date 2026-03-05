import sys 
sys.path.append("../src")

#TODO make it with 'pip insfall -e.'
# Раннее тестирование позволяет сэкономить время позднее
# Тесты показывают наличие ошибок, а не отсутсвие
# Тесты не должны дублировать логику тестируемого кода
# Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты должны покрывать "кластеры" входных параметров
# Тесты должны обнаруживать новые ошибки (pescicide paradox)
# Тесты покрывают как успешные, так и ошибочные кейсы
# Тестовые функции должны тестировать логические блоки
# Одни и теже типы это pesticide paradox

from math_demo import (add, add_with_bug,calculate_tax_bugged, calculate_tax)
def test_addition():
    assert 2 + 2 == 4
    print("test ADDIOTION PASSED")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    #assert add_with_bug(6, 7) == 13 - will fail here
    #finally we found data that makes test reliable
    print("Test BUGGED ADDITION PASSED")

def test_addition_duplicate():
    assert add(6, 7) == 6+7
    print("test DUPLICATE ADDITION PASSED")

def test_addition_overkill():
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i, j) == i+j #violation of duplication
            assert add(-i, j) == -i+j
            assert add(-i, -j) == -i-j
            assert add(i, -j) == i-j
def test_addition_clusters():
    assert add(7, 6) == 13
    assert add(6, 7) == 13
    assert add(-7, 6) == -1
    assert add(1, 1) == 2
    assert add(-5, -5) == -10
    assert add(10, 3) == 13
    assert add(11, -1) == 10

    print("Test CLUSTERS PASSED")
def test_addition_commutative():
    assert add(7, 6) == 13
    assert add(6, 7) == 13
    print("Test COMMUTATIVE PASSED")

def test_tax_calculator():
    assert calculate_tax_bugged(1000) == 150
    assert calculate_tax_bugged(100) == 15
    assert calculate_tax_bugged(10) == 1.5
    assert calculate_tax_bugged(1) == 0.15
    assert calculate_tax_bugged(234) == 35.1
    print("test TAX CALCULATOR PASSED")
    
def test_tax_calculator_pesticide():
    assert calculate_tax(1000) == 150
    assert calculate_tax(100) == 15
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(234) == 35.1
    print("test PESTICIDE PASSED")

def test_negative_income():
    try:
        calculate_tax(-100)
    except ValueError as e:
        print("Test NEGATIVE INCOME PASSED")

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()    
    test_addition_duplicate()
    test_addition_clusters()
    test_addition_commutative()
    test_tax_calculator()
    test_tax_calculator_pesticide()
    #test_addition_overkill() #can try it on yout risk