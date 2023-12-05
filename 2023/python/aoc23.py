import argparse
import re
import sys

def init_arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('day')

    return parser

def get_calib_from_line(line):
    nums = [d for d in line if d.isdigit()]
    calib = int(f'{nums[0]}{nums[-1]}')

    return calib

def get_nums(line):
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
    res = []
    for num in nlt.keys():
        hits = re.finditer(num, line)
        for hit in hits:
            res.append((nlt[num], hit.start()))
    if res:
        return  [min(res, key=lambda x:x[1]), max(res, key=lambda x:x[1])]

def get_real_calib_from_line(line):
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

    return calib

def day01(input):
    sum = 0
    real_sum = 0

    for line in input:
        sum += get_calib_from_line(line)
        real_sum += get_real_calib_from_line(line)

    print(f'Day 1 first result: {sum}')
    print(f'Day 1 second result: {real_sum}')








def day02(input):
    return

def main(argv):
    parser = init_arg_parse()
    args = parser.parse_args()

    with open(f'./{args.day}/input.txt') as f:
        input = f.readlines()

    match args.day:
        case '01':
            day01(input)
        case '02':
            day02(input)
        case _:
            return
        


if __name__ == "__main__":
    main(sys.argv)