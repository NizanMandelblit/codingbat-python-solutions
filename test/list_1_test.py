from src.list_1 import *


def test_first_last6():
    assert first_last6([1, 2, 6]) == True
    assert first_last6([6, 1, 2, 3]) == True
    assert first_last6([13, 6, 1, 2, 3]) == False
    assert first_last6([13, 6, 1, 2, 6]) == True
    assert first_last6([3, 2, 1]) == False
    assert first_last6([3, 6, 1]) == False
    assert first_last6([3, 6]) == True
    assert first_last6([6]) == True
    assert first_last6([3]) == False
    assert first_last6([5, 6]) == True
    assert first_last6([5, 5]) == False
    assert first_last6([1, 2, 3, 4, 6]) == True
    assert first_last6([1, 2, 3, 4]) == False


def test_same_first_last():
    assert same_first_last([1, 2, 3]) == False
    assert same_first_last([1, 2, 3, 1]) == True
    assert same_first_last([1, 2, 1]) == True
    assert same_first_last([7]) == True
    assert same_first_last([]) == False
    assert same_first_last([1, 2, 3, 4, 5, 1]) == True
    assert same_first_last([1, 2, 3, 4, 5, 13]) == False
    assert same_first_last([13, 2, 3, 4, 5, 13]) == True
    assert same_first_last([7, 7]) == True


def test_make_pi():
    assert make_pi() == [3, 1, 4]


def test_common_end():
    assert common_end([1, 2, 3], [7, 3]) == True
    assert common_end([1, 2, 3], [7, 3, 2]) == False
    assert common_end([1, 2, 3], [1, 3]) == True
    assert common_end([1, 2, 3], [1]) == True
    assert common_end([1, 2, 3], [2]) == False


def test_sum3():
    assert sum3([1, 2, 3]) == 6
    assert sum3([5, 11, 2]) == 18
    assert sum3([7, 0, 0]) == 7
    assert sum3([1, 2, 1]) == 4
    assert sum3([1, 1, 1]) == 3
    assert sum3([2, 7, 2]) == 11


def test_rotate_left3():
    assert rotate_left3([1, 2, 3]) == [2, 3, 1]
    assert rotate_left3([5, 11, 9]) == [11, 9, 5]
    assert rotate_left3([7, 0, 0]) == [0, 0, 7]
    assert rotate_left3([1, 2, 1]) == [2, 1, 1]
    assert rotate_left3([0, 0, 1]) == [0, 1, 0]


def test_reverse3():
    assert reverse3([1, 2, 3]) == [3, 2, 1]
    assert reverse3([5, 11, 9]) == [9, 11, 5]
    assert reverse3([7, 0, 0]) == [0, 0, 7]
    assert reverse3([2, 1, 2]) == [2, 1, 2]
    assert reverse3([1, 2, 1]) == [1, 2, 1]
    assert reverse3([2, 11, 3]) == [3, 11, 2]
    assert reverse3([0, 6, 5]) == [5, 6, 0]
    assert reverse3([7, 2, 3]) == [3, 2, 7]


def test_max_end3():
    assert max_end3([1, 2, 3]) == [3, 3, 3]
    assert max_end3([11, 5, 9]) == [11, 11, 11]
    assert max_end3([2, 11, 3]) == [3, 3, 3]
    assert max_end3([11, 3, 3]) == [11, 11, 11]
    assert max_end3([3, 11, 11]) == [11, 11, 11]
    assert max_end3([2, 2, 2]) == [2, 2, 2]
    assert max_end3([2, 11, 2]) == [2, 2, 2]
    assert max_end3([0, 0, 1]) == [1, 1, 1]

def test_sum2():
    assert sum2([1, 2, 3]) == 3
    assert sum2([1, 1]) == 2
    assert sum2([1, 1, 1, 1]) == 2
    assert sum2([1, 2]) == 3
    assert sum2([1]) == 1
    assert sum2([]) == 0
    assert sum2([4, 5, 6]) == 9
    assert sum2([4]) == 4


def test_middle_way():
    assert middle_way([1, 2, 3], [4, 5, 6]) == [2, 5]
    assert middle_way([7, 7, 7], [3, 8, 0]) == [7, 8]
    assert middle_way([5, 2, 9], [1, 4, 5]) == [2, 4]
    assert middle_way([1, 9, 7], [4, 8, 8]) == [9, 8]
    assert middle_way([1, 2, 3], [3, 1, 4]) == [2, 1]
    assert middle_way([1, 2, 3], [4, 1, 1]) == [2, 1]

def test_make_ends():
    assert make_ends([1, 2, 3]) == [1, 3]
    assert make_ends([1, 2, 3, 4]) == [1, 4]
    assert make_ends([7, 4, 6, 2]) == [7, 2]
    assert make_ends([1, 2, 2, 2, 2, 2, 2, 3]) == [1, 3]
    assert make_ends([7, 4]) == [7, 4]
    assert make_ends([7]) == [7, 7]
    assert make_ends([5, 2, 9]) == [5, 9]
    assert make_ends([2, 3, 4, 1]) == [2, 1]

def test_has23():
    assert has23([2, 5]) == True
    assert has23([4, 3]) == True
    assert has23([4, 5]) == False
    assert has23([2, 2]) == True
    assert has23([3, 2]) == True
    assert has23([3, 3]) == True
    assert has23([7, 7]) == False
    assert has23([3, 9]) == True
    assert has23([9, 5]) == False

