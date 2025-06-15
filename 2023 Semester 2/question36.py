def substring(xs:str, ys:str)-> bool:
    if not xs:
        return True
    index=ys.find(xs[0])
    if index == -1:
        return False
    return substring(xs[1:],ys[index+1:])

def test_substring(substring):
    assert substring("ac", "abc")
    assert not substring("ca", "abc")

test_substring(substring)