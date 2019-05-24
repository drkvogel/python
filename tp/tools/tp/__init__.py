import argparse
import argcomplete

from .aws import add_aws_parser


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(description='Sub description', dest='command')
    subparsers.required = True

    add_aws_parser(subparsers)

    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    args.func(args)
