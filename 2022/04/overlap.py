import os

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{path}{os.sep}assignments.txt') as s:
        areas = s.read().splitlines()

    total = partial = 0

    for assignment in areas:
        a1, a2 = assignment.split(',')
        ranges = getAssignmentRange(a1, a2)
        if checkTotalOverlap(ranges):
            total = total + 1
            partial = partial + 1
        elif checkPartialOverlap(ranges):
            partial = partial + 1

    print(f'There are {total} full overlaps of areas.')
    print(f'There are {partial} partial overlaps of areas.')


def getAssignmentRange(a1, a2):
    r1 = [int(x) for x in a1.split('-')]
    r2 = [int(x) for x in a2.split('-')]

    return (r1, r2)


def checkTotalOverlap(ranges):
    s1, e1 = ranges[0]
    s2, e2 = ranges[1]
    
    if s1 == s2 or e1 == e2:
        return True

    if s1 < s2 and e1 > e2:
        return True

    if s2 < s1 and e2 > e1:
        return True

    return False


def checkPartialOverlap(ranges):
    s1, e1 = ranges[0]
    s2, e2 = ranges[1]
    
    overlap = range(max(s1, s2), min(e1, e2)+1)

    if overlap:
        return True

    return False


if __name__ == "__main__":
    main()