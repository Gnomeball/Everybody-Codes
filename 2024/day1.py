
MONSTER_COSTS = {
    'A': 0,
    'B': 1,
    'C': 3,
    'D': 5,
    'x': 0,
}

# Part one

with open("./data/day1-a.txt") as file:
    monsters = [ _ for _ in file.read() ]

# function to track potion usage per monster

def potion_usage(monsters):
    potions_needed = []
    for m in monsters:
        potions_needed.append(MONSTER_COSTS[m])
    return potions_needed

print(sum(potion_usage(monsters)))

# Part two

with open("./data/day1-b.txt") as file:
    text = [ _ for _ in file.read() ]
    monsters = [ str(text[i] + text[i+1]) for i in range(0, len(text) - 1, 2) ]

# print(monsters)

# function to track potion usage per monster

def potion_usage(monsters):
    potions_needed = []
    for l,r in monsters:
        potions_needed.append(MONSTER_COSTS[l])
        potions_needed.append(MONSTER_COSTS[r])
        if not (l == "x" or r == "x"):
            potions_needed.append(2)
        #     print(l, r, potions_needed[-3:])
        # else:
        #     print(l, r, potions_needed[-2:])

    return potions_needed

print(sum(potion_usage(monsters)))

# Part three

with open("./data/day1-c.txt") as file:
    text = [ _ for _ in file.read() ]
    monsters = [ str(text[i] + text[i+1] + text[i+2]) for i in range(0, len(text) - 2, 3) ]

# print(monsters)

# function to track potion usage per monster

def potion_usage(monsters):
    potions_needed = []
    for a,b,c in monsters:
        potions_needed.append(MONSTER_COSTS[a])
        potions_needed.append(MONSTER_COSTS[b])
        potions_needed.append(MONSTER_COSTS[c])
        x_count = sum(1 if _ == "x" else 0 for _ in [a,b,c])
        match x_count:
            case 0: potions_needed.append(6)
            case 1: potions_needed.append(2)
            case 2: potions_needed.append(0)
            # case 3: potions_needed.append(0)
        # if not (l == "x" or r == "x"):
        #     potions_needed.append(2)
        #     print(l, r, potions_needed[-3:])
        # else:
        #     print(l, r, potions_needed[-2:])

    return potions_needed

print(sum(potion_usage(monsters)))