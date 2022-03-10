import argparse

from gendiff.gendiff import generate_diff
from gendiff.stylish import stylish


def main():
    print('IM IN SCRIPT')
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)

    # Optional arguments
    parser.add_argument("-f", "--format", help="set format of output")

    args = parser.parse_args()
    # print(args.accumulate(args.integers))

    diff = stylish(generate_diff(args.first_file, args.second_file))
    print('IN SCRIPT {}'.format(diff))
    print(diff)


if __name__ == '__main__':
    main()
