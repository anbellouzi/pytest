import pytest, math
from gaurd_clauses import extract_position

def test_error_extract_position():
    input1 = '|error| numerical calculations could not converge.'
    assert extract_position(input1) == None

def test_update_extract_position():
    input1 = '|update| the positron location in the particle accelerator is x:21.432'
    assert extract_position(input1) == '21.432'
    
def test_empty_input():
    input1 = ''
    assert extract_position(input1) == None
    
