from src.string_1 import *


def test_hello_name():
    assert hello_name('Bob') == 'Hello Bob!'
    assert hello_name('Alice') == 'Hello Alice!'
    assert hello_name('X') == 'Hello X!'
    assert hello_name('Dolly') == 'Hello Dolly!'
    assert hello_name('Alpha') == 'Hello Alpha!'
    assert hello_name('Omega') == 'Hello Omega!'
    assert hello_name('Goodbye') == 'Hello Goodbye!'
    assert hello_name('ho ho ho') == 'Hello ho ho ho!'
    assert hello_name('xyz!') == 'Hello xyz!!'
    assert hello_name('Hello') == 'Hello Hello!'


def test_make_abba():
    assert make_abba('Hi', 'Bye') == 'HiByeByeHi'
    assert make_abba('Yo', 'Alice') == 'YoAliceAliceYo'
    assert make_abba('What', 'Up') == 'WhatUpUpWhat'
    assert make_abba('aaa', 'bbb') == 'aaabbbbbbaaa'
    assert make_abba('x', 'y') == 'xyyx'
    assert make_abba('x', '') == 'xx'
    assert make_abba('', 'y') == 'yy'
    assert make_abba('Bo', 'Ya') == 'BoYaYaBo'
    assert make_abba('Ya', 'Ya') == 'YaYaYaYa'


def test_make_tags():
    assert make_tags('i', 'Yay') == '<i>Yay</i>'
    assert make_tags('i', 'Hello') == '<i>Hello</i>'
    assert make_tags('cite', 'Yay') == '<cite>Yay</cite>'
    assert make_tags('address', 'here') == '<address>here</address>'
    assert make_tags('body', 'Heart') == '<body>Heart</body>'
    assert make_tags('i', 'i') == '<i>i</i>'
    assert make_tags('i', '') == '<i></i>'


def test_make_out_word():
    assert make_out_word('<<>>', 'Yay') == '<<Yay>>'
    assert make_out_word('<<>>', 'WooHoo') == '<<WooHoo>>'
    assert make_out_word('[[]]', 'word') == '[[word]]'
    assert make_out_word('HHoo', 'Hello') == 'HHHellooo'
    assert make_out_word('abyz', 'YAY') == 'abYAYyz'


def test_extra_end():
    assert extra_end('Hello') == 'lololo'
    assert extra_end('ab') == 'ababab'
    assert extra_end('Hi') == 'HiHiHi'
    assert extra_end('Candy') == 'dydydy'
    assert extra_end('Code') == 'dedede'


def test_first_two():
    assert first_two('Hello') == 'He'
    assert first_two('abcdefg') == 'ab'
    assert first_two('ab') == 'ab'
    assert first_two('a') == 'a'
    assert first_two('') == ''
    assert first_two('Kitten') == 'Ki'
    assert first_two('hi') == 'hi'
    assert first_two('hiya') == 'hi'


def test_first_half():
    assert first_half('WooHoo') == 'Woo'
    assert first_half('HelloThere') == 'Hello'
    assert first_half('abcdef') == 'abc'
    assert first_half('ab') == 'a'
    assert first_half('') == ''
    assert first_half('0123456789') == '01234'
    assert first_half('kitten') == 'kit'


def test_without_end():
    assert without_end('Hello') == 'ell'
    assert without_end('java') == 'av'
    assert without_end('coding') == 'odin'
    assert without_end('code') == 'od'
    assert without_end('ab') == ''
    assert without_end('Chocolate!') == 'hocolate'
    assert without_end('kitten') == 'itte'
    assert without_end('woohoo') == 'ooho'


def test_combo_string():
    assert combo_string('Hello', 'hi') == 'hiHellohi'
    assert combo_string('hi', 'Hello') == 'hiHellohi'
    assert combo_string('aaa', 'b') == 'baaab'
    assert combo_string('b', 'aaa') == 'baaab'
    assert combo_string('aaa', '') == 'aaa'
    assert combo_string('', 'bb') == 'bb'
    assert combo_string('aaa', '1234') == 'aaa1234aaa'
    assert combo_string('aaa', 'bb') == 'bbaaabb'
    assert combo_string('a', 'bb') == 'abba'
    assert combo_string('bb', 'a') == 'abba'
    assert combo_string('xyz', 'ab') == 'abxyzab'


def test_non_start():
    assert non_start('Hello', 'There') == 'ellohere'
    assert non_start('java', 'code') == 'avaode'
    assert non_start('shotl', 'java') == 'hotlava'
    assert non_start('ab', 'xy') == 'by'
    assert non_start('ab', 'x') == 'b'
    assert non_start('x', 'ac') == 'c'
    assert non_start('a', 'x') == ''
    assert non_start('kit', 'kat') == 'itat'
    assert non_start('mart', 'dart') == 'artart'


def test_left2():
    assert left2('Hello') == 'lloHe'
    assert left2('java') == 'vaja'
    assert left2('Hi') == 'Hi'
    assert left2('code') == 'deco'
    assert left2('cat') == 'tca'
    assert left2('12345') == '34512'
    assert left2('Chocolate') == 'ocolateCh'
    assert left2('bricks') == 'icksbr'
