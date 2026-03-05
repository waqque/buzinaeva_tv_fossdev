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

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()    
    test_addition_duplicate()