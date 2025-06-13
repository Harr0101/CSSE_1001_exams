def foo(xs:str, ys:str)-> bool:
    while "!" in xs:
        index = xs.find("!")
        if index:
            xs = xs[0:index-1] + xs[index+1:]
        else:
            xs = xs[1:]
            
    return xs == ys

def test_foo(foo):
    assert foo("ab!c", "ac")
    assert not foo("ab!!", "ab")
    assert foo("a!c", "c")

test_foo(foo)