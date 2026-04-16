from src.logic_1 import *


def test_cigar_party():
    assert cigar_party(30, False) == False
    assert cigar_party(50, False) == True
    assert cigar_party(70, True) == True
    assert cigar_party(30, True) == False
    assert cigar_party(50, True) == True
    assert cigar_party(60, False) == True
    assert cigar_party(61, False) == False
    assert cigar_party(40, False) == True
    assert cigar_party(39, False) == False
    assert cigar_party(40, True) == True
    assert cigar_party(39, True) == False


def test_date_fashion():
    assert date_fashion(5, 10) == 2
    assert date_fashion(5, 2) == 0
    assert date_fashion(5, 5) == 1
    assert date_fashion(3, 3) == 1
    assert date_fashion(10, 2) == 0
    assert date_fashion(2, 9) == 0
    assert date_fashion(9, 9) == 2
    assert date_fashion(10, 5) == 2
    assert date_fashion(2, 2) == 0
    assert date_fashion(3, 7) == 1
    assert date_fashion(2, 7) == 0
    assert date_fashion(6, 2) == 0


def test_squirrel_play():
    assert squirrel_play(70, False) == True
    assert squirrel_play(95, False) == False
    assert squirrel_play(95, True) == True
    assert squirrel_play(90, False) == True
    assert squirrel_play(90, True) == True
    assert squirrel_play(50, False) == False
    assert squirrel_play(50, True) == False
    assert squirrel_play(100, False) == False
    assert squirrel_play(100, True) == True
    assert squirrel_play(105, True) == False
    assert squirrel_play(59, False) == False
    assert squirrel_play(59, True) == False
    assert squirrel_play(60, False) == True


def test_caught_speeding():
    assert caught_speeding(60, False) == 0
    assert caught_speeding(65, False) == 1
    assert caught_speeding(65, True) == 0
    assert caught_speeding(80, False) == 1
    assert caught_speeding(85, False) == 2
    assert caught_speeding(85, True) == 1
    assert caught_speeding(70, False) == 1
    assert caught_speeding(75, False) == 1
    assert caught_speeding(75, True) == 1
    assert caught_speeding(40, False) == 0
    assert caught_speeding(40, True) == 0
    assert caught_speeding(90, False) == 2


def test_sorta_sum():
    assert sorta_sum(3, 4) == 7
    assert sorta_sum(9, 4) == 20
    assert sorta_sum(10, 11) == 21
    assert sorta_sum(12, -3) == 9
    assert sorta_sum(-3, 12) == 9
    assert sorta_sum(4, 5) == 9
    assert sorta_sum(4, 6) == 20
    assert sorta_sum(14, 7) == 21
    assert sorta_sum(14, 6) == 20


def test_alarm_clock():
    assert alarm_clock(1, False) == '7:00'
    assert alarm_clock(5, False) == '7:00'
    assert alarm_clock(0, False) == '10:00'
    assert alarm_clock(6, False) == '10:00'
    assert alarm_clock(0, True) == 'off'
    assert alarm_clock(6, True) == 'off'
    assert alarm_clock(1, True) == '10:00'
    assert alarm_clock(3, True) == '10:00'
    assert alarm_clock(5, True) == '10:00'


def test_love6():
    assert love6(6, 4) == True
    assert love6(4, 5) == False
    assert love6(1, 5) == True
    assert love6(1, 6) == True
    assert love6(1, 8) == False
    assert love6(1, 7) == True
    assert love6(7, 5) == False
    assert love6(8, 2) == True
    assert love6(6, 6) == True
    assert love6(-6, 2) == False
    assert love6(-4, -10) == True
    assert love6(-7, 1) == False
    assert love6(7, -1) == True
    assert love6(-6, 12) == True
    assert love6(-2, -4) == False
    assert love6(7, 1) == True
    assert love6(0, 9) == False
    assert love6(8, 3) == False
    assert love6(3, 3) == True
    assert love6(3, 4) == False


def test_in1to10():
    assert in1to10(5, False) == True
    assert in1to10(11, False) == False
    assert in1to10(11, True) == True
    assert in1to10(10, False) == True
    assert in1to10(10, True) == True
    assert in1to10(9, False) == True
    assert in1to10(9, True) == False
    assert in1to10(1, False) == True
    assert in1to10(1, True) == True
    assert in1to10(0, False) == False
    assert in1to10(0, True) == True
    assert in1to10(-1, False) == False
    assert in1to10(-1, True) == True
    assert in1to10(99, False) == False
    assert in1to10(-99, True) == True


def test_near_ten():
    assert near_ten(12) == True
    assert near_ten(17) == False
    assert near_ten(19) == True
    assert near_ten(31) == True
    assert near_ten(6) == False
    assert near_ten(10) == True
    assert near_ten(11) == True
    assert near_ten(21) == True
    assert near_ten(22) == True
    assert near_ten(23) == False
    assert near_ten(54) == False
    assert near_ten(155) == False
    assert near_ten(158) == True
    assert near_ten(3) == False
    assert near_ten(1) == True
