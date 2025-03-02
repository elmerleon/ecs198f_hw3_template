import pytest



#Add testcases Here
def test_modThree():
    from foo_bar_baz import foo_bar_baz
    string = foo_bar_baz(3)
    words = string.split()
    fooCount = words.count("Foo")
    assert(fooCount == 1)

def test_madFive():
    from foo_bar_baz import foo_bar_baz
    string = foo_bar_baz(5)
    words = string.split()
    BarCount = words.count("Bar")
    assert(BarCount == 1)

def test_modThreeAndFive():
    from foo_bar_baz import foo_bar_baz
    string = foo_bar_baz(15)
    words = string.split()
    BazCount = words.count("Baz")
    assert(BazCount == 1)

def test_listEveryNum():
    from foo_bar_baz import foo_bar_baz
    string = foo_bar_baz(100)
    words = string.split()
    assert(len(words) == 100)
