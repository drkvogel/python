import asyncio
from pathlib import Path
import os

home = Path.home()


def aws_swap(args):
    credentials_file = home / '.aws/credentials'
    try:
        os.remove(str(credentials_file))
    except FileNotFoundError:
        pass
    os.symlink(str(home / '.aws/{}.credentials').format(args.credentials), str(credentials_file))


def aws_current(args):
    credentials_file = home / '.aws/credentials'
    print(credentials_file.resolve().stem)


def aws_add(args):
    file = home / '.aws/{}.credentials'.format(args.name)
    if file.is_file():
        print('Those credentials already exist')
    else:
        try:
            aws_access_key_id = input(
                'Enter aws_access_key_id:') if args.aws_access_key_id is None else args.aws_access_key_id
            aws_secret_access_key = input(
                'Enter aws_secret_access_key:') if args.aws_secret_access_key is None else args.aws_secret_access_key
            with file.open('w') as credentials_file:
                credentials_file.write("""[default]
aws_access_key_id = {id}
aws_secret_access_key = {key}""".format(id=aws_access_key_id, key=aws_secret_access_key))
        except KeyboardInterrupt:
            pass


def add_aws_parser(subparsers):
    aws_parser = subparsers.add_parser('aws')

    aws_subparsers = aws_parser.add_subparsers(dest='aws_command')
    aws_subparsers.required = True

    aws_current_parser = aws_subparsers.add_parser('current', help='tells you which aws credentials are being used')
    aws_current_parser.set_defaults(func=aws_current)

    aws_swap_parser = aws_subparsers.add_parser('swap', help='lets you swap between aws accounts')
    aws_swap_parser.set_defaults(func=aws_swap)

    aws_files = (home / '.aws').glob('**/*.credentials')
    aws_swap_parser.add_argument('credentials', choices=[file.stem for file in aws_files if file.is_file()])

    aws_add_parser = aws_subparsers.add_parser('add', help='add an accounts credentials')
    aws_add_parser.set_defaults(func=aws_add)

    aws_add_parser.add_argument('name', type=str)

    aws_add_parser.add_argument('--aws-access-key-id')
    aws_add_parser.add_argument('--aws-secret-access-key')
