#!/usr/bin/env python3

import argparse
import sys

def xor(data, key):
    res = b''
    for i in range(len(data)):
        curr_key = ord(key[i % len(key)])
        res += bytes(chr(data[i] ^ curr_key), 'latin-1')
        if i == len(data) - 1:
            res += b'\0'
    return res

def print_output(ciphertext, pad):
    padding = '02x' if pad == True else '1x'
    print('{ 0x' + ', 0x'.join(format(x, padding) for x in ciphertext) + ' };')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='xor.py')
    parser.add_argument(
        '-k', help='XOR key'
    )
    parser.add_argument(
       '-f', help='bin file containing payload' 
    )
    parser.add_argument(
        '-s', help='String to XOR'
    )
    parser.add_argument(
        '-w', help="File to write encrypted binary payload to"
    )
    parser.add_argument(
        '--pad', dest='pad', help="Pad with 0 so all output is 2 chars wide 0x0 => 0x00", action=argparse.BooleanOptionalAction, default='--no-pad' 
    )
    args = parser.parse_args()

    if args.f == None and args.s == None:
        parser.print_help()
        sys.exit()

    if args.f != None:
        with open(args.f, mode='rb') as file:
            buf = file.read()
            file.close()
    else:
        buf = bytes(args.s, 'latin-1')

    ciphertext = xor(buf, args.k)
    if args.w != None:
        with open(args.w, mode='wb') as file:
            file.write(ciphertext)
            file.close
    else:
        print_output(ciphertext, args.pad)
