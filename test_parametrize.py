import pytest
import matlib

@pytest.mark.parametrize("expected_input1, expected_input2, expected_output",
                            [
                                (5,5,25),
                                (6,3,18),
                                (9,3,27)
                            ]
                        )
def test_mul_with_input_output(expected_input1, expected_input2, expected_output):
    result = matlib.calc_mul(expected_input1,expected_input2)
    assert result == expected_output