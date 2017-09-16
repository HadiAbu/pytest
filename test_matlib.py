import matlib
import pytest
import sys


@pytest.mark.skipif(sys.version_info > (3,5) ,reason="Demonstrating how to skip this test. python version is less than 3.5")
def test_calc_add( ):
    res = matlib.calc_add(4,5)
    assert res == 9

def test_calc_mul():
    res = matlib.calc_mul(10, 3)
    assert res == 30