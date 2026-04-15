from src.warmup_2 import *


def test_string_times():
    assert string_times('Hi', 2) == "HiHi"
    assert string_times('Hi', 3) == 'HiHiHi'
    assert string_times('Hi', 1) == 'Hi'
    assert string_times('Hi', 0) == ''
    assert string_times('Hi', 5) == 'HiHiHiHiHi'
    assert string_times('Oh Boy!', 2) == 'Oh Boy!Oh Boy!'
    assert string_times('x', 4) == 'xxxx'
    assert string_times('', 4) == ''
    assert string_times('code', 2) == 'codecode'
    assert string_times('code', 3) == 'codecodecode'


def test_front_times():
    assert front_times('Chocolate', 2) == 'ChoCho'
    assert front_times('Chocolate', 3) == 'ChoChoCho'
    assert front_times('Abc', 3) == 'AbcAbcAbc'
    assert front_times('Ab', 4) == 'AbAbAbAb'
    assert front_times('A', 4) == 'AAAA'
    assert front_times('', 4) == ''
    assert front_times('Abc', 0) == ''


def test_string_bits():
    assert string_bits('Hello') == 'Hlo'
    assert string_bits('Hi') == 'H'
    assert string_bits('Heeololeo') == 'Hello'
    assert string_bits('HiHiHi') == 'HHH'
    assert string_bits('') == ''
    assert string_bits('Greetings') == 'Getns'
    assert string_bits('Chocoate') == 'Coot'
    assert string_bits('pi') == 'p'
    assert string_bits('Hello Kitten') == 'HloKte'
    assert string_bits('hxaxpxpxy') == 'happy'


def test_string_splosion():
    assert string_splosion('Code') == 'CCoCodCode'
    assert string_splosion('abc') == 'aababc'
    assert string_splosion('ab') == 'aab'
    assert string_splosion('x') == 'x'
    assert string_splosion('fade') == 'ffafadfade'
    assert string_splosion('There') == 'TThTheTherThere'
    assert string_splosion('Kitten') == 'KKiKitKittKitteKitten'
    assert string_splosion('Bye') == 'BByBye'
    assert string_splosion('Good') == 'GGoGooGood'
    assert string_splosion('Bad') == 'BBaBad'


def test_last2():
    assert last2('hixxhi') == 1
    assert last2('xaxxaxaxx') == 1
    assert last2('axxxaaxx') == 2
    assert last2('xxaxxaxxaxx') == 3
    assert last2('xaxaxaxx') == 0
    assert last2('xxxx') == 2
    assert last2('13121312') == 1
    assert last2('11212') == 1
    assert last2('13121311') == 0
    assert last2('1717171') == 2
    assert last2('hi') == 0
    assert last2('h') == 0
    assert last2('') == 0


def test_array_count9():
    assert array_count9([1, 2, 9]) == 1
    assert array_count9([1, 9, 9]) == 2
    assert array_count9([1, 9, 9, 3, 9]) == 3
    assert array_count9([1, 2, 3]) == 0
    assert array_count9([]) == 0
    assert array_count9([4, 2, 4, 3, 1]) == 0
    assert array_count9([9, 2, 4, 3, 1]) == 1


def test_array_front9():
    assert array_front9([1, 2, 9, 3, 4]) == True
    assert array_front9([1, 2, 3, 4, 9]) == False
    assert array_front9([1, 2, 3, 4, 5]) == False
    assert array_front9([9, 2, 3]) == True
    assert array_front9([1, 9, 9]) == True
    assert array_front9([1, 2, 3]) == False
    assert array_front9([1, 9]) == True
    assert array_front9([5, 5]) == False
    assert array_front9([2]) == False
    assert array_front9([9]) == True
    assert array_front9([]) == False
    assert array_front9([3, 9, 2, 3, 3]) == True


def test_array123():
    assert array123([1, 1, 2, 3, 1]) == True
    assert array123([1, 1, 2, 4, 1]) == False
    assert array123([1, 1, 2, 1, 2, 3]) == True
    assert array123([1, 1, 2, 1, 2, 1]) == False
    assert array123([1, 2, 3, 1, 2, 3]) == True
    assert array123([1, 2, 3]) == True
    assert array123([1, 1, 1]) == False
    assert array123([1, 2]) == False
    assert array123([1]) == False
    assert array123([]) == False


def test_string_match():
    assert string_match('xxcaazz', 'xxbaaz') == 3
    assert string_match('abc', 'abc') == 2
    assert string_match('abc', 'axc') == 0
    assert string_match('hello', 'he') == 1
    assert string_match('he', 'hello') == 1
    assert string_match('h', 'hello') == 0
    assert string_match('', 'hello') == 0
    assert string_match('aabbccdd', 'abbbxxd') == 1
    assert string_match('aaxxaaxx', 'iaxxai') == 3
    assert string_match('iaxxai', 'aaxxaaxx') == 3
