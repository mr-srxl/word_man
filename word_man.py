import wordlist
import time
from colorama import Fore
import argparse
import random
import string


def generate_strong_password(length=20, uppercase=True, lowercase=True, digits=True, punctuation=True):
    characters = []
    if uppercase:
        characters.extend(string.ascii_uppercase)
    if lowercase:
        characters.extend(string.ascii_lowercase)
    if digits:
        characters.extend(string.digits)
    if punctuation:
        characters.extend(string.punctuation)
    password = ''.join(random.choice(characters) for _ in range(length))
    print(password)


def passwd_list(charset, max, min, output_file=None):
    maximum = len(charset)
    print(Fore.MAGENTA + f'Warning: The max size can be produce is {maximum}')
    generate = wordlist.Generator(charset)
    if max <= maximum and min <= maximum:
        for word in generate.generate(min, max):
            if output_file:
                with open(output_file, 'a') as f:
                    print(word, file=f)
            else:
                print(word)
        print("it\'s down")
    else:
        print(Fore.RED + "[!]the limit of the max and min is wrong\n ")
        time.sleep(7)
    # clear()


def pattern_word(charset, pattern, output_file=None):
    generator = wordlist.Generator(charset)
    for word in generator.generate_with_pattern(pattern):
        if output_file:
            with open(output_file, 'a') as f:
                print(word, file=f)
        else:
            print(word)


parser = argparse.ArgumentParser(prog="word_man.py",
                                 description="A tool for generating wordlists and strong passwords.",
                                 formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("-m", "--mode",
                    choices=[1, 2, 3],
                    required=True,
                    type=int,
                    help="""Choose a mode:
          1. Simple wordlist (all combinations)
          2. Wordlist with pattern
          3. Strong password generator
          """)

# Character Set (for Modes 1 and 2)
parser.add_argument("-s", "--string",
                    help="Character set for word generation (e.g., 'abcdefghijklmnopqrstuvwxyz')",
                    type=str)

parser.add_argument("-max", "--max",
                    help="Maximum word length",
                    type=int)
parser.add_argument("-min", "--min",
                    help="Minimum word length",
                    type=int)

parser.add_argument("-p", "--pattern",
                    help="Pattern for word generation (e.g., '@@@y@si@' for 3-letter words)",
                    type=str)

parser.add_argument("-o", "--output",
                    help="Output file name",
                    type=str)

args = parser.parse_args()

if args.mode == 1:
    if args.string and args.min and args.max:
        if args.output:
            passwd_list(args.string, args.max, args.min, output_file=args.output)
        else:
            passwd_list(args.string, args.max, args.min)
    else:
        parser.print_help()

elif args.mode == 2:
    if args.pattern and args.string:
        if args.output:
            pattern_word(args.string, args.pattern, output_file=args.output)
        else:
            pattern_word(args.string, args.pattern)
    else:
        parser.print_help()

elif args.mode == 3:
    generate_strong_password()

else:
    print("Invalid option")
    parser.print_help()
