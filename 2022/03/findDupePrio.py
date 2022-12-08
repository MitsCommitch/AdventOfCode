import os

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{path}{os.sep}bags.txt') as s:
        bags = s.read().splitlines()

    dupes = findDupes(bags)

    prios = []
    for dupe in dupes:
        prios.append(findPrio(dupe))

    print(f'Sum of priorities of all duped items is: {sum(prios)}')

def findDupes(bags):
    dupes = []
    for bag in bags:
        half = int(len(bag)/2)
        c1, c2 = set(bag[:half]), set(bag[half:])
        dupe = set.intersection(c1, c2)
        if len(dupe) == 1:
            dupes.append(dupe.pop())
    return dupes

def findPrio(item):
    if item.isupper():
        prio = ord(item) - 38
    else:
        prio = ord(item) - 96
    return prio

if __name__ == "__main__":
    main()