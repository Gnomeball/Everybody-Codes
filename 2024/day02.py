# Part one

with open("./data/day02-a.txt") as file:
    runes, words = file.read().split("\n\n")
    runes = runes.replace("WORDS:", "").split(",")
    words = words.replace(".", "").replace(",", "")#.replace(" ", "")

# print(runic, words)

total = sum(words.count(rune) for rune in runes)

print("Part one =", total)

# Part two

with open("./data/day02-b.txt") as file:
    runes, words = file.read().split("\n\n")
    runes = runes.replace("WORDS:", "").split(",")
    words = words.splitlines()

# print(runic, words)

# function to count how many letters in a word are used by all runes

def count_used_letters(word, runes):

    # function to count how many letters in a word are used by a rune

    def used_letters_by_rune(word, rune):
        used = set()
        rune_len = len(rune)
        reversed_rune = rune[::-1]
        for i in range(len(word)-rune_len+1):
            snippet = word[i:i+rune_len]
            if rune == snippet or reversed_rune == snippet:
                used = used.union(_ for _ in range(i, i+rune_len))
        return used

    used = set()
    for rune in runes:
        used = used.union(used_letters_by_rune(word, rune))
    return len(used)

total = sum(count_used_letters(word, runes) for word in words)

print("Part two =", total)

# Part three

# it can wait
