#!/usr/bin/python

"""
Program to make random files of a disired size!
"""

import random, sys, string
from argparse import ArgumentParser

# Usage Message
def msg(name=None):
    return '''makeRandFile [OPTION]... SIZE'''
def main():

    parser = ArgumentParser(description='''Make a random file of printable characters of size SIZE''', usage=msg())
    parser.add_argument("SIZE", type=int, help="size of file in bytes")
    parser.add_argument("-o", "--output-file", type=str, help="write contents into OUTPUT_FILE")
 
    size_group = parser.add_mutually_exclusive_group()
    size_group.add_argument("-K", "--kilobytes", action="store_true", help="SIZE is in terms of kilobytes")
    size_group.add_argument("-M", "--megabytes", action="store_true", help="SIZE is in terms of megabytes")
    
    type_group = parser.add_mutually_exclusive_group()
    type_group.add_argument("-d", "--digits", action="store_true", help="file of only random digits")
    type_group.add_argument("-L", "--letters", action="store_true", help="file of only random letters")
    type_group.add_argument("-u", "--uppercase", action="store_true", help="file of only uppercase letters")
    type_group.add_argument("-l", "--lowercase", action="store_true", help="file of only lowercase letters") 
    type_group.add_argument("-p", "--punctuation", action="store_true", help="file of only punctuation characters")
   
    args = parser.parse_args()

    if args.SIZE < 0:
        parser.error("SIZE must be 0 or positive")
        
    # adjust for -K and -M options
    if args.kilobytes:
        SIZE = args.SIZE * 1000
    elif args.megabytes:
        SIZE = args.SIZE * 1000000
    else:
        SIZE = args.SIZE    

    # adjust what characters to print
    if args.digits:
        str_bank = string.digits
    elif args.letters:
        str_bank = string.ascii_letters
    elif args.lowercase:
        str_bank = string.ascii_lowercase
    elif args.uppercase:
        str_bank = string.ascii_uppercase
    elif args.punctuation:
        str_bank = string.punctuation
    else:
        str_bank = string.printable

    # make the output string
    output_str = ""
    for i in range(SIZE):
        output_str += random.choice(str_bank)

    # adjust for output file
    if args.output_file is not None:
        try:
            with open(args.output_file,"w") as f:
                f.write(output_str)
        except:
            parser.error("{}: Error opening and writing to file".format(args.output_file))
    else:
        sys.stdout.write(output_str)

if __name__ == "__main__":
    main()
