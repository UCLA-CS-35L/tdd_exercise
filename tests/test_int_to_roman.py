from src.roman.int_to_roman import to_roman

def test_convert_1_to_I():
    assert to_roman(1) == 'I'

def test_convert_2_to_II():
    assert to_roman(2) == 'II'