from ppred import Matcher 

def test_wrap():
    m = Matcher(low=65500)
    assert m.match(65500)
    assert m.match(65535)
    assert m.match(0)
    assert m.match(987)
    assert not m.match(988)
    assert not m.match(32767)