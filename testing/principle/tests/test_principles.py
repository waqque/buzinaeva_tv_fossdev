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
from math_demo import (add, add_with_bug)
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
if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()    
    test_addition_duplicate()
    test_addition_clusters()
    test_addition_commutative()
    #test_addition_overkill() #can try it on yout risk