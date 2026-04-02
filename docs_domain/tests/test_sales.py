from sales import _row, total

def test_row_parses_valid_line():
    result = _row("coffee,drinks,12.5,3\n")
    
    assert result == {
        "name": "coffee",
        "category": "drinks", 
        "price": 12.5,
        "quantity": 3,
    }

def test_total_calculates_sum_with_discount():
    data = [
        {"name": "coffee", "category": "drinks", "price": 10.0, "quantity": 2},
        {"name": "tea", "category": "drinks", "price": 5.0, "quantity": 4},
    ]
    
    assert total(data) == 40.0
    assert total(data, 10) == 36.0