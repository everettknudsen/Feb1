import pytest

@pytest.mark.parametrize("a,b,expected",[
    (2,3,-1),
    (10,3,7),
    (30,50,-20),
    (3,3,0),
    ])
def test_subtratction(a,b,expected):
    from subtraction import subtract_two_numbers

    answer = subtract_two_numbers(a,b)
    assert answer == expected
    

@pytest.mark.parametrize("ls,expect",[
    ([1,2,3,4],4),
    ([3,4,5,6],6),
    ([50,60,80,11],80),
    ])

def test_max(ls, expect):
    from subtraction import max_list

    answer = max_list(ls)
    assert answer == expect

@pytest.mark.parametrize("ls,expect",[
    ([1,2,3,4],1),
    ([3,4,5,6],3),
    ([50,60,80,11],11),
    ])

def test_min(ls, expect):
    from subtraction import min_list

    answer = min_list(ls)
    assert answer == expect
