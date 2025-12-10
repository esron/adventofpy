import argparse
import sys
from importlib import import_module


def validate_year(value):
    """Validate year is between 2015 and 2025."""
    year = int(value)
    if year < 2015 or year > 2025:
        raise argparse.ArgumentTypeError(f'Year must be between 2015 and 2025, got {year}')
    return year


def validate_day(value):
    """Validate day is between 1 and 25."""
    day = int(value)
    if day < 1 or day > 25:
        raise argparse.ArgumentTypeError(f'Day must be between 1 and 25, got {day}')
    return day


def validate_part(value):
    """Validate part is either 1 or 2."""
    if value not in ['1', '2']:
        raise argparse.ArgumentTypeError(f'Part must be 1 or 2, got {value}')
    return value


def cli():
    """Advent of Python - Python solutions to Advent of Code."""
    parser = argparse.ArgumentParser(
        description='Advent of Python - Python solutions to Advent of Code.'
    )
    parser.add_argument(
        '-y', '--year',
        type=validate_year,
        required=True,
        help='Event year (2015-2023)'
    )
    parser.add_argument(
        '-d', '--day',
        type=validate_day,
        required=True,
        help='Problem day (1-25)'
    )
    parser.add_argument(
        '-p', '--part',
        type=validate_part,
        required=True,
        help='Problem part (1 or 2)'
    )

    args = parser.parse_args()

    print(f'Running script for year: {args.year}, day: {args.day:02d}, part: {args.part}')
    try:
        script = import_module(f'.part{args.part}', f'year_{args.year}.day{args.day:02d}')
        script.run()
    except ModuleNotFoundError:
        print(f'Module year_{args.year}.day{args.day:02d}.part{args.part} not found.', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    cli()
