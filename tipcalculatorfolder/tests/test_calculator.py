from app.calculator import calculate_tip

def test_calculate_tip():
    assert calculate_tip(100, 10, 2) == 55
    assert calculate_tip(200, 15, 4) == 58
