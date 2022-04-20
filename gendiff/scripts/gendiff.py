import argparse
from gendiff.gendiff import generate_diff


def make_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)

    # Optional arguments
    parser.add_argument(
        "-f", "--format", default='stylish',
        choices=['stylish', 'plain', 'json'],
        help="set format of output"
    )
    return parser


def main():
    parser = make_parser()
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
