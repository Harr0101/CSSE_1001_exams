def remove_adjacent_pairs(cs):
    new= cs[0]
    for i, char in enumerate(cs[1:]):
        if char == new[-1]:
            return remove_adjacent_pairs(new[:-1] + cs[i+2:])
        new+= char
    return cs

def test_adjacent_pairs(func):
    assert func("abbaca") == "ca"
    assert func("aaac") == "ac"
    assert func("azxxzy") == "ay"

test_adjacent_pairs(remove_adjacent_pairs)
