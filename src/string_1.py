def hello_name(name):
    """
    Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

    """
    return 'Hello ' + name + '!'


def make_abba(a, b):
    """
    Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

    """
    return a + b + b + a


def make_tags(tag, word):
    """
    The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

    """
    tag = '<' + tag + '>'
    closing_tag = tag[0] + '/' + tag[1:]
    return tag+word+closing_tag


def make_out_word(out, word):
    """
    Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

    """
    pre_out = out[0:2]
    post_out = out[2:]
    return pre_out + word + post_out


def extra_end(str):
    """_
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The original string will be at least length 2.
    """

    end_str = str[-2:]
    return end_str*3


def first_two(str):
    """
    Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X" and the empty string "" yields the empty string "".
    """
    if len(str) < 2:
        return str
    two_chars = str[0:2]
    return two_chars


def first_half(str):
    """
    Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

    """
    half = (len(str) // 2) # floor division operator //. This ensures the result is an integer.
    return str[0:half]


def without_end(str):
    """
    Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

    """
    return str[1:-1]


def combo_string(a, b):
    """
    Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

    """
    long, short = '', ''
    if len(a) > len(b):
        long = a
        short = b
    else:
        long = b
        short = a

    return short+long+short


def non_start(a, b):
    """
    Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

    """
    return a[1:]+b[1:]


def left2(str):
    """
    Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.


    """
    return str[2:]+str[0:2]
