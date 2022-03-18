# XOR
Python3 XOR encryption with rotating key

## Features:
* Supports a rotating integer or string encryption key.
* Accepts binary file as input or pass it a string. 
* Prints encrypted result to console as hex, or writes an encrypted binary file.
* All output is null byte terminated.
* Prints hex chars with no padding or '0' padding. e.g., 0x0 => 0x00

## Usage:
```bash
usage: xor.py [-h] [-k K] [-f F] [-s S] [-w W]

optional arguments:
  -h, --help  show this help message and exit 
  -k K        XOR key
  -f F        bin file containing payload     
  -s S        String to XOR
  -w W        File to write encrypted binary payload to
  --pad, --no-pad  Pad with 0 so all output is 2 chars wide 0x0 => 0x00 (default: --no-pad)
  ```

## Examples:
```bash
# Encrypt file with mysecretkey and print output in hex format
python3 ./xor.py -f myfile.bin -k secretkey

# Encrypt string
python3 ./xor.py -s SomeFunctionCall -k secretkey
{ 0x20, 0xa, 0xe, 0x17, 0x23, 0x1, 0x5, 0x6, 0xd, 0x1a, 0xa, 0xd, 0x31, 0x4, 0x18, 0x7, 0x0 };

# Encrypt binary file and output encrypted binary file
python3 ./xor.py -f meterpreter.bin -k 1337 -w meterpreter.enc
```