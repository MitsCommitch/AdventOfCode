import re
import sys

nlt = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def get_nums(line):
    res = []
    print(f'Line: {line}')
    for num in nlt.keys():
        hits = re.finditer(num, line)
        for hit in hits:
            res.append((nlt[num], hit.start()))
    if res:
        print(f'Res: {res}')
        return  [min(res, key=lambda x:x[1]), max(res, key=lambda x:x[1])]


def get_calib_from_line(line):
    digits = list(filter(str.isdigit, line))
    if digits:
        first, last = (digits[0], digits[-1])
        fi, li = (line.find(first), line.rfind(last))
    wordnums = get_nums(line)
    if wordnums:
        fw, fwi = wordnums[0]
        if fi > fwi:
            first = fw

        lw, lwi = wordnums[1]
        if li < lwi:
            last = lw

    calib = int(f'{first}{last}')

    print(f'{calib}')

    return calib

def main(argv):
    if len(argv) < 1:
        sys.exit("Please provide a filename.")

    input_file = argv[0]
    sum = 0

    try:
        with open(input_file) as f:
            for line in f:
                sum += get_calib_from_line(line)
    except FileNotFoundError as e:
        sys.exit(e)

    print(f'Final sum was: {sum}')

if __name__ == "__main__":
    main(sys.argv[1:])