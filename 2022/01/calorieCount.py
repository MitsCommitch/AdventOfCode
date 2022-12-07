import os
import itertools

def main():
    """Setup and output."""
    path = os.path.dirname(os.path.realpath(__file__))

    with open(f'{path}{os.sep}calories.txt') as c:
        # Input is a list of calories carried by each elf, elves 
        # separated by blank lines

        # The `if X != '' else ''` bit ensures that we convert
        # string input to ints but preserve blank lines
        calList = [int(x) if x != '' else '' for x in c.read().splitlines()]

    # Process input into a list of calories carried by each elf
    elfCalDict = processElfCalList(calList)

    # Get sorted descending list of max cals
    max_cals = getMaxN(elfCalDict, 3)

    print(f'Elf {max_cals[0][0]} has the max cals with {max_cals[0][1]}')
    print(f'The top {len(max_cals)} elves, {[i for i, j in max_cals]} have {sum([j for i, j in max_cals])} total.')


def processElfCalList(calList):
    """Take a blank line separated list of calories by elf and return a list
    of each elves total calories. """
    elves = {}

    # Generate a sublist for each elf, splitting groups by ''
    # then sum the sublists
    cals =  [sum(list(y)) for x, y in itertools.groupby(calList, lambda z: z == '') if not x]

    # Problem didn't state a need to know which elf has what, but just in case
    elves = {i:e for i, e in zip(range(len(cals)), cals)}

    return elves

def getMaxN(d, n):
    maxes = []

    while len(maxes) < n:
        m = (max(d, key=d.get))
        maxes.append((m, d.pop(m)))

    return maxes

if __name__ == "__main__":
    main()