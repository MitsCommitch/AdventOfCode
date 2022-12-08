import os
from itertools import zip_longest

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{path}{os.sep}bags.txt') as s:
        bags = s.read().splitlines()

    groups = findGroups(bags)

    prios = []
    for group in groups:
        prios.append(findPrio(group))

    print(f'Sum of priorities of all group items is: {sum(prios)}')

def findGroups(bags):
    groups = []
    for b1, b2, b3 in grouper(bags, 3):
        s1, s2, s3 = set(b1), set(b2), set(b3)
        dupe = set.intersection(s1, s2, s3)
        if len(dupe) == 1:
            groups.append(dupe.pop())
    return groups

# From itertools recipes
def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')

def findPrio(item):
    if item.isupper():
        prio = ord(item) - 38
    else:
        prio = ord(item) - 96
    return prio

if __name__ == "__main__":
    main()