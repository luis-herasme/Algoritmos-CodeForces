def to_jaden_case(string):
    # ...
    words = string.split(" ")
    for idx, word in enumerate(words):
        words[idx] = word[0].upper() + word[1:]
    return " ".join(words)

print(to_jaden_case("hola mundo"))
