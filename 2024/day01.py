# Global map for potion costs

POTION_COSTS = { 'A': 0, 'B': 1, 'C': 3, 'D': 5, 'x': 0 }

# Global map tracking additional costs when monsters pair up

PAIRED_COSTS = { 0: 0, 1: 0, 2: 2, 3: 6 }

# Function .. with closures?

def score(monsters):

    def usage_single(single):
        return POTION_COSTS[single]

    def usage_double(double):
        left, right = double
        usage  = POTION_COSTS[left]
        usage += POTION_COSTS[right]
        usage += PAIRED_COSTS[2 - double.count('x')]
        return usage

    def usage_triple(triple):
        a, b, c = triple
        usage  = POTION_COSTS[a]
        usage += POTION_COSTS[b]
        usage += POTION_COSTS[c]
        usage += PAIRED_COSTS[3 - triple.count('x')]
        return usage

    match len(monsters):
        case 1: return usage_single(monsters)
        case 2: return usage_double(monsters)
        case 3: return usage_triple(monsters)

# Tests?

TEST_INPUTS = [ "A B B A C", "Ax BC DD CA xD", "xBx AAA BCD xCC" ]

assert sum(map(score, TEST_INPUTS[0].split())) == 5
assert sum(map(score, TEST_INPUTS[1].split())) == 28
assert sum(map(score, TEST_INPUTS[2].split())) == 30

# And go!

with open("./data/day01-a.txt") as file:
    print("Part one =", sum(map(score, [ _ for _ in file.read() ])))

with open("./data/day01-b.txt") as file:
    text = file.read()
    print("Part two =", sum(map(score, [ text[i:i+2] for i in range(0, len(text) - 1, 2) ])))

with open("./data/day01-c.txt") as file:
    text = file.read()
    print("Part three =", sum(map(score, [ text[i:i+3] for i in range(0, len(text) - 2, 3) ])))
