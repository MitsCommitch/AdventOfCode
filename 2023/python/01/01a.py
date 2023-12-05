import sys

def get_calib_from_line(line):
    nums = [d for d in line if d.isdigit()]
    calib = int(f'{nums[0]}{nums[-1]}')

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