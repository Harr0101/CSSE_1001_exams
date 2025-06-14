def foo(f_path: str, word:str)-> list[str]:
    with open(f_path,"rt") as file:
        lines = file.readlines()
    words = []
    for line in lines:
        words.extend(line.split())
    acc = []
    for i, w in enumerate(words):
        if w == word:
            acc.append(words[i-1])
    return acc
        

def test_foo(foo):
    assert foo("2023 Semester 1/run.txt", "spot") ==  ['See', 'run', 'see', 'run', 'see', 'see','spot']
    
test_foo(foo)