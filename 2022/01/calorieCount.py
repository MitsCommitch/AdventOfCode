import os
import itertools

def main():

    path = os.path.dirname(os.path.realpath(__file__))

    with open(f'{path}{os.sep}calories.txt') as c:
        calList = [int(x) if x != '' else '' for x in c.read().splitlines()]

    elfCalDict = processElfCalList(calList)

    max_cals = getMaxN(elfCalDict, 3)

    print(f'Elf with the max cals has {max_cals[0]} while the top 3 have {sum(max_cals)} total.')


def processElfCalList(calList):
    elves = {}

    cals =  [sum(list(y)) for x, y in itertools.groupby(calList, lambda z: z == '') if not x]

    elves = {i:e for i, e in zip(range(len(cals)), cals)}

    return elves

def getMaxN(d, n):
    maxes = []

    while len(maxes) < n:
        m = (max(d, key=d.get))
        maxes.append(d.pop(m))

    return maxes

if __name__ == "__main__":
    main()