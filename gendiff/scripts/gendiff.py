import argparse

from gendiff import generate_diff


def make_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        type=str,
                        default='stylish')
    return parser.parse_args()


def main():
    args = make_parser()

    print(generate_diff(args.first_file, args.second_file, format=args.format))


if __name__ == '__main__':
    main()